
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = tip_percent / 100 * meal_cost
    tax = tax_percent / 100 * meal_cost
    return round(meal_cost + tip + tax)
    
if __name__ == '__main__':
    i = 4
    d = 4.0
    s = 'HackerRank'

    i += int(input("Input int value:"))

    d += float(input("Input double value:"))

    s += input("Input String value:")

    print(i)
    print(d)
    print(s)

   
