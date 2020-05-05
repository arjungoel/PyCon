animals = {'birds': 1, 'cats': 2, 'mammals': 3}

for item in animals:
    print(f"I have {item}") # python 3.6 and beyond if you are not on this version you have to use .format() method.

print("#############")

# To get number along with category
for item in animals:
    print(f"I have {animals[item]} {item}")

print("@@@@@@@@@@@@@")

# better way of doing this
for animal, count in animals.items():
    print(f"I have {count} {animal}")