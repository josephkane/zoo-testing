class Animal:

	def __init__(self):
		self.name = ''
		self.species = None

class Species:

	def __init__(self):
		self.common_name = ''
		self.geo_region = ''

class Habitat:

	def __init__(self):
		self.name = ''
		self.members = set()