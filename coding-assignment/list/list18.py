# replace negative numbers with 0
numbers = [5, -1, 0, -8, 3]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print(numbers)  # Output: [5, 0, 0, 0, 3]