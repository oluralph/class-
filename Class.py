class Bear:
    def __init__(self, animal_name, age, how_many_dozens):
        self.name = animal_name
        self.age = age
        self.dozens = how_many_dozens
    
    def calculate_all_animal(self):
        return self.dozens * 12
    
    