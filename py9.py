# Write a python function to multiply all the numbers in the list

def multiply_list(numbers):
    
    result = 1
    for num in numbers:
        result *= num
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = multiply_list(my_list)
print(product)


