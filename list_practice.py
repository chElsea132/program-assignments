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
def print(my_list):
    for el in my_list:
        print(el)
    return "All cities printed"

def reorganize_list(my_list):
    # [1,2,3,4,5]
    print(my_list)
    counter = 0

    while counter <= len(my_list):
        item1 = my_list[counter]
        item2 = my_list[counter + 1]
        
        if len(item1) >= len(item2):
            counter += 1
            continue
        elif counter + 1 == len(my_list):
            break
        else:
            my_list.remove(item1)
            my_list.append(item1)
            counter += 1
    return my_list

def sort_list(my_list):
    return sorted()

print(my_list)
