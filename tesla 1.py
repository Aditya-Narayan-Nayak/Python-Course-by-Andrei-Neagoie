def checkdriverAge():
    age = input("what is your age ?: ")
    if int(age) < 18:
        print("sorry, you are too young to drive to drive this car< powering off")
    elif int(age) > 18:
        print("powering on. Enjoy your ride!");
    elif int(age) == 18:
        print("congratulation on your first year of driving. Enjoy your ride ");
checkdriverAge()

# def checkdriverAge(age=0):
#     if int(age < 18):
#         print("sorry you are too young to drive the car. parking off")
#     elif int(age)>18:
#         print("Powering on, enjoy your ride");
#     elif int(age)==18:
#         print("congradulation on your first year of driving, Enjoy the ride!")
# checkdriverAge()