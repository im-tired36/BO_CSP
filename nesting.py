#BO, 6th, nesting notes

csp = ["bliss", "caleb", "ainsley", "dara"]
if len(csp) > 0:
    for student in csp:
        print(f"checking in {student}")
else:
    print("There is no one in class.")

while True:
    username = input("what is your username?").strip()
    password = input("what is your passowrd?").strip()
    if username == "LaRose4" and password == "password":
        print("Welcome to the program")
        break
    else:
        print("those credentials were incorrect.")

 