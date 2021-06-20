import unittest

from algo.min_conf_rooms import min_meeting_rooms_needed

class MinConfRoomsTest(unittest.TestCase):
    def test_1(self):
        intervals = [[0,30],[5,10],[15,20]]
        self.assertEqual(min_meeting_rooms_needed(intervals), 2)
        
    def test_2(self):
        intervals = [[7,10],[2,4]]
        self.assertEqual(min_meeting_rooms_needed(intervals), 1)
        
    def test_3(self):
        intervals = [[13,15],[1,13]]
        self.assertEqual(min_meeting_rooms_needed(intervals), 1)