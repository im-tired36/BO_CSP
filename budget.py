#BO 6th, Your Budget


while True:
    try:
        income = int(input("What is the cost of your monthly income?"))
        break
    except:
        print("That isn't a number.")

while True:
    try:
        rent_mortgage = int(input("What is the cost of your monthly rent/mortgage?"))
        break
    except:
        print("That isn't a number.")

while True:
    try:
        utilities = int(input("What is the cost of your monthly utilities?"))
        break
    except:
        print("That isn't a number.")

while True:
    try:
        groceries= int(input("What is the cost of your monthly groceries?"))
        break
    except:
        print("That isn't a number.")

while True:
    try:
        transportation = int(input("What is the cost of your monthly transportation?"))
        break
    except:
        print("That isn't a number.")

print(f"The cost of your rent/mortgage is {rent_mortgage} and {rent_mortgage/income*100,2}")
print()
print()
print()
print()
