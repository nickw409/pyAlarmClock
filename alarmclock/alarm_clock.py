#! /usr/bin/python3

import time
import os
from datetime import datetime
from sound_player import Player

class Alarm:
    def __init__(self, alarm_file):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.__alarms_file = os.path.join(script_dir, alarm_file)
        self.__player = Player()

        print("\nStarting up...\n")
        self.__player.play()
        print("Playing alarm sound")
        time.sleep(3)
        self.__player.stop()
        print("\nInitialization completed\n")

    def get_time(self):
        try:
            with open(self.__alarms_file, 'r') as f:
                return f.read()
        except OSError as error:
            print("file not found, recreate alarm object.")

    def run_alarm(self):
        print("Currently set alarm time: ", self.get_time().strip())
        while True:
            current_time = datetime.now().strftime("%H:%M").strip()

            if current_time == self.get_time().strip():
                print("Alarm ringing")
                time.sleep(3)
                self.__player.play()

            time.sleep(30)

    def set_time(self, time):
        #time is a string with format %HH:%MM
        with open(self.__alarms_file, 'w') as f:
            f.write(time)


def main():
    alarm = Alarm("alarm_times.txt")
    alarm.run_alarm()


if __name__ == "__main__":
    main()
