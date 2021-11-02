my_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(my_list)
drinks_list= ["Lemonade", "Sprite", "Dr.Pepper", "Ginger Ale", "Fanta", "Water", "Pepsi", "Manzana"]
drinks_list[2]
print(drinks_list[2])
print(drinks_list[0:3])
drinks_list[3] = "Acid"
print(drinks_list)
drinks_list[4]= "H20"
drinks_list[1]= "Chemicals"
drinks_list[2]= "Sodium"
print(drinks_list)
drinks_list.extend(["Iron", "Calcium", "Sulfur"])
print(drinks_list)
drinks_list.append("Sprite")
drinks_list.insert(5, "Fanta")
print(drinks_list)
del drinks_list[4]
print(drinks_list)
drinks_list.pop(2)
print(drinks_list)
drinks_list.remove("Water")
print(drinks_list)
