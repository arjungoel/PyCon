colors = ['red', 'green', 'blue']
ratios = [0.1, 0.2, 0.3]

for i in range(len(colors)):
    print(colors[i], ratios[i])

print('#################')

# better way of doing
for i, color in enumerate(colors):
    print(color, ratios[i])

print('@@@@@@@@@@@@@@@@@')

# another better way as we are looping over 2 things at the same time
for color, ratio in zip(colors, ratios):
    print(color,ratio)

print('$$$$$$$$$$$$$$$$$')

# if the lists are not of same length
# zip stops at the shortest one.
ratios_copy = [*ratios, 0.4]

for color, ratio in zip(colors, ratios_copy):
    print(color, ratio)