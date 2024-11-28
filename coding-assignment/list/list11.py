# finding the third smallest element in a list
numbers = [40, 10, 20, 50, 30]
sorted_list = []
while len(sorted_list) < 3:
    smallest = float('inf')
    for num in numbers:
        if num < smallest and num not in sorted_list:
            smallest = num
    sorted_list.append(smallest)
third_smallest = sorted_list[2]
print(third_smallest)  # Output: 30