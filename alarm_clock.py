#! /usr/bin/env python

import pygame,time,sys
import datetime
from gpiozero import Button
import wakeup_game as game
import random


pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
pygame.mixer.init()
random.seed(time.time())
#if (random.randint(0,2) == 1):
pygame.mixer.music.load("/home/pi/python_code/alarm_clock/alarm_sounds/solid_snake_is_dummy_thicc.wav")
#pygame.mixer.music.play(2)
#else:
    #pygame.mixer.music.load("/home/pi/python_code/alarm_clock/alarm_sounds/Thomas_The_Tank_Engine_Earrape.wav")
    #pygame.mixer.music.play(2)

button = Button(17)
f_output = ("/home/pi/python_code/alarm_clock/output.txt")

with open(f_output, 'a') as output_file:
    output_file.write("New Run:\n")

print("Starting up...\n")
game.warmUp()
pygame.mixer.music.play()
time.sleep(3)
pygame.mixer.music.stop()

reset_timer = 0

while True:
    current_time_struct = time.localtime()
    current_time = "{}:{}:{}".format(current_time_struct[3],
                                        current_time_struct[4],
                                        current_time_struct[5])

    print(current_time)
    alarm = False
    if current_time == "6:0:0":
        time.sleep(3)
        startTime = time.time()
        alarm = True
        pygame.mixer.music.play(4)
        with open(f_output, 'w') as f:
            f.write("New Day\n")
        while alarm:
            if button.is_pressed:
                pygame.mixer.music.stop()
                time.sleep(5)
                passed = game.start_game()
                if passed:
                    alarm = False
                else:
                    pygame.mixer.music.play(4)
            #elif (time.time() - startTime) > 40:
            #    print(time.time()-startTime)
            #    pygame.mixer.music.play(1)
            #    startTime = time.time()

    with open(f_output, 'a') as f:

        if current_time[-1:] == "0" or current_time[-2:] == "30":
            f.write(current_time + "\n")

    time.sleep(1)
