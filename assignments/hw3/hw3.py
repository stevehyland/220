"""
Name: <Steve Hyland>
<hw3.py>

Problem: <This HW assignemnt consist of looping and assignment issues.  Of note were
 several instances of promoting data types from INT to FLOAT and the consequences>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work.>

"""
#
def average():
    sum_total = 0
    tot_grades = eval(input("how many grades will you enter?: "))
    for _n in range(tot_grades):
        grade = eval(input("Enter grade: "))
        sum_total = sum_total + grade
    avg = sum_total / tot_grades
    print("average is ", avg)
#
def tip_jar():
    tip_total = float
    donation = float
    tip_total = 0.0
    for _ in range(5):
        donation = eval(input("how much would you ike to donate? "))
        tip_total = tip_total + donation
#
    print("total tips: ", tip_total)
#
def newton():
    approx = float
    approx = eval(input("what number do you want to square root? :"))
    iterations = eval(input("how many times should we improve the approximation?: "))
    xapprox = approx
#
    for _ in range(iterations):
        approx = (approx + (xapprox/approx))/2
#
    print("the square root is approximately ", approx)
#
def sequence():
    terms = int
    terms = eval(input("how many terms would you like? "))
    for i in range(1, terms + 1, 2):
        print(i, end=' ')
        for _ in range(i, terms, terms):
            print(i, end=' ')
#
def pi():
    terms = int
    pi_div2 = float
    pi_div2 = 1.00
    rterms = int
    tterms = int
    terms = eval(input("how many terms would you like? "))
    rterms = (terms+1)//2
    tterms = round(terms//2)
    for nth in range(1, rterms+1):
        #print(n, end=' ')
        pi_1 = (2*nth)/((2*nth)-1)
        pi_div2 = pi_div2 * pi_1
        #print("pi_1 + ",pi_1)
        for _ in range(nth, tterms+1, terms):
            pi_2 = (2*nth)/((2*nth)+1)
            pi_div2 = pi_div2 * pi_2
#
    pi_div2 = pi_div2 * 2.
    print("approx value of pi:",pi_div2)
#
;
#
#average()
#
#tip_jar()
#
#newton()
#
#pi()
#
#sequence()
