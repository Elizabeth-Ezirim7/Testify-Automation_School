""""

Declare a global variable with name as language and the value as "Python"
Create a function, in the function declare a variable with name as language and value as "Java", then print out the variable in the function
Print out the variable name into the console
Invoke the function"""

# Declare a global variable with name as language and the value as "Python
language = "Python"


# Create a function, in the function declare a variable with name as language and value as "Java", then print out the
# variable in the function
def insideScope():
    language = "Java"
    print(language)


# Print out the variable name into the console
print(language)

# Invoke the function
insideScope()
