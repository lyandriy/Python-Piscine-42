import random

def gess_game():
    number = random.randint(1, 99)
    count = 0
    while True:
        count += 1
        txt = input("What's your guess between 1 and 99?\n")
        if txt == "exit":
            print("Goodbye!")
            return None
        try:
            txt = int(txt)
            if txt < number:
                print("Too low!")
            elif txt > number:
                print("Too high!")
            elif txt == number:
                if number == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                if count == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print(f"You won in {count} attempts!")
                return None
        except ValueError:
            print("That's not a number.")
    

if __name__ == "__main__":
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    gess_game()