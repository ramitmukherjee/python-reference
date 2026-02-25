

# dictionaries contain key and value pairs
# keys are immutable (can be tuples) and unique
# values are mutable and can have duplication
d1 = {'ramit': 'active', 'apurva': 'inactive'}
print(d1)

# copy
d1.copy()

# delete an element
del(d1['apurva'])
print(d1)
# {'ramit': 'active'}

# add an element
d1["dwipa"] = 'active'
print(d1)
# {'ramit': 'active', 'dwipa': 'active'}

# contains
print('ramit' in d1) # True
print('apurva' not in d1) # True

# keys returns an iterable (not list) of all keys
print(d1.keys())
# dict_keys(['ramit', 'dwipa'])
# if we want it as list we need to use list constructor
print(list(d1))

# values returns an iterable of all values
print(d1.values())
# dict_values(['active', 'active'])

# get iterator over the keys
# same as iter(d1.keys())
print(iter(d1))

# error is thrown when trying to get a non existing key
# print(d1['apurva'])
print(d1.get('apurva'))
# get is a safer version which returns None instead of error
print(d1.get('apurva', 'inactive'))
# will return inactive if key is not found
print(d1)

# clears the dict
d1.clear()
print(d1)
# {}


