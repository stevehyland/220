"""
Name: <Steve Hyland>
<Pro>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

# Provided Code - no changes to the code except deletion of the PASS statement
def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

# First Coding Exercise - my changes to the code
def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    depth = eval(input("Enter the depth: "))
    vol = length * width * depth
    print("Volume =", vol)

# Second coding exercise - calculate shooter's accuracy percentage
def shooting_percentage():
    shots = eval(input("Enter the player's total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    percentage = made / shots * 100
    print("Shooting Percentage =", percentage)

# Third coding exercise - calculate total cost of a coffee order
def coffee():
    qty = eval(input("How many pounds of coffee would you like?: "))
    cost = 1.50 + (qty * 10.50) + (qty * 0.86)
    print("Your total is: ", cost)

# Fourth coding exercise - convert kilosmeters to miles
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


