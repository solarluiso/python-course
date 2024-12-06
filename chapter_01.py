# 1. VARIABLES

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4
x = "Sally"
print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# valid variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print(myVariableName)
print(MyVariableName)
print(my_variable_name)


# 2. DATA TYPES

# number 
123456

# string
"my name is luiso"
'this also works'

# list / array
["eggs", "beans", "bananas", 4, []]

print(7)

# object / dictionary
{
  "name": "luiso",
  "age": 33
}

def jello():
    print('jello')

person = {
    # "name": "james",
    "age": 28,
    "action": jello
}

# boolean - truthy falsey
True
False

# None - absence of information
None


# A data type is a type of data that is friendly to python