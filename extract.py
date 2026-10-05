def transform_data(data):
    return [row for row in data if row is not None]

def load_data(data):
    print("Loading", len(data), "rows")