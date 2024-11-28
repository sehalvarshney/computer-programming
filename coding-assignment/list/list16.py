#  find second largest number in a given list
numbers = [10, 20, 15, 5, 25]
largest = numbers[0]
second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)  # Output: 20