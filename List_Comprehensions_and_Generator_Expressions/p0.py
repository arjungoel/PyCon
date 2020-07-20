colors = ['red', 'green', 'blue']
rations = [0.1, 0.2, 0.3]
ratios = [*rations, 5]   # python3 syntax

# using enumerate()
for i, color in enumerate(colors):
    print(color, rations[i])

# using zip()
for color, ratio in zip(colors, rations):
    print(f"The colors value is:{color} and the rations value is:{ratio}")

for color, ratio in zip(colors, ratios):
    print(color, ratio)
