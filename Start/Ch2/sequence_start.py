# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[4])
print(mylist[-1])
mylist[0] = 10
print(mylist)

# add a list to another list
another_list = [6, 7, 8]
mylist = mylist + another_list
print(mylist)

mystring = "This is a string"
print(mystring[2])

# use slices to get parts of a sequence
print(mylist[1:4])
# third value is the skip amount (normally 1, can do every 2nd)
print(mylist[1:4:2])

# you can use slices to reverse a sequence
# leaving out the start and end, and using -1 as the step, reverses the list
print(mylist[::-1])

# Tuples are like lists, but they are immutable
# Tuples are faster in memory because they're immutable
mytuple = (0, 1, 2, "three")
print(mytuple[1])

# Sets are also sequences, but they contain unique values
# 2 only printed once because sets do not allow duplicates
# does not support indexing or slicing as they are unordered
myset = {1, 2, 3, 2, 5, "hey"}
print(myset)
# print(myset[2])  # this will cause an error

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(2 in myset)  # True
print(4 in myset)  # False
