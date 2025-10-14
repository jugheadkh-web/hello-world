import math

def main():
    print("Think of a number between two numbers.")
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    max_guesses = math.ceil(math.log2(high - low + 1))
    print(f"I will guess your number in at most {max_guesses} tries.")

    attempts = 0
    min_possible = low
    max_possible = high

    while min_possible <= max_possible:
        guess = (min_possible + max_possible) // 2
        print(f"My guess is: {guess}")
        response = input("Enter 'higher', 'lower', or 'correct': ").lower()

        attempts += 1

        if response == "correct":
            print(f"I guessed it in {attempts} tries!")
            return
        elif response == "higher":
            min_possible = guess + 1
        elif response == "lower":
            max_possible = guess - 1
        else:
            print("Invalid input. Please enter 'higher', 'lower', or 'correct'.")

        if min_possible > max_possible:
            print("Inconsistent answers detected. Are you cheating?")
            return

    print("Something went wrong. Exiting.")

if __name__ == "__main__":
    main()
