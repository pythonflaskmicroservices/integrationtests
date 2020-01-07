from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase): 
    def test_create_item(self):
        item = ItemModel('test',19.99)
        self.assertEqual(item.name, 'test',
			"The name of item after creation does not equal the constructor arguement.")
	self.assertEqual(item.price, 19.99,
			"The price of item is wrong")


    def test_item_json(self):
        item = ItemModel('test',19.99)
	expected = {
            'name': 'test',
            'price': 19.99
	}
        self.assetEqual(item.json(), expected,
			"The json export is not correct.")
