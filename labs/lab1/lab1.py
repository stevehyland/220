"""
Steve Hyland
\
"""


def monthly_interest():
    # prompt for inputs
    annual_rate = eval(input("Enter your Annual Interest Rate: "))
    monthly_rate = (annual_rate / 12) / 100
    print("monthly rate: ", monthly_rate)
    #
    days_in_cycle = eval(input("enter billing Cycle Days: "))
    previous_bal = eval(input("Input previous balance: "))
    payment_amt = eval(input("Input payment amount: "))
    day_of_cycle = eval(input("Input cycle day paid: "))
    net_balance = previous_bal * days_in_cycle
    max_to_apply = payment_amt * (days_in_cycle - day_of_cycle)
    print("max to apply: ", max_to_apply)
    new_balance = net_balance - max_to_apply
    avg_daily = new_balance / days_in_cycle

    monthly_int = avg_daily * monthly_rate
    print( "monthly intereat:  $ ", monthly_int)

monthly_interest()

