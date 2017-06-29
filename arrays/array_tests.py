import unittest
import random

class TestDutchFlagPartition(unittest.TestCase):
    def setUp(self):
        self.a = range(0,10)
        random.shuffle(self.a)
        self.i = random.randint(0,9)

    def test_less_than_pivot(self):
        left = dutch_flag_partition(self.a)[:self.i]
        less_than = map(lambda x: x < self.a[self.i], left)
        self.assertTrue(all(less_than))

    def test_greater_than_pivot(self):
        right = dutch_flag_partition(self.a)[self.i + 1:]
        greater_than = map(lambda x: x >= self.a[self.i], right)
        self.assertTrue(all(greater_than))

if __name__ == '__main__':
    unittest.main()
