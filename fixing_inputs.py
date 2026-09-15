# BO, 6th, Fixing Inputs

# when you want a number
while True:
    try:
        age = int(input("how old are you?"))
        break
    except:
        print("That isn't a number.")

print(f"Wow you are {age} that is really old!") 

# when you want a specific input
while True:
    color = input("Tell me a color that is only one word:").lower( ).strip()
    if color.isnumeric():
        print("sorry that is a number")
    elif " " in color:
        print("I said one word")
    else:
        break

print(f"I painted your walls {color}!")
