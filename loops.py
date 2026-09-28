#BO, 6th, loops notes
import random

#code that will repeat over and over again
count = 1

while count <= 10:
    print(count)
    count += 1

goose = random.randint(1,11)
duck = 1

while True:
    print("duck")
    if duck == goose:
        break
    duck += 1
print("GOOSE!!")

#lists
siblings = ["Aven", "Laura", "Etrina", "Lilia"]

print(siblings[2])
print(siblings)
siblings.append("Ara")
siblings.insert(3, "Bliss")
print(siblings)

#removing
print(siblings)
siblings.pop()
print(siblings)

#for loops
for number in range(1,11):
    print(number)

for sibling in siblings:
    print(sibling + " Oh")
