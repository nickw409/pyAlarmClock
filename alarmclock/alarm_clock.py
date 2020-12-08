#! /usr/bin/python3

import random, time, platform, sys, os, threading
from datetime import datetime
#import wakeup_game as wakeup
import client

if platform.system() == "Linux":
    from gpiozero import Button
    import pygame
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
    pygame.mixer.init()
    sound_file = "solid_snake_is_dummy_thicc.wav"
    script_dir = os.path.dirname(os.path.realpath(__file__))
    project_dir, script_dir = os.path.split(script_dir)
    sound_dir = os.path.join(project_dir, "alarm_sounds",)
    pygame.mixer.music.load(os.path.join(sound_dir, sound_file))
    print("Sound initialized")


class Alarm:
    def __init__(self):
        #self.snooze = Button(17)
        #self.game = wakeup.Game()
        self.status = False
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.alarms_file = os.path.join(script_dir, "alarm_times.txt")


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
    if len(sys.argv) < 2:
        print("Too few args, must include server ip")
        exit(1)
    if sys.argv[1] == "-h":
        print("alarm_clock.py <server_ip>")
        exit(1)

def init_alarm(alarm):
    print("Starting up...\n")
    #alarm.game.warm_up()
    pygame.mixer.music.play()
    print("Playing alarm sound")
    time.sleep(3)
    pygame.mixer.music.stop()
    random.seed(time.time())

def run_alarm():
    alarm = Alarm()
    init_alarm(alarm)
    #print("run alarm")
    alarm_time = alarm.get_time().strip()
    print("Currently set alarm time: ", alarm_time)
    while True:
        current_time = datetime.now().strftime("%H:%M").strip()
        alarm_time = alarm.get_time().strip()
        #print(current_time)
        #print(alarm_time)
        #print((current_time == alarm_time))

        if current_time == alarm_time:
            print("Alarm ringing")
            time.sleep(3)
            #alarm.status = True
            pygame.mixer.music.play(4)
            while alarm.status:
                if alarm.snooze.is_pressed:
                    pygame.mixer.music.stop()
                    time.sleep(5)
                    #passed = alarm.game.start_game()
                    if passed:
                        alarm.status = False
                    else:
                        pygame.mixer.music.play(4)

        time.sleep(30)

def main():
    check_args()
    server_ip = sys.argv[1]
    print("main")
    threading.Thread(target=client.run, 
                        daemon=True, 
                        args=(server_ip,)
                     ).start()
    
    run_alarm()
    

if __name__ == "__main__":
    main()
