class Habitat:

	def __init__(self):
		self.name = ''
		self.members = set()

	def add_member(self, member):
		self.members.add(member)

	def remove_member(self, member):
		self.members.discard(member)

class Aquarium(Habitat):

	def __init__(self, water_type):
		Habitat.__init__(self)
		self.water_type = water_type
