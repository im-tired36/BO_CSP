# BO, 6th, Hello User

while True:
    name = input("Tell me your first name:").lower( ).strip()
    if name.isnumeric():
        print("sorry that is a number")
    elif " " in name:
        print("I said only your first name")
    else:
        break


print(f"Hello, {name} nice to meet you!")