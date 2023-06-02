def print_square():
    while True:
        try:
            num = int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            square = num ** 2
            print(f"The square of {num} is {square}.")
            break

print_square()
