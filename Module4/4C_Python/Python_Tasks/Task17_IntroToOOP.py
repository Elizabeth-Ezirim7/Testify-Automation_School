""""
Create a class called Human
Initialize the class"""


# class
class Human:
    name = "Elizabeth"
    sex = "Female"

    def get_name_sex(self):
        return self.name + ":" + self.sex


# Object initialization
human = Human()

#print attributes and method
print(human.name, human.sex, human.get_name_sex())

# just the method
print(human.get_name_sex())

