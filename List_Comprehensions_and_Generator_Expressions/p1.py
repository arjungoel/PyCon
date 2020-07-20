animals = {'birds': 3, 'cats': 2, 'dogs': 1}


# 1st way to loop over dictionary
for item in animals:
    print(f"I have {animals[item]} {item}")  # print the both keys and values.

print("============================================================================================================")

# 2nd way to loop over dictionary
for animal, count in animals.items():  # iteritems() has been deprecated.
    print(f"I have {count} {animal}")
