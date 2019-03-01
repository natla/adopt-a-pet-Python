""" This module contains the adoption center methods.
"""

import random


class AdoptionCenterFactory:
    """ Adoption Center Factory that provides the user
    with a desired animal from the Pool
    or a random animal that just got lucky.
    """

    def __init__(self, adoption_pool):
        self.adoption_pool = adoption_pool

    def adopt_animal(self, breed, age, gender):
        """ Adopt any desired animal by breed, age and gender.

        :param breed: The desired breed of the animal.
        :param age: The desired age of the animal.
        :param gender: The desired gender of the animal.
        :return: A tuple of a suitable message and an animal object with the desired attributes OR
                 A tuple of a suitable message and a list of additional animals
                 if the desired animal is not in the Pool.
                 The additional list of animals is ordered by (breed > age > gender)
        """
        lucky_animal_list = [animal for animal in self.adoption_pool
                             if animal.breed == breed and animal.age == age and animal.gender == gender]
        if len(lucky_animal_list) > 0:
            # Return only one animal to not confuse the user with too many options:
            lucky_animal = lucky_animal_list[0]
            message = "You adopted a {}.".format(str(lucky_animal))
            # Remove the animal from the pool once it has been adopted:
            self.adoption_pool.remove(lucky_animal)
            return message, lucky_animal

        # If no such animal exists in the Pool,
        # propose an additional list of animals filtered and ordered by: breed > gender > age
        breed_list = list(filter(lambda x: x.breed == breed, self.adoption_pool))
        gender_list = list(filter(lambda x: x.gender == gender, self.adoption_pool))
        age_list = list(filter(lambda x: x.age == age, self.adoption_pool))
        # Remove the duplicates from the final list:
        additional_possibilities = list(dict.fromkeys(breed_list + gender_list + age_list))

        message = "Sorry, we don't have this pet in our shop!" \
                  " Would you consider adopting one of these cuties instead: {}." \
            .format(additional_possibilities)
        return message, additional_possibilities

    def get_lucky(self):
        """ Get a random animal from the shop.
        :return: An animal object with random breed, age and gender.
        """
        lucky_animal = random.choice(self.adoption_pool)  # or random.randint(the index of the animal from the pool)
        message = "You adopted a {}.".format(str(lucky_animal))
        # Remove the animal from the pool once it has been adopted
        self.adoption_pool.remove(lucky_animal)
        return message, lucky_animal
