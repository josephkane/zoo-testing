import unittest
import zoo

class TestAnimal(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		pass

	def test_animal_creation(self):
		bob = zoo.Betta('orange', 'Bob')
		self.assertEqual(bob.name, 'Bob')
		self.assertEqual(bob.species.color, 'orange')
		self.assertIsInstance(bob, zoo.Animal)
		self.assertIsInstance(bob, zoo.Swimming)
		self.assertIsInstance(bob.species, zoo.Species)
		self.assertIsInstance(bob.species, zoo.BettaTrifasciata)

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

	def test_add_animal_to_habitat(self):
		aquarium = zoo.Aquarium('freshwater')
		bob = zoo.Betta('orange', 'Bob')
		james = zoo.Betta('orange', 'James')
		aquarium.add_member(bob)
		self.assertIn(bob, aquarium.members)

		aquarium.add_member(james)
		self.assertIn(bob, aquarium.members)
		self.assertIn(james, aquarium.members)

	def test_remove_members(self):
		aquarium = zoo.Aquarium('freshwater')
		james = zoo.Betta('orange', 'James')
		aquarium.add_member(james)
		aquarium.remove_member(james)

		self.assertNotIn(james, aquarium.members)

class TestWalking(unittest.TestCase):

	def test_legs_zero_by_default(self):
		walking = zoo.Walking()
		self.assertEqual(walking.legs, 0)

	def test_walk_speed_zero_by_default(self):
		walking = zoo.Walking()
		self.assertEqual(walking.walk_speed, 0)

class TestSwimming(unittest.TestCase):

	def test_appendages_false_by_default(self):
		swimming = zoo.Swimming()
		self.assertFalse(swimming.fins)
		self.assertFalse(swimming.flippers)
		self.assertFalse(swimming.web_feet)

	def test_swim_speed_zero_by_default(self):
		swimming = zoo.Swimming()
		self.assertEqual(swimming.swim_speed, 0)

class TestFlying(unittest.TestCase):

	def test_wings_zero_by_default(self):
		flying = zoo.Flying()
		self.assertFalse(flying.wings, 0)

	def test_wingspan_zero_by_default(self):
		flying = zoo.Flying()
		self.assertFalse(flying.wingspan, 0)

	def test_air_speed_zero_by_default(self):
		flying = zoo.Flying()
		self.assertEqual(flying.air_speed, 0)


if __name__ == '__main__':
	unittest.main()