#BO, 6th, reading and writing to files

with open("practice.txt", "r") as file:
    content = file.read()
    print(content)
    print(content.upper())
    word = content.find("bliss")
    length = len("bliss")
    print(content[word:word+length])

with open("practice.txt", "w") as file:
    file.write("hello")

with open("practice.txt", "r+") as file:
    content = file.read()
    print(content)
    content+= "Treyson"
    file.write(content)

with open("practice.txt", "a") as file:
    content = file.write("another line")