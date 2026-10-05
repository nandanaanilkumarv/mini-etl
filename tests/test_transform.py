import sys
sys.path.insert(0, ".")
from extract import transform_data
def test_transform_data():
    data = [["Anu", 22], None, ["Rahul", 25]]
    result = transform_data(data)

    assert None not in result