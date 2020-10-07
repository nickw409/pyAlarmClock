import unittest
from alarm_clock import *
from datetime import datetime

class TestAlarmClock(unittest.TestCase):
    def test01_time(self):
        now = datetime.now().strftime("%H:%M")
        alarm = Alarm(time=datetime.now().strftime("%H:%M"))
        print("Now: {}\nAlarm Time: {}\n".format(now, alarm.time))
        self.assertEqual(now, alarm.time)

if __name__ == "__main__":
    unittest.main()
