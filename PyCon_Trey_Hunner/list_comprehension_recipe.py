my_favorite_numbers = [1, 2, 3, 4, 5, 9]

doubled_numbers = []
for n in my_favorite_numbers:
    doubled_numbers.append(n*2)

###########################################
'''list comprehension recipe '''
###########################################


# single-line notation
doubled_numbers = [n*2 for n in my_favorite_numbers]

# multi-line notation 
doubled_numbers = [
    n*2
    for n in my_favorite_numbers 
]
