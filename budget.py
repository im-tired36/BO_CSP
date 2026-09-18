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
saving = income* 0.10
spending_money = income - rent_mortgage - utilities - groceries - transportation - saving

print(f"The cost of your rent/mortgage is {rent_mortgage} and {rent_mortgage/income*100}")
print(f"The cost of your utilities is {utilities} and {utilities/income*100}% of your income")
print(f"The cost of your is {groceries} and {groceries/income*100}% of your income")
print(f"The cost of your is {transportation} and {transportation/income*100}% of your imcome")
print(f"you should save ${saving} and thats 10% of your income.")
print(f"${spending_money} is your spending money.")