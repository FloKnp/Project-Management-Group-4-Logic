import unittest
import se01_data_model


class TestDataModel(unittest.TestCase):


    def test_give_nouns(self):

        list1 = ['kläder', 'Kvinna']
        given = se01_data_model.give_noons(list1)
        intersection = list(set(list1) & set(given))
        self.assertFalse(intersection, "Intersection of list1 and given shoud be empty")

    def test_give_adjectives(self):
        list1 = ['gul']
        given = se01_data_model.give_adjectives(list1)
        intersection = list(set(list1) & set(given))
        self.assertFalse(intersection, "Intersection of list1 and given shoud be empty")


if __name__ == '__main__':
    unittest.main()
