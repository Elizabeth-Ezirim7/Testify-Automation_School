""""
Declare a dictionary with any key-value pair of items/elements
Print the dictionary in console
Update the dictionary with two different key-value pair items
Print the dictionary in console again

Note: you can experiment with the other list functions too in the task"""

# Declare a dictionary with any key-value pair of items/elements

cohorts = {
    "cohortOne": "Elizabeth",
    "cohortTwo": "Olamide",
    "cohortThree": "Precious",
    "cohortFour":  "Ife",
    "cohortFive":  "Zainab",
    "cohortSix":  "Aridunnu",
    "cohortSeven":  "Chioma",
    "cohortEight":  "Mary",
    "cohortNine":  "Ebere",
}

# Print the dictionary in console
print(cohorts)

# Update the dictionary with two different key-value pair items
cohorts.update({"cohortTen": "Tim", "cohortEleven": "Comfort"})
print("Update:", cohorts)

# Other List Functions
# Keys
cohorts_keys = cohorts.keys()
print("Keys:", cohorts_keys)

# Values
cohorts_values = cohorts.values()
print("Values:", cohorts_values)

# popitem
cohorts.popitem()
print("Pop Item:", cohorts)

#copy
cohort_copy = cohorts.copy()
print(cohort_copy)

#clear
cohort_copy.clear()
print("Clear:", cohort_copy )

#Print the first original cohorts
print(cohorts)




