def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Address", "Name", "Age")

def func(**kids):
  print("The youngest child is " + kids["lname"])
func(email="Emil", addr="Address", lname="Name", age="Age")

def fun(age='29'):
    print("my age is " + age)
fun('30')
fun()