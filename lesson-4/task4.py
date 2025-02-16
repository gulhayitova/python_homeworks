from random import randint
def random_game():
    x = randint(1,101)
    for i in range(10):
        g = input("Guess: ")
        try:
            g = int(g)
        except ValueError:
            print("Please enter a valid number. ")
            continue
        if g == x:
            print("Your guess is correct!")
            break
        elif g > x:
            print("Too high.")
        elif g < x:
            print("Too low.")
        else:
            print("Incorrect input.")
    else:
        ans = input("You lost. Do you want to play again? ")
        if ans in ['yes','y','ok','Y','YES']:
            random_game()
random_game()
