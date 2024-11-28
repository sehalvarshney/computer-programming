 # shift all elements in a list by 2 positions left
numbers = [10, 20, 30, 40, 50]
shifted_list = []
for i in range(len(numbers)):
    shifted_list.append(numbers[(i + 2) % len(numbers)])
print(shifted_list)  # Output: [30, 40, 50, 10, 20]