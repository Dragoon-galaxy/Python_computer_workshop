def count_upper_lower(s):
    
    upper_count = 0
    lower_count = 0
    
    for i in s:
        # Check if the character is an upper case letter
        if i.isupper():
            upper_count += 1
        # Check if the character is a lower case letter
        elif i.islower():
            lower_count += 1
            
    print(f'Number of upper case letters are : {upper_count}')
    print(f'Number of lower case letters are : {lower_count}')


str1 = "Set Your Heart Upon Your Work But Never Its Reward."
count_upper_lower(str1) 
