#! /usr/bin/env python

import random, time, platform
from datetime import datetime
import wakeup_game as wakeup

if platform.system() == "Linux":
    import pygame
    from gpiozero import Button




class Alarm:
    def __init__(self, time="06:00"):
        self.snooze = Button(17)
        self.game = wakeup.Game()
        self.time = time
        self.status = False

    def set_time(self, time):
        #time is a string with format %HH:%MM
        self.time = time

def init_sound():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/python_code/alarm_clock/alarm_sounds/solid_snake_is_dummy_thicc.wav")

def init_alarm(alarm):
    print("Starting up...\n")
    alarm.game.warm_up()
    pygame.mixer.music.play()
    time.sleep(3)
    pygame.mixer.music.stop()
    random.seed(time.time())

def main():
    alarm = Alarm()
    init_sound()
    init_alarm(alarm)

    while True:
        current_time = datetime.now.strftime("%H:%M")
        print(current_time)

        if current_time == alarm.time:
            time.sleep(3)
            startTime = time.time()
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

if __name__ == "__main__":
    main()