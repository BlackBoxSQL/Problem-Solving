import unittest
from circle import circleArea
from math import pi

class TestCircleArea(unittest.TestCase):
	def test_area(self):
		self.assertAlmostEqual(circleArea(1), pi)