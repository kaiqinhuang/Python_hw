"""
sorter.py

Name: Kaiqin Huang
Date: 1/19/2017

A script to sort the content in a file.
"""


try:
    # Reads the content in to_sort.txt
    before = input("What file would you like to sort? ")
    with open(before, "r") as f:
        content = f.read()
        list_to_sort = content.split("\n")
        list_to_sort.sort()  # _.sort() just sorts but does not return anything
    
    # Creates a new file sorted.txt and save the sorted content in it
    after = input("Where would you like to place the result? ")
    with open(after, "w") as f_sorted:
        for i in range(len(list_to_sort)):
            f_sorted.write(list_to_sort[i])
            f_sorted.write("\n")

    print("Done!")


except FileNotFoundError:
    print("Did not find the file.")

