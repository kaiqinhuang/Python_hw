"""
vending.py

Name: Kaiqin Huang
Date: 1/18/2017

A module of class VendingMachine.
"""


class VendingMachine:

    def __init__(self, initial_chocolates):  # __init__(): constructor
        '''Gives the number of chocolates in the vending machine
            
        Args:
            initial_chocolates: number of chocolates left in this vending machine
            
        Returns:
            none
            
        '''

        self.chocolates = initial_chocolates  # properties
        print("There is (are) %d chocolate(s) left in this vending machine!" % initial_chocolates)


    def vend(self):  # vend(): method
        '''Plays as a real vending machine
            
        Args:
            none
            
        Returns:
            none
            
        '''

        if self.chocolates > 0:
            self.chocolates -= 1
            print("Here is a chocolate!")
        elif self.chocolates == 0:
            print("Sorry, no more chocolate!")
        else:
            print("The vending machine might be broken.")

