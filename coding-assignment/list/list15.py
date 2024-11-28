# llist of cumulative sums
numbers = [1, 2, 3, 4]
cumulative_sum = []
current_sum = 0
for num in numbers:
    current_sum += num
    cumulative_sum.append(current_sum)
print(cumulative_sum)  # Output: [1, 3, 6, 10]