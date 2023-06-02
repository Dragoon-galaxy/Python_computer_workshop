# Write a program using function to check who is employee of the month.

employees = {"Ash": [5000, 6000, 7000], "Ben": [4000, 5500, 6000], "Kenichi": [6000, 6500, 8000],
             "Nobita": [9000, 4400, 8880], "Max": [1000, 3300, 1500]}

print('The name of Employees are: ')
for i in employees:
    print(i)
        
def eom(emp_data):
    
    top_employee = None
    top_performance = 0
     
    for emp_name, performance in emp_data.items():    
        cumulative_performance = sum(performance)
        if cumulative_performance > top_performance: 
            top_employee = emp_name
            top_performance = cumulative_performance
     
    return top_employee
 
result = eom(employees)
print(f"The employee of the month is {result}.")
