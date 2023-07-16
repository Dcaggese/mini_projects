import random

def main():
    playing = True
    while playing:
        number = random.randint(1,100)

        guessed = guess()

        while True:
            if guessed == number:
                print("You guessed correct")
                break
            elif guessed < number:
                print("You guessed too low, the number is higher.")
                guessed = guess()
            elif guessed > number:
                print("You guessed too high, the number is lower.")
                guessed = guess()
        play = input("Press 'q' to quit or anything else to play again.").lower()
        if play == 'q':
            break

def guess():
    guess = int(input("Guess a number between 1 and 100: "))
    return guess

main()