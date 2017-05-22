"""
    tipper.py
    
    Name: Kaiqin Huang
    Date: 1/5/17
    
    A short description of what this script should do.
    
    Inputs: bill amount and tip percentage
    Effects: calculate how much tip needs to pay and how much is the total bill amount
    Outputs: tip amount and total bill amount
"""

bill = float(input("What is your bill amount? "))
print("Hello, your bill is $%.2f." % bill)

percent_tip = int(input("How much percent tip do you want to pay? "))

tip_amount = bill * percent_tip / 100
total_bill = bill + tip_amount

print("Your tip amount is $%.2f" % tip_amount)
print("Your total bill is $%.2f." % total_bill)

if percent_tip > 25:
    print("Thank you!")
