"""
fileop.py

Name: Kaiqin Huang
Date: 1/21/2017

A module of function cat().
"""


def cat(files, target):
    
    target_list = []


    # Reads the content in the files on list
    for file in files:
        try:
            with open(file, "r") as f:
                content = f.read()
                content_list = content.split("\n")
                target_list.extend(content_list)

        except FileNotFoundError:
                print("Did not find the file %s." % file)


    # Writes the content in the target file
    try:
        with open(target, "w") as t:
            for i in range(len(target_list)):
                t.write(target_list[i])
                t.write("\n")

    except FileNotFoundError:
        print("Did not find the file %s." % target)


    # Returns the number of non-empty lines
    num_lines = 0
    for i in range(len(target_list)):
        if target_list[i] != "":
            num_lines += 1

    return num_lines

