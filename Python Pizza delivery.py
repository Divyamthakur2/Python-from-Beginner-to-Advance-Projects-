print("Welcome to the Python Pizza Delivery!")
size = input("Enter the size of the pizza L, M or S: ")
Pepperoni = input("Do you want the pepperoni? Y or N: ")
extra_cheese = input("Do you want the extra cheese? Y or N: ")
bill = 0
if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15
#pepperoni cost
if Pepperoni == "Y":
    if size == "S":
     bill +=2
    else:
     bill+=3
#extra cheese
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: £ {bill}")






