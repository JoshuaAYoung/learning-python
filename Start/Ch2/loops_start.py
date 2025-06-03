# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
while x < 5:
  print(x)
  x = x + 1

answer = input("should I stop it?")
while answer != "yes":
  print(answer)
  answer = input("should I stop it?")

# define a for loop
# little different from JS, uses iterators
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# creating variable named day
for day in days:
  print(day)

# use a for loop over a collection


# use the break and continue statements
for day in days:
  if (day == "Wednesday"):
      break
  print(day)

# use the continue statement to skip an iteration
for day in days:
  if (day == "Wednesday"):
      continue
  print(day)

# using the enumerate() function to get an index and an item
# enumerate() returns a tuple of (index, item)
for i,day in enumerate(days):
   print(i, day)