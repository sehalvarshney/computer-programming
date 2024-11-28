#  reversing a list
numbers = [10, 20, 30, 40]
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
print(reversed_list)  # Output: [40, 30, 20, 10]