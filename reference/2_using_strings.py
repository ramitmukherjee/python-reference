import re # regex

print("""
-------------
Using Strings
-------------
""")

# creating an immutable string
x = "banana"

print(x.upper()) # BANANA
print(x.replace('b', 'sh')) # shanana
print(x.find('nana')) # 2 or -1 if not found
print("a, b, c".split(', ')) # ['a', 'b', 'c']

# strings are arrays
print(f"x = {x}") # b
print(f"x[0] = {x[0]}") # b

# iterating a string
y = ""
for i in x:
    y += i
print(f"y = {y}")

# length
print(f"len(x) = {len(x)}") # 6

# test contains f strings and escape
test = "nana" in x
print(f"\"nana\" in x = {test}") # True

# get every second character
print(f"x[::2] = {x[::2]}")

# multiply strings only with integers
print(f"x * x = {x * 2}") # bananabanana

# raw strings
print(r"C:\new\file.txt") # \ is no longer special

wordMatcher = re.compile(r"\w{2}", re.IGNORECASE)
m = wordMatcher.match(x)
print(m.start()) # 0
print(m.group()) # ba
print(m.span()) # 0, 2

