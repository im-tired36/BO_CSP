#BO, 6th, String notes

first_name = 'bliss'
last_name = "oh"

#concatenation => add two string together
name = first_name + " " + last_name

#escape character lets the
print(f'{name} told the class, "you can\'t drive my car."')

user= input("please tell me your name:\n").strip().title()

print(f"New user recognized\nWelcome { user}")
 
sentence = "The quick brown fox jumped over the lazy dog."
print(sentence)
print(sentence.replace("dog", name))