def validate_input():
    while True:
        user_input = input("Please enter a number between 1 and 10: ")

        try:
            number = int(user_input)
            if 1 <= number <= 10:
                print("Valid input!")
                break
            else:
                print("Input out of range. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

validate_input()
