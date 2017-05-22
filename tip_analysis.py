"""
tip_analysis.py

Name: Kaiqin Huang
Date: 1/24/2017

A script using pandas to load and analysis data in tips.csv.
"""


import pandas
import matplotlib.pyplot as plt

tips = pandas.read_csv("tips.csv")

tips["per_person"] = tips["total_bill"] / tips["size"]

tips["per_person"].describe()

print(tips["per_person"].min())
print(tips["per_person"].mean())
print(tips["per_person"].max())

tips_smoker = tips[tips["smoker"] == "Yes"]
print(tips_smoker["per_person"].mean())

plt.clf()
plt.hist(tips["per_person"])
plt.xlabel("price per person")
plt.ylabel("number of cases")
plt.title("Price per Person")
plt.savefig("priceperperson.png")
# plt.clf()

