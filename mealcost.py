
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
    meal_cost = float(input("Input meal cost:"))

    tip_percent = int(input("Input tip percent:"))

    tax_percent = int(input("Input tax percent:"))

    print(solve(meal_cost, tip_percent, tax_percent))
   
