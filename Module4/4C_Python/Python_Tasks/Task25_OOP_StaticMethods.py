""""
Create a class called Utilities
Create a static method called print_name which accepts a parameter, and prints out the parameter.
Invoke the static method print_name()

You can use any of the two methods to create your static methods.
"""


class Utilities:
    @staticmethod
    def print_name(name):
        print(name)


# Invoke
Utilities.print_name("Elizabeth")



# print(Utilities.print_name("Elizabeth"))  
# tester = Utilities
# tester.print_name("Elizabeth")
# print("QA Engineer is :",tester.print_name("Elizabeth"))

# print("Testers Name:", Utilities.print_name("Elizabeth"))
