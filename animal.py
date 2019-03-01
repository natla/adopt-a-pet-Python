""" This module contains the Animal, Dog and Cat classes.
"""

# A list of dog breeds for testing purposes
# TODO: Take the list of dog breeds that are available in the adoption center from the database.
DOG_BREED = ["bulldog", "german shepherd", "labrador", "poodle",
             "goldren retriever", "chihuahua", "pug", "beagle",
             "dachshund", "yorkshire terrier", "bull terrier",
             "husky", "doberman", "rottweiler", "chow chow",
             "mastiff", "collie", "greyhound", "corgi",
             "dalmatian", "cocker spaniel", "unbred"]

# A list of cat breeds for testing purposes
# TODO: Take the list of cat breeds that are available in the adoption center from the database.
CAT_BREED = ["russian blue", "persian", "british shorthair",
             "munchkin", "siamese", "sphynx", "savannah",
             "ragamuffin", "ragdoll", "maine coon", "unbred"]

# A tuple of binary animal genders
GENDER = ("M", "F")


class Animal:
    """ Define the Animal super class"""

    def __init__(self, name, breed, age, gender):
        """ Initialize an instance of the Animal class

        :param name: the name of the animal
        :param breed: the breed of the animal
        :param age: the age of the animal
        :param gender: the gender of the animal
        """
        self.name = str(name)
        # Convert breed to lowercase in order to match the breed lists:
        self.breed = str(breed).lower()
        self.age = int(age)
        # Take only the first letter of the gender, capitalized:
        self.gender = str(gender).capitalize()[0]
        if self.gender not in GENDER:
            self.gender = 'Other'

    def __repr__(self):
        """ User-friendly description of the animal object. Can be invoked with str(object)."""
        if self.gender is not 'Other':
            return "{} named {} that is {} and a {}" \
                .format(self.breed.capitalize(),
                        self.name,
                        str(self.age) + " years old",
                        'boy' if self.gender == 'M' else 'girl')
        else:
            return "{} named {} that is {}" \
                .format(self.breed.capitalize(),
                        self.name,
                        str(self.age) + " years old")

    # This method is not being used yet in the adoption process but it adds pet personality.
    @staticmethod
    def eat(fav_food):
        """ What is the pet's favorite food?

        :param fav_food: my favorite food
        :return: I like to eat {fav_food}
        """
        return "I like to eat {}.".format(fav_food)


class Dog(Animal):
    """ Define the Dog child class. Inherits from Animal"""

    def __init__(self, name, breed, age, gender):
        """ Initialize attributes from the parent class Animal."""
        super().__init__(name, breed, age, gender)

        # Make sure that the breed of the dog is present in the list of available dog breed values.
        assert self.breed in DOG_BREED


class Cat(Animal):
    """ Define the Cat child class. Inherits from Animal"""

    def __init__(self, name, breed, age, gender):
        """ Initialize attributes from the parent class Animal."""
        super().__init__(name, breed, age, gender)

        # Make sure that the breed of the cat is present in the list of available cat breed values.
        assert self.breed in CAT_BREED
