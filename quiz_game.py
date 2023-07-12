CATEGORIES = {
    1: 'history',
    2: 'science'
}

def main():
        welcome()
        selection = category_selection(CATEGORIES)
        print(CATEGORIES[selection])


def welcome():
        print("Welcome to Quiz Game! Use the number keys 1-4 to select your answer.")
        print("The game will consist of 4 random questions from the selected category.")
        print("Good luck!")

def category_selection(categories):
    for category in categories:
        print(f"Press {category} to answer {categories[category]} based questions.")

    while True:
        selection = input("Select Category: ")

        if selection == '1' or selection == '2':
            return int(selection)
        
        print("Enter a valid number to select a category.")

main()