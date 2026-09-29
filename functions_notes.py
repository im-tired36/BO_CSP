#BO, 6th, functions notes

#functions
#round()
#len()
#print()
def stupid_proof(money):
    while True:
        try:
            temp = float(input(f"What is your monthly {money}"))
            return temp
        except:
            print("That is not a number")

#variables go first
"""income = float(input("what is your monthy income:"))
rent = float(input("what is your monthy rent:"))
utilities = float(input("what is your monthy utilities:"))
transportation = float(input("what is your monthy transportation:"))
groceries = float(input("what is your monthy groceries:"))
save = round(income*.1,2)
"""
#variables turn into this because of def stupid_proof
income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
transportation = stupid_proof("transportation")
groceries = stupid_proof("groceries")
save = round(income*.1,2)
#functions go second
def calc_percent(bill, income):
    return round(bill/income * 100)
print(f"Your rent is ${rent} which is {calc_percent(rent, income)}% of your income")
print(f"Your utilites is ${utilities} which is {calc_percent(utilities, income)}% of your income")
print(f"Your transportation is ${transportation} which is {calc_percent(transportation, income)}% of your income")
print(f"Your groceries is ${groceries} which is {calc_percent(groceries, income)}% of your income")
print(f"You should save ${income*.1} which is 10% of your income.")
print(f"That means you have ${income-rent-utilities-transportation-groceries-save} left to save.")