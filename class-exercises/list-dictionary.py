'''
    Class Notes
    04/07/2022

    Lists and Dictionaries
'''

# List  - ordered and changeable
#  - List.append()
# Tuple - ordered and unchangeable

# LISTS
# Remove element at index i
# .pop(i)
# Remove element of value x
# .remove(x)
# Add an element to the end
# .append(x)
# Get a coppy of the list
# .copy()
# How many elements are equal to x
# .count(x)
# Print the index with value x
# .index(x)
# Sort the list
# .sort()
# Reverse the list
# .reverse()
# Remove all elements
# .clear()

# DICTIONARY
# key value structure
example_dict = {
    "class" : "ASTR 19",
    "prof"  : "Brant",
    "awesomeness" : 10
}
print(type(example_dict))

# get a vlue via a key
course = example_dict["class"]
print(course)

# change a value via key
example_dict["awesomeness"] += 1

# print the dictionary
print(example_dict)

# print dictionary element by element
for x in example_dict.keys():
    print(x, example_dict[x])