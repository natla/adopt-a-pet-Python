""" This module provides tests for the Dog class and the adoption center methods
"""

import unittest
from adoption_center import AdoptionCenterFactory
from animal import Animal, Dog, Cat


class TestAdoptionService(unittest.TestCase):
    def setUp(self):
        """ Create animals for testing purposes.
            TODO - take the animals from a database instead
        """
        self.sharo = Dog('Sharo', 'unbred', 5, "male")
        self.lucy = Dog('Lucy', 'collie', 3, "Female")
        self.daisy = Dog('Daisy', 'labrador', 2, "fem")
        self.rocco = Dog('Rocco', 'German Shepherd', 1, "M")
        self.duke = Dog('Duke', 'Doberman', 4, "Male")
        self.mike = Dog('Mike', 'Doberman', 4, "Male")
        self.max_ = Dog('Max', 'greyhound', 7, "M")

        self.maya = Cat('Maya', 'Sphynx', 5, "F")
        self.ruh = Cat('Ruh', 'unbred', 3, "male")
        self.tiger = Cat('Tiger', 'SAVANNAH', 4, "M")

        # Create a non-animal object
        self.non_animal_object = (5, "F")

        # Create a Pool with dogs for adoption
        self.dog_pool = [self.sharo, self.lucy, self.daisy, self.rocco, self.duke, self.mike, self.max_]
        # Create a Pool with cats for adoption
        self.cat_pool = [self.maya, self.ruh, self.tiger]

    def test_class_instances(self):
        """Test the class of the set-up animal instances
        """
        self.assertIsInstance(self.sharo, Dog)
        self.assertNotIsInstance(self.lucy, Cat)
        self.assertIsInstance(self.maya, Cat)
        self.assertNotIsInstance(self.ruh, Dog)
        self.assertIsInstance(self.tiger, Animal)
        self.assertIsNot(self.non_animal_object, Animal)

    def test_animal_age(self):
        """ Test the age of the animal instances
        """
        self.assertEqual(self.sharo.age, 5)
        self.assertNotEqual(self.daisy.age, 512)

    def test_animal_breed(self):
        """ Test the breed of the animal instances
        """
        self.assertEqual(self.lucy.breed, 'collie')
        # Akita breed is not in the list of available breeds:
        with self.assertRaises(AssertionError):
            Dog('Mollie', 'Akita', 6, 'Male')

    def test_animal_gender(self):
        """ Test the gender of the animal instances
        """
        self.assertEqual(self.rocco.gender, 'M')
        self.assertEqual(Dog('Bobby', 'chow chow', 6, 'Unknown_gender').gender, 'Other')

    def test_eat_method(self):
        """ Test the eat method of the animal instances
        """
        self.assertEqual("I like to eat bones.", self.sharo.eat("bones"))
        self.assertEqual("I like to eat fish.", self.ruh.eat("fish"))
        self.assertEqual("I like to eat chicken soup.", self.tiger.eat("chicken soup"))

    def test_adoption_methods(self):
        """ Test the adoption methods of the Adoption Center Factory
        """
        dog_adoption_center = AdoptionCenterFactory(self.dog_pool)
        cat_adoption_center = AdoptionCenterFactory(self.cat_pool)

        # Adopt a dog that exists in the Pool
        message, result = dog_adoption_center.adopt_animal("doberman", 4, "M")
        self.assertIsInstance(result, Dog)
        # Assert that the adopted dog has been removed from the Dog pool:
        self.assertNotIn(result, self.dog_pool)
        # Assert that the user received a proper message and only Duke is returned:
        self.assertEqual("You adopted a Doberman named Duke that is 4 years old and a boy.", message)

        # Try to adopt a dog that doesn't exist in the Pool
        message, result_list = dog_adoption_center.adopt_animal("labrador", 3, "F")
        # Assert that the proper message has been returned
        self.assertIn("Sorry, we don't have this pet in our shop!"
                      " Would you consider adopting one of these cuties instead: ", message)
        self.assertIn("Daisy", str(result_list[0]))  # Daisy has same breed + gender
        self.assertIn("Lucy", str(result_list[1]))  # Lucy has same gender + age

        # Adopt a random cat from the Pool
        message, result = cat_adoption_center.get_lucky()
        self.assertIsInstance(result, Cat)
        # Assert that the lucky cat has been removed from the Cat pool
        self.assertNotIn(result, self.cat_pool)
        # Assert that the user received a proper message
        self.assertEqual("You adopted a {}."
                         .format(str(result)),
                         message)


if __name__ == '__main__':
    unittest.main()
