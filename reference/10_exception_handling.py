myFile = None
try:
    myFile = open("filename", "r")
except IOError:
    print("IOError occured")
except:
    print("generic error occured")
finally:
    if myFile is not None:
        myFile.close()

# IOError occured

try:
    1/0
except ZeroDivisionError as e:
    print("Cannot divide by zero.")

# Cannot divide by zero

try:
    x = 100
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("no error occured")

# no error occured