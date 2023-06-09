list = [1, 2, 3, 4, 5]

max = list[0]
min = list[0]

for element in list:
    if element < min:
        min = element
    
    if element > max:
        max = element

print("Min value is", min)
print("Max value is", max)