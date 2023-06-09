my_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 8, 9, 10, 10]

duplicates = []
seen = []

for item in my_list:
    if item not in seen:
        seen.append(item)
    else:
        if item not in duplicates:
            duplicates.append(item)

print("Duplicate elements:", duplicates)