#! /usr/bin/env python

import random, time, platform, sys, os, threading
from datetime import datetime
import wakeup_game as wakeup
from . import client

if platform.system() == "Linux":
    from gpiozero import Button
    import pygame
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sounds/solid_snake_is_dummy_thicc.wav")
    print("Sound initialized")


class Alarm:
    def __init__(self):
        self.snooze = Button(17)
        self.game = wakeup.Game()
        self.status = False
        self.alarms_file = "alarm_times.txt"
        if not (os.path.isfile(self.alarms_file)):
            set_time("06:00")

    def set_time(self, time):
        #time is a string with format %HH:%MM
        with open(self.alarms_file, 'w') as f:
            f.write(time)
    
    def get_time(self):
        try:
            with open(self.alarms_file, 'r') as f:
                return f.read()
        except OSError as error:
            print("file not found, recreate alarm object.")


def check_args():
    if len(sys.argv) < 3:
        print("Too few args, must include server ip and port")
        exit(1)
    if sys.argv[1] == "-h":
        print("alarm_clock.py <server_ip>")
        exit(1)

def init_alarm(alarm):
    print("Starting up...\n")
    alarm.game.warm_up()
    pygame.mixer.music.play()
    print("Playing alarm sound")
    time.sleep(3)
    pygame.mixer.music.stop()
    random.seed(time.time())

def run_alarm():
    alarm = Alarm()
    init_alarm(alarm)

    while True:
        current_time = datetime.now().strftime("%H:%M")
        print(alarm.get_time())

        if current_time == alarm.get_time():
            time.sleep(3)
            alarm.status = True
            pygame.mixer.music.play(4)
            while alarm.status:
                if alarm.snooze.is_pressed:
                    pygame.mixer.music.stop()
                    time.sleep(5)
                    passed = alarm.game.start_game()
                    if passed:
                        alarm.status = False
                    else:
                        pygame.mixer.music.play(4)

        time.sleep(50)

def main():
    check_args()
    server_ip = sys.argv[1]
    server_port = sys.argv[2]
    
    t = threading.Thread(target=client.run, 
                        daemon=True, 
                        args=(server_ip, server_port)
                    )
    t.start()
    

if __name__ == "__main__":
    main()
