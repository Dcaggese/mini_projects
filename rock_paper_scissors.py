import random

CHOICES = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}

def main():
    print('Welcome to Rock, Paper, Scissors! Use the number keys to select your choice!')
    while True:
        game(CHOICES)
        play = input("press 'y' to play again").lower()
        if play != 'y':
            break

def game(option):
    while True:
        choice = int(input('Press 1 for Rock, 2 for Paper, or 3 for Scissors.'))
        if 1 <= choice <= 3:
            computer = random.randint(1,3)
            print(f'You have chosen {option[choice]}, the computer chooses {option[computer]}')
            if choice == computer:
                print("You've tied, play again.")
            elif choice == 1 and computer == 2:
                print("You lost, paper beats rock.")
            elif choice == 1 and computer == 3:
                print("You win, rock beats scissors.")
            elif choice == 2 and computer == 3:
                print("You lost, scissors beat paper.")
            elif choice == 2 and computer == 1:
                print("You win, scissors beats rock.")
            elif choice == 3 and computer == 1:
                print("You lost, rock beats scissors.")
            elif choice == 3 and computer == 2:
                print("You win, scissors beats paper.")
            break
        else:
            print('Invalid selection')


main()