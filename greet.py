"""
    greet.py
    
    Name: Kaiqin Huang
    Date: 1/8/17
    
    Greetings and judge whethere leagal to buy alcohol or not.
    
    Inputs: name and age
    Effects: if age is above 21 then it is legal to buy alcohol
    Outputs: greeting by name and legal or not to buy alcohol
    """


name = input("What is your name? ")
print("Neat!")
print("Hello, %s!" % name)

age = int(input("How old are you? "))
while age < 0:
    age = int(input("Please enter a reasonable age.  How old are you? "))

born_year = 2017 - age
print("You were born in %d." % born_year)

if age >= 21:
    print("Yes, you can legally buy alcohol in the state of California.")
else:
    print("No, you are not old enough to legally buy alcohol in the state of California.")

print("Goodbye, %s, who is %d years old." % (name, age))
