def intro():
    print("\nWelcome to the Jungle Adventure!")
    print("You're an explorer entering a mysterious jungle in search of an ancient treasure.")
    print("Do you want to:")
    print("1. Enter the jungle path")
    print("2. Walk along the river")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        jungle_path()
    elif choice == "2":
        river_path()
    else:
        print("Invalid choice. Try again.")
        intro()

def jungle_path():
    print("\nYou venture deep into the jungle.")
    print("You see a fork in the path. Do you:")
    print("1. Take the left path towards the ruins")
    print("2. Take the right path into the dense forest")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        ruins()
    elif choice == "2":
        forest()
    else:
        print("Invalid choice. Try again.")
        jungle_path()

def river_path():
    print("\nYou follow the river and see a boat tied to a tree.")
    print("Do you:")
    print("1. Use the boat to go downstream")
    print("2. Ignore the boat and continue on foot")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        waterfall()
    elif choice == "2":
        crocodile()
    else:
        print("Invalid choice. Try again.")
        river_path()

def ruins():
    print("\nYou reach ancient ruins covered in vines.")
    print("Inside, you find the treasure! You win!")
    play_again()

def forest():
    print("\nThe forest is too thick and you get lost.")
    print("After wandering for hours, you realize you're going in circles.")
    print("Game over.")
    play_again()

def waterfall():
    print("\nThe boat speeds up and you hear rushing water.")
    print("You fall off a waterfall but land in a deep pool unharmed.")
    print("You climb out and discover a hidden cave with treasure. You win!")
    play_again()

def crocodile():
    print("\nAs you walk, a crocodile lunges out of the river!")
    print("You try to run, but it's too fast. Game over.")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        intro()
    elif choice == "no":
        print("Thanks for playing!")
    else:
        print("Invalid input.")
        play_again()

# Start the game
intro()
