# create a running product list
numbers = [1, 2, 3, 4]
running_product = []
current_product = 1
for num in numbers:
    current_product *= num
    running_product.append(current_product)
print(running_product)  # Output: [1, 2, 6, 24]