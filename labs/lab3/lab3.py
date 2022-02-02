"""
Steve Hyland
File Name: lab3.py
Lab1 Assignment 3: Calculate Mean value of entered data.
I did this alone.

"""
def traffic():
    roads_tot = eval(input("How many roads were surveyed? "))
    tot_total = 0
    for idays in range(1, roads_tot+1):
        print("How many days was road", idays, "surveyed? ",end=" ")
        days = eval(input(" "))
        days_total = 0
        for day_n in range(1,days+1):
            print("\t","How many cars traveled on day",day_n," ?",end=" ")
            daily_total = eval(input(" "))
            days_total = days_total + daily_total
        roadn_avg = days_total / days
        tot_total = tot_total + days_total
        print("Road", idays, "average vehicles per day ", roadn_avg)
    daily_average = tot_total / idays
    print("Total number of vehicles traveled on all roads:", tot_total)
    print("Average number of vehicles per road ", round(daily_average,2))
#
#traffic()






