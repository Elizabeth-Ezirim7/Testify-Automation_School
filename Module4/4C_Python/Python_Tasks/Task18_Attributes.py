""""
Create a class called Human
Add an attribute leg_count with the value of 4
Add another attribute can_walk with value of True

Optionally you can instantiate the class and prints out the leg_count and can_walk attributes"""



# Create a class called Human
# Add an attribute leg_count with the value of 4
class Human:
    leg_count = 4
    can_walk = True

    def __init__(self):
        self.leg_count = 4
        self.can_walk = True


# Optionally you can instantiate the class and prints out the leg_count and can_walk attributes
human_sample = Human()

print("Infor Output:" , human_sample.leg_count, " and ", human_sample.can_walk)







