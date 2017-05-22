"""
functionization

Name: Kaiqin Huang
Date: 1/12/2017

A module of functions.
"""


def tipper(bill, tip_percent):
    """Gets the factorial of n
        
    Arguments:
        bill (float): Original bill amount
        tip_percent (int): Tip percent, which is between 0 and 100
        
    Returns:
        tip_amount: Tip amount
        total_bill: Final bill needs to pay
    """
    
    print("Hello, your bill is %.2f." % bill)
    
    tip_amount = bill * tip_percent / 100
    print("Your tip amount is %.2f." % tip_amount)
    
    total_bill = bill + tip_amount
    print("Your total bill is %.2f." % total_bill)

    if tip_percent > 25:
        print("Thank you!")


def greet(name, age):
    """Greets by name and age, and determine whether or not can legally buy alcohol
        
    Arguments:
        name (str): Your name
        age (int): Your age
        
    Returns:
        print
    """

    print("Hello, %s!" % name)

    assert age > 0, "Age should be reasonable."

    born_year = 2017 - age
    print("You were born in %d." % born_year)
    
    if age >= 21:
        print("Yes, you can legally buy alcohol in the state of California.")
    else:
        print("No, you are not old enough to legally buy alcohol in the state of California.")

    print("Goodbye, %s, who is %d years old." % (name, age))


def choice(basket):
    """Gets the item in basket that should buy
        
    Arguments:
        basket: A list of items you might want to buy
        
    Returns:
        print
    """

    import random
    
    purchase = random.choice(basket)
    print("Out of all those options in basket, you should probably buy %s." % purchase)


def exponentiate(base, power):
    """Gets the exponentiation
        
    Arguments:
        base: The base number
        power: The power
        
    Returns:
        x: The exponentiation
    """
    
    x = 1
    for _ in range(power):
        x *= base
    
    print("Number %d to the power %d is %d." % (base, power, x))
    return x


def prime_test(p):
    """Estimates whether a number is a prime number or not
    
    Arguments:
        p (int): The number needs to estimate
    
    Returns:
        print
    """

    n = 2
    r = 1
    
    while r != 0:
        r = p % n
        n += 1

    assert n < p + 2, "There is an error."

    if n == p + 1:
        print("Yes, %d is a prime number." % p)
        return True
    else:
        print("No, %d is not a prime number" % p)
        return False

