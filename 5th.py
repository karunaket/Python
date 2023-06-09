numbers = [1, 2, 3, 1, 2, 4, 5]

unique_numbers = []

for number in numbers:

    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)