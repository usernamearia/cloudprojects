#!/usr/bin/env python3
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')

    # Ensure there are enough columns (timestamp, instance type, OS, region/zone, price)
    if len(parts) >= 5:
        timestamp_str = parts[0]
        instance_type = parts[1]
        os = parts[2]
        availability_zone = parts[3]
        price = parts[4]

        # Parse timestamp to Python datetime object
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S+00:00")
        
        # Check if the record is within the "eu-central-1" region, for Linux/UNIX OS, and between 9 AM and 5 PM
        if 'eu-central-1' in availability_zone and os == 'Linux/UNIX' and 9 <= timestamp.hour <= 17:
            # Emit instance type, timestamp hour, and price for further processing
            print(f'{instance_type},{timestamp.hour}\t{price}')
