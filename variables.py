#https://www.w3schools.com/python/python_variables_multiple.asp


# Python allows you to assign values to multiple variables in one line:
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# #  And you can assign the same value to multiple variables in one line:
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


#  if you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# # print(x)
# # print(y)
# # print(z)
# print(x,y,z)
# fruits.append('peach')
# print(fruits)


# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types

x = 5
y = "John"
# print(x, y,'tomorrow')



# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

def myfunc():
    print(y + " loves python")



x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
