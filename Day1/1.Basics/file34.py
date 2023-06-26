# if elif else statement

age = 200

if age == 0 or age < 0:
    print("You can't watch")
elif 0 < age <= 3:
    print("Ticket price is : Free")
elif 3 < age <= 10:
    print("Ticket price : 150")
elif 10 < age <= 60:
    print("Ticket price is 200")
else:
    print("Ticket price is 200")
