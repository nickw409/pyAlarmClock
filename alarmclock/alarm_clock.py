#! /usr/bin/env python

import random, time, platform, sys, socket, os
from datetime import datetime
import wakeup_game as wakeup

if platform.system() == "Linux":
    from gpiozero import Button
    import pygame
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sounds/solid_snake_is_dummy_thicc.wav")
    print("Sound initialized")


class Alarm:
    def __init__(self, time="06:00"):
        self.snooze = Button(17)
        self.game = wakeup.Game()
        self.status = False
        self.alarms_file = "times.txt"
        set_time(time)

    def set_time(self, time):
        #time is a string with format %HH:%MM
        with open(self.alarms_file, 'w') as f:
            f.write(time)
    
    def get_time(self):
        try:
            with open(self.alarms_file) as f:
                return f.read()
        except OSError as error:
            print("file not found, recreate alarm object.")


def check_args():
    if len(sys.argv) < 2:
        print("Too few args, must include server ip")
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

        time.sleep(1)

def main():
    check_args()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
    server_ip = sys.argv[1]
    sock.connect((server_ip, 2550))
    new_time = sock.recv()
    

if __name__ == "__main__":
    main()
