#Runs the wakeup game designed to stop the user from falling back asleep
#The user needs to press the button corresponding to the correct led once
#That led lights up to win only 3 misses allowed

import random
import time
from gpiozero import LED, Button


class Game:
    def __init__(self):
        #LEDs used in game
        self.led1 = LED(21)
        self.led2 = LED(20)
        self.led3 = LED(16)
        #Buttons corresponding to LEDs
        self.button1 = Button(13)
        self.button2 = Button(19)
        self.button3 = Button(26)


    def warm_up(self):
        #Tests if hardware is working properly
        self.led1.blink()
        self.led2.blink()
        self.led3.blink()
        time.sleep(5)
        self.led1.off()
        self.led2.off()
        self.led3.off()


    def start_game(self):
        random.seed()
        start_time = time.time()
        attempted = 0
        correct = 0

        while (time.time()-start_time) < 50:
            rand_led = int((random.random()*3)) + 1
            #print(str(rand_led))
            rand_interval = random.randint(1, 5)
            time.sleep(rand_interval)
            if rand_led == 1:
                self.led1.on()
                print("led1 on\n")
                attempted += 1
                led_start_time = time.time()
                while(time.time()-led_start_time) < 2:
                    if self.button1.is_pressed:
                        correct += 1
                        break
                self.led1.off()
            elif rand_led == 2:
                self.led2.on()
                print("led2 on\n")
                attempted += 1
                led_start_time = time.time()
                while (time.time()-led_start_time) < 2:
                    if self.button2.is_pressed:
                        correct += 1
                        break
                self.led2.off()
            elif rand_led == 3:
                self.led3.on()
                print("led3 on\n")
                attempted += 1
                led_start_time = time.time()
                while (time.time()-led_start_time) < 2:
                    if self.button3.is_pressed:
                        correct += 1
                        break
                self.led3.off()
        print(str(attempted-correct))
        if (attempted - correct) < 3:
            return True
        else:
            return False
