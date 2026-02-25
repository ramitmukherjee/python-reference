
def fullName(fname="John", lname="Doe"):
    """
    return full name by joining fname and lname
    returns John Doe by default
    """
    return f"{fname} {lname}"

help(fullName)
# returns the documentation in triple quotes from the first line

print(fullName("Michael", "Jackson"))
# Michael Jackson

print(fullName())
# John Doe

# this function does nothing
def dummy():
    pass

print(dummy())
# None

# will create a tuple with the variables passed to it
def varArgFunc(*varArgs):
    print(varArgs)

varArgFunc()
# ()
varArgFunc('apple')
# ('apple',)
varArgFunc('apple', 'banana')
# ('apple', 'banana')

# this function creates a global variable
def badFunction():
    global globalVar
    globalVar = 10

# but we cannot access it outside without calling the function first
# print(globalVar)

badFunction()
# now we can use the global variable
print(globalVar)