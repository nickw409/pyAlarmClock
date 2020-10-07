import unittest
from alarm_clock import *
from datetime import datetime

class TestAlarmClock(unittest.TestCase):
    def test01_time(self):
        now = datetime.now.strftime("%H:%M")
        alarm = Alarm(time=datetime.now.strftime("%H:%M"))
        self.assertEqual(now, alarm.time)

if __name__ = "__main__":
    unittest.main()