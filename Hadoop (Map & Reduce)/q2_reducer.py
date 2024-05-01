#!/usr/bin/env python3
import sys

current_key = None
prices = []

def calculate_average(prices):
    return sum(prices) / len(prices) if prices else 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    price = float(value)

    if key == current_key:
        prices.append(price)
    else:
        if current_key:
            # Output the average price for the current instance type and hour
            print(f'{current_key}\t{calculate_average(prices)}')
        current_key = key
        prices = [price]

# Don't forget the last key
if current_key:
    print(f'{current_key}\t{calculate_average(prices)}')
