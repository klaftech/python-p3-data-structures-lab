import ipdb

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



"""
Define a function get_names() that takes a list of spicy_foods 
and returns a list of strings with the names of each spicy food.
"""
def get_names(spicy_foods): 
    return [food.get("name") for food in spicy_foods]

print(get_names(spicy_foods))


"""
Define a function get_spiciest_foods() that takes a list of spicy_foods 
and returns a list of dictionaries where the heat level of the food is greater than 5.
"""
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]

print(get_spiciest_foods(spicy_foods))



"""
Define a function print_spicy_foods() that takes a list of spicy_foods 
and output to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶.

HINT: you can use times (*) with a stringLinks to an external site. to produce the correct number of "🌶" emojis.
for example:
"hello" * 3 == "hellohellohello"
# => True
print_spicy_foods(spicy_foods)
# => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# => Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
"""
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {food.get('heat_level') * '🌶'}")

print_spicy_foods(spicy_foods)


"""
Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods 
and a string representing a cuisine, 
and returns a single dictionary for the spicy food whose cuisine matches the cuisine 
being passed to the method.

get_spicy_food_by_cuisine(spicy_foods, "American")
# => {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}

get_spicy_food_by_cuisine(spicy_foods, "Thai")
# => {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}
"""
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food.get("cuisine") == cuisine][0]

print(get_spicy_food_by_cuisine(spicy_foods, "American"))


"""
Define a function print_spiciest_foods() that takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:
Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
"""
def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

print_spiciest_foods(spicy_foods)


"""
Define a function average_heat_level() that takes a list of spicy_foods and 
returns an integer representing the average heat level of all the spicy foods in the array. 
Recall that to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.

average_heat_level(spicy_foods)
# => 6
"""
def get_average_heat_level(spicy_foods):
    foods = [food.get("heat_level") for food in spicy_foods]
    total = 0
    for heat in foods:
        total += heat
    return int(total / len(foods))

print(get_average_heat_level(spicy_foods))



"""
Define a function create_spicy_food() that takes a list of spicy_foods and a new spicy_food 
and returns the original list with the new spicy_food added.
"""
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
))