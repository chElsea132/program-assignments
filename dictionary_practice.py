nba_players = ["Lebron James", "Kevin Durant", "Stephen Curry", "Damian Lillard", "Kawhi Leonard"]
print("\nIndex of Lebron James:")
print(nba_players[0])
food_items= {"Chicken": 1.59,"Beef":1.99, "Cheese":1.00, "Milk": 2.50 }
print(food_items["Milk"])
age_numbers= {"Jaden": 3, "Matthew": 12, "Tyson": 16, "Chelsea": 22}
print(age_numbers)
print(age_numbers["Jaden"])
shoes_numbers= {"Jordan 13": 1,"Yeezy": 8,"Foamposite": 10,"Air Max": 5,"SB Dunk": 20}
print(shoes_numbers["Yeezy"])
shoes_numbers["Jordan 13"] = 8
shoes_numbers= {"Jordan 13": 8, "Yeezy": 16, "Foamposite": 18,"Air Max": 13,"SB Dunk": 28}
print(shoes_numbers["SB Dunk"])
shoes_numbers= {"Jordan 13": 5, "Yeezy": 11, "Foamposite": 15,"Air Max": 10,"SB Dunk": 25}
print(shoes_numbers["Yeezy"])
shoes_numbers= {"Jordan 13": 5, "Yeezy": 11, "Foamposite": 15,"Air Max": 10,"SB Dunk": 25, "Converse": 25, "Nike": 37}
del shoes_numbers["Yeezy"]
print(shoes_numbers["Air Max"])
del food_items["Chicken"]
del food_items["Milk"]
def total_price(food_item, food_item2): 
    total = food_items[food_item] + food_items[food_item2]
    return total
def price_diff(food_item, food_item2): 
    diff = food_items[food_item]- food_items[food_item2]
    return abs(diff)
print(total_price("Beef", "Cheese"))
print(price_diff("Beef", "Cheese"))
print(shoes_numbers)
del shoes_numbers["Jordan 13"]
del shoes_numbers["Converse"]
def shoe_restock(shoe, num):
    shoes_numbers[shoe] *= num 
    return shoes_numbers
def clearance_sale(shoe, num):
    shoes_numbers[shoe] *= num 
    return shoes_numbers
print(shoe_restock("Air Max", 3))
print(clearance_sale("SB Dunk",2))
def supply_search(dict):
    largest = 0
    supply= ''

    for key in dict.keys():
        if dict[key] > largest:
            largest = dict[key]
            supply = key 

    return (supply, largest)

print(supply_search(shoes_numbers))