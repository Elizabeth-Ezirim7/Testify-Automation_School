""""

Declare a list with any value and number of item/element
Print the list in console
Sort the list
Print the list in console again

Note: you can experiment with the other list functions too in the task."""

# Declare a list with any value and number of item/element
vegetables = ["Kale", "Spinach", "Carrot", "Brocolli", "Tomatoes", "Cayenne", "Fern"]

# Print the list in console
print(vegetables)

# Sort the list
vegetables.sort()

# Print the list in console again
print("sort-asc:", vegetables)


# Other List functions
#len
length = len(vegetables)
print(length)

# reverse
before_reverse = vegetables
after_reverse = vegetables.reverse()
print(before_reverse, after_reverse)

# extend
vegetables.extend(["Lettuce", "Zucchini", "Cauliflower", "Celery", "Asparagus"])
print(vegetables)

# pop
vegetables.pop()
print(vegetables)

#count
count_celery = vegetables.count("Celery")
# print(vegetables)
print(count_celery)






