"""
Name: <Steve Hyland>
HW1.py

Problem: <Homework assignmet 1 - modify existing code and add code per assignment instructions>

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

# Provided Code - no changes to the code except deletion of the PASS statement
def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

# First Coding Exercise - my changes to the code - compute volume length * width * depth.
def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    depth = eval(input("Enter the depth: "))
    vol = length * width * depth
    print("Volume =", vol)

# Second coding exercise - calculate shooter's accuracy percentage - shots made / attempts.
def shooting_percentage():
    shots = eval(input("Enter the player's total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    percentage = made / shots * 100
    print("Shooting Percentage =", percentage)

# Third coding exercise - calculate total cost of a coffee order with given defaults.
def coffee():
    qty = eval(input("How many pounds of coffee would you like?: "))
    cost = 1.50 + (qty * 10.50) + (qty * 0.86)
    print("Your total is: ", cost)

# Fourth coding exercise - convert kilosmeters to miles with formula provided.
def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?: "))
    miles = (kilometers / 1.61)
    print("That's", miles, "miles!")

if __name__ == '__main__':
    pass

# instructions for running - uncomment the procedure you wish to test by removing the hashtag.

calc_rec_area()

calc_volume()

shooting_percentage()

coffee()

kilometers_to_miles()
