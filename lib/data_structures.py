spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

# => ["Green Curry", "Buffalo Wings", "Mapo Tofu"]    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# => [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, 
# => {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# => Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

get_spicy_food_by_cuisine(spicy_foods, "American")
# => {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}

get_spicy_food_by_cuisine(spicy_foods, "Thai")
# => {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{ food['name'] } ({ food['cuisine'] }) | Heat Level: { '🌶' * food['heat_level']}")

# => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    return total / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
