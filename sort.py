import json


class fruit:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color
        print(self.id, self.name, self.color)


fruits = [
    fruit(1, "apple", "pink"),
    fruit(2, "mango", "yellow"),
    fruit(3, "banana", "yellow"),
    fruit(4, "orange", "orange"),
    fruit(5, "grapes", "green"),
]


def get_sorted_fruits():
    # Sort the fruits based on color
    sorted_fruits = sorted(fruits, key=lambda x: x.color)
    return sorted_fruits

ad = get_sorted_fruits()
# Convert fruits to a JSON serializable format
fruits_json = []
for fruit in ad:
    fruits_json.append({
        'id': fruit.id,
        'name': fruit.name,
        'color': fruit.color
        })
print(fruits_json)