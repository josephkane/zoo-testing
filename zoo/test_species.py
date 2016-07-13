import unittest
from zoo import *

class TestSpecies(unittest.TestCase):

	def test_common_name_empty_string_by_default(self):
		species = Species()
		self.assertEqual(species.common_name, '')

	def test_georegion_empty_string_by_default(self):
		species = Species()
		self.assertEqual(species.geo_region, '')

if __name__ == '__main__':
	unittest.main()