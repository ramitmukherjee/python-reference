
print()

# range
print(f"range(3): {range(3)}")
# range(0, 3)

print("len(range(3)): {len(range(3))}")
# 3

print(f"list(range(3)): {list(range(3))}")
# [0, 1, 2]

print(f"list(range(5, 10)): {list(range(5, 10))}")
# [5, 6, 7, 8, 9] including i but not including j

print()
l1 = ["apple", "banana", "coconut"]
for i in range(len(l1)):
    print(l1[i])

print()
for fruit in l1:
    print(fruit)

print()
for i, fruit in enumerate(l1):
    print(f"{i} - {fruit}")

print()
count = 3
while count > -1:
    print(count)
    count -= 1

