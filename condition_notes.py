#BO, 6th, Conditional

military_time = 900

if military_time < 600:
    print("It is the afternoon.")
elif military_time < 900:
    print("Good morning!")
elif military_time < 1200:
    print("Good morning! You should be at school.")
elif military_time < 1700:
    print("Good afternoon!")
else:
    print("Good evening!")

#nesting conditional
day = "Saturday"
time = 900

if time > 900 and time < 1600:
    if day != "Saturday" or day != "Sunday":
        print("You should be at school!")
    else:
        if time > 1200:
            print("Good afternoon!")
        else:
            print("Good Morning!")
else:
    print("You are not required to be at school.")
             