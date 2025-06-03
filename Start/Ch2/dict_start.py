# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {
  "one" : 1,
  "two" : 2,
  3 : "three",
  4.5 : ["four", "point", "five"]
}
print(mydict)

# dictionaries are accessed via keys
print(mydict["one"])
mydict["one"] = "WON"
print(mydict)

# you can also set dictionary data by creating a new key


# Trying to access a nonexistent key will produce an error
# print(mydict["five"])

# To avoid this, you can use the "in" operator to see if a key exists
print("five" in mydict)  # Falsex

# You can retrieve all of the keys and values from a dictionary
print(mydict.keys())  # returns a list of keys
print(mydict.values())  # returns a list of values

# You can also iterate over all the items in a dictionary
for key, val in mydict.items():
  print(key, val)