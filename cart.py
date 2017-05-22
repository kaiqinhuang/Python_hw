"""
cart.py

Name: Kaiqin Huang
Date: 1/13/2017

A module of three functions, shop(), value(), and item().
A point-of-sale system for a grocery store.
"""


def shop(cart):
    """Calculates the final quantity and bill for the shopping cart
        
    Arguments:
        cart (dict): A dictionary of products and prices
    
    Returns:
        print: final quantity and bill
    """

    value(cart)
    price_list = list(cart.values())
    quant_list = item(cart)
    
    bill = 0
    for i in range(len(price_list)):
        bill += price_list[i] * quant_list[i]

    quant_total = sum(quant_list)

    print("Total: $%.2f for %d items." % (bill, quant_total))
    print("Thank you for shopping!")


def value(cart):
    """Examines whether prices are all positive
        
    Arguments:
        cart (dict): A dictionary of products and prices
    
    Returns:
        assert
    """

    price_list = list(cart.values())
    for price in price_list:
        assert price > 0, "Error: Price should be positive."


def item(cart):
    """Gets a list of quantities for each product
        
    Arguments:
        cart (dict): A dictionary of products and prices
        
    Returns:
        quant_list (list): a list of quantities for each product
    """

    product_list = list(cart.keys())
    quant_list = []
    for i in len(product_list):
        quant = int(input("%s? " % product_list[i]))
        if quant < 0:
            quant = 0
        quant_list.append(quant)

    return quant_list
