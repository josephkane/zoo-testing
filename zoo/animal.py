from species import *
from transport import *

class Animal:

	def __init__(self, name, species):
		self.name = name
		self.species = species

class Betta(Animal, Swimming):

	def __init__(self, color, name):
		super().__init__(name, BettaTrifasciata(color))
