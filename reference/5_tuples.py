
# tuples are ordered immutable lists in Python
tup1 = (10, 20, 30, "Hello")
print(tup1)

# we can concatenate tuples (comma is required for single element tuples)
tup2 =  tup1 + ("World",)
print(tup2)

# we can slice (slicing last two here)
print(tup2[-2:]) # ('Hello', 'World')

# length
print(len(tup2))

# tuple is immutable
# tup1[0] = 100 - error

# sorted
# sorted(tup1) - error since mixed type int and string
print(sorted((30, 20, 10)))
# [10, 20, 30] - This is a list not a tuple

# nested tuple
print((10, (15, 16) , 20, 30))
