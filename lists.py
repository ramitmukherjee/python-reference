

print("""
-----------------------------
Working with lists in Python:
-----------------------------
""")

# defining a list
print('\nlist = [1, 2, 3]')
list = [1, 2, 3]
print(list)

# checking its type
print('\ntype(list)')
list = [1, 2, 3]
print(type(list)) # <class 'list'>

# inserting
print('\nlist.append(4)')
list.append(4)
print(list) # 1, 2, 3, 4

# replacing
print('\nlist[0:2] = [0, 1]')
list[0:2] = [0, 1]
print(list) # 0, 1, 3, 4

# splicing
print('\nlist[2:2] = [2]')
list[2:2] = [2]
print(list) # 0, 1, 2, 3, 4

print('\nlist[0:0] = [-2, -1]')
list[0:0] = [-2, -1]
print(list) # -2, -1, 0, 1, 2, 3, 4