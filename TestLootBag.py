import unittest
from lootbag import *

class TestBagOLoot(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.bag = LootBag()

	def test_add_toy_to_bag(self):
		self.isInstance(vincents_toys, list)
		self.assertIn('Ball', vincents_toys)

	def test_remove_toy_of_kid(self):
		self.assertIn('Vincent', self.bag.get_kids())
		self.bag.remove_toy_from_kid(toy, 'Vincent')
		vincents_toys = self.bag.list_toys_for_kid('Vincent')

		self.assertNotIn(toy, vincents_toys)

	def test_list_of_good_kids(self):
		good_kids = self.bag.get_good_kids()

		self.assertIsInstance(good_kids, list)
		self.assertIn()

	def test__toys_in_bag_for_specific_kid(self):
		vincents_toys = self.bag.list_toys_for_kid('Vincent')

		self.assertIsInstance(vincents_toys, list)
		self.assertIn('Slime', vincents_toys)

	def test_kid_toys_are_delivered(self):
		toy = 'Pony'
		self.bag.add_to_bag(toy, 'Vincent')
		vincent = self.bag.get_single_kid('Vincent')

		self.assertIsInstance(vincent, dict)
		
		self.bag.deliver_toys_to_kid('Vincent')
		self.assertTrue(vincent['delivered'])





