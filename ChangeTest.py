import unittest

from Change   import *

class ChangeTest(unittest.TestCase):
  def test_zero_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(0), {})

  def test_one_cent(self):
    change = Change()
    self.assertEqual(change.makeChange(1), {'p':1})

  def test_four_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(4), {'p':4})

  def test_five_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(5), {'n':1})

  def test_eight_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(8), {'n':1, 'p':3})

  def test_ten_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(10), {'d':1})

  def test_twenty_five_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(25), {'q':1})

  def test_forty_eight_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(48), {'q':1, 'd':2, 'p':3})

  def test_fifty_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(50), {'h':1})

  def test_seventy_four_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(74), {'h':1, 'd':2, 'p':4})

  def test_ninety_one_cents(self):
    change = Change()
    self.assertEqual(change.makeChange(91), {'h':1, 'q':1, 'd':1, 'n':1, 'p':1})

if __name__ == '__main__':
    unittest.main()