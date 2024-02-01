"""

Create a function that prints out "Hello World"
Invoke the same function in it own body
Invoke the function outside the function block

Take note of the function invoke and put the Python whitespace rule in mind
"""


"""def greet():
    print('Hello World')
    # Invoke the same function in it own body
    greet()

# Invoke the function outside the function block
greet()"""


def salute(counter):
    # Base case: stop recursion when counter reaches 0
    if counter == 0:
        return

    print("Hello World")

    # Invoke the function within its own body with a decremented counter
    salute(counter - 1)


# Invoke the function with an initial counter value
salute(3)



