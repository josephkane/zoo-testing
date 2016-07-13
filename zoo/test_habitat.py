import unittest
from zoo import *

class TestHabitat(unittest.TestCase):

	def test_name_empty_string_by_default(self):
		habitat = Habitat()
		self.assertEqual(habitat.name, '')

	def test_members_empty_set_by_default(self):
		habitat = Habitat()
		self.assertIsInstance(habitat.members, set)

	def test_add_animal_to_habitat(self):
		aquarium = Aquarium('freshwater')
		bob = Betta('orange', 'Bob')
		james = Betta('orange', 'James')
		aquarium.add_member(bob)
		self.assertIn(bob, aquarium.members)

		aquarium.add_member(james)
		self.assertIn(bob, aquarium.members)
		self.assertIn(james, aquarium.members)

	def test_remove_members(self):
		aquarium = Aquarium('freshwater')
		james = Betta('orange', 'James')
		aquarium.add_member(james)
		aquarium.remove_member(james)

		self.assertNotIn(james, aquarium.members)

if __name__ == '__main__':
	unittest.main()