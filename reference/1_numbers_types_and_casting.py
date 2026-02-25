print(type(10))
# <class 'int'>
print(type(6//2)) # integer division discards remainder
# <class 'int'>
print(type(100%51)) # remainder
# <class 'int'>
print(type(2 ** 2)) # power like x^y
# <class 'int'>

print(type(10.5))
# <class 'float'>
print(type(6/2))
# <class 'float'>
print(type(5e2)) # 10 exponent ans - 500.0
# <class 'float'>

print(type("10"))
# <class 'str'>

print(type(True))
# <class 'bool'>

print(type(1 + 10j))
# <class 'complex'>

print(type(['a', 'b', 'c']))
# <class 'list'>

print(type(('a', 'b', 'c')))
# <class 'tuple'>

print(type({'id': 1, 'name': 'john'}))
# <class 'dict'>

# print(int('A'))
# Error

print(int(1.6))
# 1
print(int(False))
# 0

print(int('100'))
# 100

print(bool(1))
# True

# Integers
a = 1
b = 35656222554887711
c = -3255522


# Floats
x = 1.10
y = 1.0
z = -35.59
p = 1e2 # 1 * 10^2

# Complex

i = 3+5j
j = 5j
k = -5j

print(i + j) # (3+10j)

# Converting types (casting)

#convert from string to complex:
t = complex("100j") # 0 + 100j

#convert from int to float:
u = float(a) # 1.0

#convert from float to int:
v = int(z) # -35

#convert from float to complex:
w = complex(x) # (1.1+0j)
