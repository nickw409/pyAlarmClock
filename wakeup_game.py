import random
import time
from gpiozero import LED, Button

def warmUp():
    led1 = LED(21)
    led2 = LED(20)
    led3 = LED(16)

    led1.blink()
    led2.blink()
    led3.blink()
    time.sleep(5)
    led1.off()
    led2.off()
    led3.off()

def start_game():
    random.seed()
    button3 = Button(26)
    button2 = Button(19)
    button1 = Button(13)
    led1 = LED(21)
    led2 = LED(20)
    led3 = LED(16)
    start_time = time.time()
    attempted = 0
    correct = 0

    while (time.time()-start_time) < 50:
        rand_led = int((random.random()*3)) + 1
        #print(str(rand_led))
        rand_interval = random.randint(1, 5)
        time.sleep(rand_interval)
        if rand_led == 1:
            led1.on()
            print("led1 on\n")
            attempted += 1
            led_start_time = time.time()
            while(time.time()-led_start_time) < 2:
                if button1.is_pressed:
                    correct += 1
                    break
            led1.off()
        if rand_led == 2:
            led2.on()
            print("led2 on\n")
            attempted += 1
            led_start_time = time.time()
            while (time.time()-led_start_time) < 2:
                if button2.is_pressed:
                    correct += 1
                    break
            led2.off()
        if rand_led == 3:
            led3.on()
            print("led3 on\n")
            attempted += 1
            led_start_time = time.time()
            while (time.time()-led_start_time) < 2:
                if button3.is_pressed:
                    correct += 1
                    break
            led3.off()
    print(str(attempted-correct))
    if (attempted-correct) < 3:
        return True
    else:
        return False
