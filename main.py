# Using Pandas module
from pandas import *


def get_total_price_from_csv(file):
    data = read_csv(file)
    return data["price"].sum()


print(get_total_price_from_csv("example.csv"))

# Using csv module
import csv

def get_total_price_from_csv_module(file_path):
    filename = open(file_path, "r")
    file = csv.DictReader(filename)
    
    total_profit = []
    
    for col in file:
        total_profit.append(float(col["price"]))
    filename.close()
    return sum(total_profit)


print(get_total_price_from_csv_module("./example.csv"))