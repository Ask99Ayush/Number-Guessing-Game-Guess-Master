from random import randint
from time import sleep

def get_difficulty():
    print("🎮 Choose Difficulty Level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–100)")
    print("3. Hard (1–1000)")
    print("4. Custom Range")
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            return 1, 10
        elif choice == '2':
            return 1, 100
        elif choice == '3':
            return 1, 1000
        elif choice == '4':
            try:
                low = int(input("Enter Lower Limit: "))
                high = int(input("Enter Upper Limit: "))
                if low >= high:
                    print("❌ Upper limit must be greater than lower limit.")
                    continue
                return low, high
            except ValueError:
                print("❌ Please enter valid integers.")
        else:
            print("❌ Invalid choice. Please select between 1-4.")

def get_hint(number):
    print("\n💡 ----------- HINT -----------")
    print("🔢 The number is", "even." if number % 2 == 0 else "odd.")
    print(f"🔢 It has {len(str(number))} digits.")
    
    for div in [7, 5, 3, 2]:
        if number % div == 0:
            print(f"🔍 It is divisible by {div}.")
            break
    print("------------------------------\n")

def play_game():
    low, high = get_difficulty()
    random_no = randint(low, high)
    attempts = 0
    max_attempts = 10

    print(f"\n🎯 Guess the number between {low} and {high}!")
    print("🚪 Enter -1 to exit, or -2 for a hint.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"🔢 Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("❌ Invalid input. Please enter an integer.\n")
            continue

        if guess == -1:
            print("\n👋 Game exited. Hope to see you again!\n")
            break

        elif guess == -2:
            get_hint(random_no)
            continue

        attempts += 1

        if guess == random_no:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            break

        elif guess > random_no:
            print("📉 Too high! Try a smaller number.\n")

        else:
            print("📈 Too low! Try a bigger number.\n")

    else:
        print(f"\n❌ You've reached the max limit of {max_attempts} attempts.")
        print(f"The correct number was: {random_no}")

def main():
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\n👋 Thanks for playing! Goodbye!\n")
            break

# Run the game
main()
