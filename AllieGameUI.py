import random
import Cowsay

from AllieGameClass import AllieGame


def main():
    type = int(input("""Welcome to work, ALLIE!!! Choose some maths!

    1. Add

    2. Subtract

    3. Multiply

    """))

    # Can set the range here. Lets make it super hard for this demo
    game = AllieGame(0, 10)

    # game = AllieGame(0,6) #uncomment this

    if type == 1:
        game.AddGame()
    if type == 2:
        game.SubtractGame()
    if type == 3:
        game.MultiplyGame()
    else:
        Cowsay.trex(f"THATS NOT AN OPTION!!! >:( ")

    main()


if __name__ == "__main__":
    main()
