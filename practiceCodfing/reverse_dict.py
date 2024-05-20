# Create a dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Use reversed() on the keys view and convert it to a list
reversed_keys = list(reversed(list(dict1.keys())))
print("Reversed keys: ", reversed_keys)

# Use reversed() on the values view and convert it to a list
reversed_values = list(reversed(list(dict1.values())))
print("Reversed values: ", reversed_values)

# Use reversed() on the items view and convert it to a list
reversed_items = list(reversed(list(dict1.items())))
print("Reversed items: ", reversed_items)
