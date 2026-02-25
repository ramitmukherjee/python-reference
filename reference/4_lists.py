
# Lists are ordered mutable collections

# defining a list
l1 = [3, 2, 1]
print(l1)
# [3, 2, 1]

# reverse the list
l1.reverse()
print(l1)
# [1, 2, 3]

# we can splice lists
l1[1:1] = [100]
print(l1)
# [1, 100, 2, 3]

# we can concatenate lists
print(l1 + [200, 300])
# [1, 100, 2, 3, 200, 300]

# we can mutate a list by extending it this will append each element of the argument list to the original list
# same as l1 + [200, 300]
l1.extend([200, 300])
print(l1)
# now l1 is updated to [1, 100, 2, 3, 200, 300]

# if we want to add a single item we can use append. the argument will not be spread here
l1.append([400, 500])
print(l1)
# now l1 is updated to [1, 100, 2, 3, 200, 300, [400, 500]]

# deleting an element. here we are deleting the last element
print('\nDeleting: ')
del(l1[-1])
print(l1)
# [1, 100, 2, 3, 200, 300]
del(l1[2])
print(l1)
# [1, 100, 3, 200, 300]

# update every second item from index 0 (will be returned) to 4 (not inclusive)
print('\nSlice and update: ')
l1[0:4:2] = [8, 9]
print(l1)
# [8, 100, 9, 200, 300] will be changed to [8, 100, 9, 3, 200, 300]

# get every second item from index 0 (will be returned) to 4 (not inclusive)
print('\nSlice: ')
print(l1[0:4:2])
# [8, 9]

# pop ith item (argument optional -1 (last element) by default)
print('\nPop: ')
print(l1.pop(0))
# 8
print(l1)
# [100, 9, 200, 300]

# removes an element (will error out if element not found)
print('\nRemove 200: ')
l1.remove(200)
print(l1)
# [100, 9, 3, 300]

# copy list
l3 = l1
l2 = l1.copy()

# clear list
print('\nClear: ')
l1.clear()
print(l1)
# []
# l3 also got cleared since referring to same object
print(l3)
# []

# l2 still has values
print(l2)