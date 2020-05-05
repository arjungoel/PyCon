my_favorite_numbers = [1, 2, 3, 4, 5, 9]
doubled_numbers = []

for n in my_favorite_numbers:
    doubled_numbers.append(n*2)

print(doubled_numbers)

print('@@@@@@@@@@@@@@@@@@@@')

# better way of doing this using list comprehension
doubled_numbers = [n*2 for n in my_favorite_numbers]
print(doubled_numbers)