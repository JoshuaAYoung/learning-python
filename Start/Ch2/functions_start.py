# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def hello_func():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

hello_func()

# function that takes parameters
def hello_func_two(greeting):
  print("hello world!")
  name = input("What is your name? ")
  print(greeting, name)

hello_func_two("how are you doing,")

# function that returns a value
def cube(x):
  return x*x*x

result = cube(3)
print(result)

# function with default value for an parameter
def hello_func_three(greeting, name=None):
  print("hello world!")
  if name == None:
    name = input("What is your name? ")
  print(greeting, name)

hello_func_three("whassup,", "josh")
hello_func_three("thanks for telling me your name,")
hello_func_three(name="joshie", greeting="wordddd,")

# function with variable number of parameters
def multi_add(start, *args):
  result = start
  for x in args:
    result = result + x
  return result

print(multi_add(10, 1, 2, 3, 4, 5))
print(multi_add(10, 1, 2, 3))  
print(multi_add(10, 1, 2))  