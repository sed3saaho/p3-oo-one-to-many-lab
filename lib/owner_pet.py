class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def pets(self):
        return self.pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self.pets.append(pet)
            pet.owner = self
        else:
            raise Exception("Pet must be an instance of the Pet class")

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Invalid pet type")
        self.owner = owner
        Pet.all.append(self)

    def __str__(self):
        return f"{self.name} ({self.pet_type})"