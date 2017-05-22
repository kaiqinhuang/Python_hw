"""
lab13.py

Name: Kaiqin Huang
Date: 1/25/2017

A file to implement a Flask server.
"""


from flask import Flask
import pandas
import matplotlib as plt
app = Flask(__name__)


reviews = { "the princess bride": "as you wish",
            "happy feet": "what's your heart song?",
            "wizard of oz": "there's no place like home"
          }

@app.route("/movies/<movie>")
def movies(movie):
    return reviews[movie]


@app.route("/histo/<column>.png")
def histo(column):
    mpg = pandas.read_csv("mpg.csv")
    plt.clf()
    if column in list(mpg.column):
        plt.hist(column)
        plt.title(column)
        plt.savefig("static/histo.png")
    else:
        print("There is no such an attribute in the given data.")
    return app.send_static_file("static/histo.png")


@app.route("/keys/move/<location>")
def keys_move(location):
    with open("location.txt", 'w') as f:
        f.write("%s\n" % location)
    #f.write("\n")
    return ("Location recorded, thanks!")


@app.route("/keys/locate")
def keys_locate():
    with open("location.txt", 'r') as f:
        return f.read()


app.run()

