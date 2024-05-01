#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')

    # Ensure there are enough columns (timestamp, instance type, OS, region/zone, price)
    if len(parts) >= 5:
        timestamp = parts[0]
        instance_type = parts[1]
        os = parts[2]
        availability_zone = parts[3]
        price = parts[4]

        # Output composite key and value
        print(f'{instance_type},{os},{availability_zone}\t{timestamp},{price}')
