
# question 1
def login():
  username = input ("Enter the username ")
  password = input ("Enter the password ")
  confirm_password = input ("Enter the confirm password ")
  if(password == confirm_password ):
    print("Login Successful")
  else:
    print("Login Failed")
login()

#question 2

num = int(input ("Enter the num "))
if (num % 2) == 0:
    print("The number is even ")
else:
    print("The number is odd")

#question 3

fruits=["avacodo","burdekin plum","Calabash Fruit","Damson","Emblica","Feijoa"]
FRUIT = [x for x in fruits if "a" in x]
GOODTASTE = [x for x in fruits  if "o" in x]
JUICY = [x for x in fruits  if "m" in x]
HEALTHY = [x for x in fruits  if "i" in x]
print(FRUIT)
print(GOODTASTE)
print(JUICY)
print(HEALTHY)
