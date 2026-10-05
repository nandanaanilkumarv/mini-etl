import csv

with open("data.csv", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)

print("Row count:", len(rows) - 1)
def transform_data(data):
    return [row for row in data if row]