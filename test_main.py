import unittest
import main

class TestMain(unittest.TestCase):
  def test_date1(self):
    result = main.verifyDate()
    self.assertEqual(result, "5/32/2014 is an invalid date")

  def test_date2(self):
    result = main.verifyDate()
    self.assertEqual(result, "2/29/1936 is a valid date")

  def test_date3(self):
    result = main.verifyDate()
    self.assertEqual(result, "11/31/1873 is an invalid date")

if __name__ == "__main__":
  unittest.main()