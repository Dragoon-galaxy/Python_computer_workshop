def compare_numbers(num1, num2):
    
    if num1 % 2 == 0 and num2 % 2 == 0:
        # Both numbers are even
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        # One or both numbers are odd
        if num1 > num2:
            return num1
        else:
            return num2

print(compare_numbers(2, 4)) 
print(compare_numbers(17, 13)) 
print(compare_numbers(10, 19)) 
