import unittest
import zoo

class TestAnimal(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		pass

	def test_name_empty_string_by_default(self):
		a_animal = zoo.Animal()
		self.assertEqual(a_animal.name, '')

	def test_species_none_by_default(self):
		a_animal = zoo.Animal()
		self.assertEqual(a_animal.species, None)

class TestSpecies(unittest.TestCase):

	def test_common_name_empty_string_by_default(self):
		species = zoo.Species()
		self.assertEqual(species.common_name, '')

	def test_georegion_empty_string_by_default(self):
		species = zoo.Species()
		self.assertEqual(species.geo_region, '')

class TestHabitat(unittest.TestCase):

	def test_name_empty_string_by_default(self):
		habitat = zoo.Habitat()
		self.assertEqual(habitat.name, '')

	def test_members_empty_set_by_default(self):
		habitat = zoo.Habitat()
		self.assertIsInstance(habitat.members, set)

if __name__ == '__main__':
	unittest.main()