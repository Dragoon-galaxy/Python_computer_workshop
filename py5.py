import random

cups = ["X", "O", "O"]
ball = "X"

while True:
    random.shuffle(cups)

    # Print the shuffled cups
    print(f"    _____   _____   _____ ")
    print(f"   |     | |     | |     |")
    print(f"   |  {cups[0]}  | |  {cups[1]}  | |  {cups[2]}  |")
    print(f"   |_____| |_____| |_____|")

    # Ask the player to guess which cup the ball is under
    guess = input("Guess which cup the ball is under (1-3), or enter 'q' to quit: ")

    if guess.lower() == "q":
        print("Thanks for playing!")
        break

    guess_index = int(guess) - 1

    if cups[guess_index] == ball:
        print("Congratulations, you found the ball!")
        print(f"    _____   _____   _____ ")
        print(f"   |     | |     | |     |")
        print(f"   |     | |  {ball}  | |     |")
        print(f"   |_____| |_____| |_____|")
        break
    else:
        print(f"Sorry, the ball was under cup {cups.index(ball)+1}. Try again.")

