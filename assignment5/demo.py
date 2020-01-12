# This is a class of Persons
class Person:  

  # This is function greeting
  def greeting():
    print("Hello")

  # This is function check_age
  def check_age():
    if self.age < 18:
      print("You will get 50 percent discount")

    elif self.age > 18:
      print("You will get 20 percent discount")


# a simple for loop
for x in range(5):
  print(x)


# a simple while loop
count = 0
while count < 5:
  print(count)
  count += 1  # This is the same as count = count + 1

# a simple try except example
try:
  print(a)
except:
  print("An exception occurred")