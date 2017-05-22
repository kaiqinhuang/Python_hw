"""
mpg_analysis.py

Name: Kaiqin Huang
Date: 1/24/2017

A script using pandas to load and analysis data in mpg.csv.
"""


import pandas
import matplotlib.pyplot as plt

mpg = pandas.read_csv("mpg.csv")
print(list(mpg.columns))

# Scatter plot of mpg and car weight
plt.clf()
plt.scatter(mpg["weight"], mpg["mpg"])
plt.xlabel("car weight")
plt.ylabel("mpg")
plt.title("Mpg and Car Weight")
plt.savefig("mpgandcarweight.png")

# Histogram of mpg for cars made before 1976
plt.clf()
mpg_bf76 = mpg[mpg["model_year"] < 76]
plt.hist(mpg_bf76["mpg"])
plt.xlabel("mpg")
plt.ylabel("number of cases")
plt.title("Mpg for Cars Made before 1976")
plt.savefig("mpgbefore1976.png")

# Histogram of mpg for cars made on or after 1976
plt.clf()
mpg_af76 = mpg[mpg["model_year"] >= 76]
plt.hist(mpg_af76["mpg"])
plt.xlabel("mpg")
plt.ylabel("number of cases")
plt.title("Mpg for Cars Made on or after 1976")
plt.savefig("mpgafter1976.png")

# Average mpg for cars made before or after 1976
print(mpg_bf76["mpg"].mean())
print(mpg_af76["mpg"].mean())
