import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals(data):
    for animal in data:
        name = animal.get("name")
        locations = animal.get("locations") or []
        characteristics = animal.get("characteristics") or {}
        diet = characteristics.get("diet")
        type_ = characteristics.get("type")

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations:
            print(f"Location: {locations[0]}")
        if type_:
            print(f"Type: {type_}")
        print()

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    print_animals(animals_data)
