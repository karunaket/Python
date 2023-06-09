list = [1, 2, -3, 4, -5]

positive_count = 0
negative_count = 0

for element in list:

    if element > 0:
        positive_count += 1

    elif element < 0:
        negative_count += 1

print("The number of positive numbers is", positive_count)
print("The number of negative numbers is", negative_count)