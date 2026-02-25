# sets contain only unique items. set is unordered

s1 = {"apple", "orange", "beer", "beer"}
print(s1)
# duplicate is removed {'orange', 'apple', 'beer'}

# converting a list into a set
s2 = set(["apple", "banana", "lion", "lion"])
print(s2)
# {'banana', 'apple', 'lion'}

# adding an item
s1.add("pony")
print(s1)
# {'beer', 'orange', 'apple', 'pony'}

# same item cannot be added again
s1.add("apple")
print(s1)
# {'beer', 'orange', 'apple', 'pony'}

# removing an item
s1.remove("pony")
print(s1)
# {'beer', 'orange', 'apple'}

# will error out if item is not found for removal
# s1.remove("pony")

# set will have "in" "not in" to check if item is present

# intersection same as s1.intersection(s2)

print(s1 & s2)
# {'apple'}

# union - same as print(s1.union(s2))
print(s1 | s2)
# {'apple', 'banana', 'lion', 'orange', 'beer'}

# other methods
print(s1.issubset(s2)) # False
print(s1.isdisjoint(s2)) # False
print(s1.difference(s2)) # {'orange', 'beer'}