

print("""
---------------------
Working with objects:
---------------------
""")
# defining a dictionary
print("{'ramit': 'active', 'apurva': 'inactive'}")
users = {'ramit': 'active', 'apurva': 'inactive'}
print(users)

# copy
print('\nusers.copy()')
print(users.copy())

# items
print("\niterating a dictionary \n")
print('iterating using simple for in:')
for key in users.copy():
    print(key + '->' + users[key])

print('\niterating using tuple:')
for (key, value) in users.copy().items():
    print(key + '->' + value)