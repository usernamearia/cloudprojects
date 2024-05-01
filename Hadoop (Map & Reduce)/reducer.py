#!/usr/bin/env python3
import sys

def calculate_average_price_fluctuations(price_list):
    # Calculate average price fluctuation between consecutive prices
    if len(price_list) < 2:
        return 0
    fluctuations = [abs(price_list[i] - price_list[i-1]) for i in range(1, len(price_list))]
    average_fluctuation = sum(fluctuations) / len(fluctuations)
    return average_fluctuation

current_key = None
current_prices = []

for line in sys.stdin:
    line = line.strip()
    composite_key, value = line.split('\t', 1)
    timestamp, price = value.split(',')
    price = float(price)

    if current_key == composite_key:
        current_prices.append(price)
    else:
        if current_key:
            average_fluctuation = calculate_average_price_fluctuations(current_prices)
            print(f'{current_key}\t{average_fluctuation}')
        current_key = composite_key
        current_prices = [price]

# Don't forget the last key
if current_key:
    average_fluctuation = calculate_average_price_fluctuations(current_prices)
    print(f'{current_key}\t{average_fluctuation}')
