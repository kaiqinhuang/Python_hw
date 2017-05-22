# Assignment_2

p = 423121628483
n = 2
r = 1  # Define the reminder variable by assigning an initial value

while r != 0:
    r = p % n
    n += 1
    
if n == p + 1:
    print("%d is a prime number."%p)
elif n < p:
    print("%d is not a prime number."%p)
else:
    print("There is error.")
    