import sys
from stats import average_by_city, read_valid, warmest_city
lines = sys.stdin.read().splitlines()
records = read_valid(lines)
averages = average_by_city(records)
city = warmest_city(records)
invalid_count = sum(1 for line in lines if line) - len(records)
print(len(records))
print(invalid_count)
if city:
    print(f"{averages[city]:.1f}")
else:
    print("0.0"))