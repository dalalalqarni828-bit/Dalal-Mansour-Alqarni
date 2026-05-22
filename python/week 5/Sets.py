colors = {"red", "blue", "green"}
print(colors)
colors.add("yellow")
colors.add("red")
print("Size:", len(colors))
print("red in set:", "red" in colors)
print("yellow in set:", "yellow" in colors)

print("_" * 30 + "\n" )

nums = {1, 2, 2, 3, 4, 4, 5, 1}

unique_nums = set(nums)

print("Unique values:", unique_nums)
print("Count of unique values:", len(unique_nums))

print("_" * 30 + "\n" )

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("In a but not in b:", a - b)
