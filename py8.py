# Write a python function that takes a list and return a new list with unique elements of the first list.
# For example,Sample List =[1,1,1,2,2,3,3,4]Unique List = [1,2,3,4]

def get_unique_elements(input_list):
    
    unique_elements = []

    for element in input_list:
        # Check if the element is already in the list of unique elements
        if element not in unique_elements:
            # If not, add it to the list
            unique_elements.append(element)

    return unique_elements

List1 = [1, 1, 9, 2, 2, 3, 3, 4, 7, 7, 3, 9, 5]
unique_list = get_unique_elements(List1)
print(unique_list)
