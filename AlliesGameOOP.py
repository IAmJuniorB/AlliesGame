from glob import glob
import random
from typing import Any
import shelve
from HighScore import score_list
import Cowsay

# "game" created for 4 y.o girl to practice maths. Simple addition and subtraction equations that never results in negative answers (such as -3). Can easily be tweaked for any age group.

class AlliesGame:
    in_a_row = 0  # Establish amount of correct answers in a row
    total_correct = 0  # Used to calculate amount of total correct answers
    medals = 0  # cause why not give out medals

    try:
        user_name = str(input("What is your name? ")
                        ).title().strip()  # get users name
        print(f"Welcome to work, {user_name}!!\n")

    except:
        print('empty string')

    def __init__(self):
        self.main()  # run the main method

    def main(self):
        try:
            difficulty = int(input(f"""Choose a difficulty!
1. Easy

2. Medium

3. Hard

Current high score: {self.get_high_score()}\n"""
                                   ))  # prompts user to choose what difficulty they would like to try

            if difficulty == 1:  # easy level
                self.level_one()

            elif difficulty == 2:  # medium level
                self.level_two()

            elif difficulty == 3:  # hard level
                self.level_three()

        except ValueError:
            print("Invalid input")
            self.main()  # prompts user again if incorrect input

    def get_high_score(self):
        # Default high score
        high_score = 0

    # Try to read the high score from a file
        try:
            high_score_file = open("high_score.txt", "r")
            high_score = int(high_score_file.read())
            high_score_file.close()
            print("The high score is", high_score)
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("No high score on file")

        return high_score

    def save_high_score(self):
        try:
            # high_score_dict = {self.user_name: self.total_correct}
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(self.total_correct))
            high_score_file.close()
            print(f"New high score: {self.total_correct}")
        except IOError:
            # can't write it.
            print("Unable to save the high score.")

    def top_three(self, name, score):
        self.name = name
        self.score = score
        self.high_score = high_score
        high_score = open("HighScore.py", "w")
        high_score.write(str({name: score}))

    def congratulations(self):
        # Congratulations message for correct answer
        character = Cowsay.char_names[random.randint(
            0, len(Cowsay.char_names) - 1)]
        print(Cowsay.get_output_string(
            character, f"""{self.user_name} is correct with {self.in_a_row} in a row and
            a total of {self.total_correct} correct!"""))

    def congratulations_2(self):
        self.medals += 1
        print(Cowsay.trex(f"""That's another 5 in a row! Here's a medal!
        Medals: {self.medals}"""))

    def add_total(self):
        self.total_correct += 1

    def in_a_row_method(self):
        self.in_a_row += 1

    def high_scores(self, user_name, high_score):
        self.high_score = high_score
        self.user_name = user_name
        high_score = 0
        updated_high_score = {self.user_name, self.total_correct}
        if self.total_correct > high_score:
            high_score = self.total_correct
            score_list(self.user_name, high_score)

    def level_one(self):

        # Addition equation
        while True:

            number_one = random.randint(0, 6)  # Random numbers for equation
            number_two = random.randint(0, 6)  # Random numbers for equation

            # 0 begins addition and 1 begins subtraction
            equation = random.randint(0, 1)

            if equation == 0:  # addition
                answer_one = number_one + number_two  # answer to equation

                try:
                    user_answered: int = int(
                        input(f"{number_one} + {number_two} = ?\n"))  # Prints equation requiring user input
                    if user_answered != answer_one:
                        self.in_a_row = 0  # resets how many correct in a row if answered incorrectly

                        user_answered: int = int(
                            input(f"{number_one} + {number_two} = ?\n"))  # reprints equation requiring user input if answered incorrectly
                    else:
                        self.in_a_row_method()  # Adds to the amount answered correctly without guessing wrong
                        self.add_total()
                        self.save_high_score()
                        self.high_scores(self.user_name, self.total_correct)
                        if self.in_a_row % 5 == 0:
                            self.congratulations_2()

                        else:
                            self.congratulations()  # congratulations message for correct answer
                            self.level_one()  # loops back to new question
                except ValueError:
                    print("Invalid input")

            else:  # Subtraction equation
                answer_one = number_one - number_two

                try:
                    while answer_one >= 0:  # prevents negative answers
                        user_answered = int(
                            input(f"{number_one} - {number_two} = ?\n"))
                        if user_answered != answer_one:
                            self.in_a_row = 0  # resets how many correct in a row if answered incorrectly
                            user_answered = int(
                                input(f"{number_one} - {number_two} = ?\n"))  # Repeats question if answered incorrectly
                        else:
                            self.in_a_row_method()  # Adds to the amount answered correctly without guessing wrong
                            self.add_total()
                            self.save_high_score()
                            self.high_scores(
                                self.user_name, self.total_correct)
                            if self.in_a_row % 5 == 0:
                                self.congratulations_2()

                            else:
                                self.congratulations()  # congratulations message for correct answer
                                self.level_one()  # loops back to new question
                    else:
                        self.level_one()  # asks another question if last question was negative
                except ValueError:
                    print("Invalid input")

    def level_two(self):
        # Addition equation
        while True:
            # Random numbers for equation
            number_one = random.randint(0, 3)
            number_two = random.randint(0, 2)
            number_three = random.randint(0, 3)
            # 0 begins addition and 1 begins subtraction
            equation = random.randint(0, 1)
            if equation == 0:
                answer_one = number_one + number_two + number_three
                try:
                    user_answered = int(
                        input(f"{number_one} + {number_two} + {number_three} = ?\n"))
                    while user_answered != answer_one:
                        user_answered = int(
                            input(f"{number_one} + {number_two} + {number_three} = ?\n"))
                    if answer_one == user_answered:
                        self.congratulations()
                        continue
                except ValueError:
                    print("Invalid input")
            # Subtraction equation
            else:
                answer_one = number_one - number_two + number_three
                try:
                    user_answered = int(
                        input(f"{number_one} - {number_two} + {number_three} = ?\n"))
                    while user_answered != answer_one:
                        user_answered = int(
                            input(f"{number_one} - {number_two} + {number_three}= ?\n"))
                    # Congratulations message if correct
                    self.congratulations()
                    continue
                except ValueError:
                    print("Invalid input")

    def level_three(self):

        # Multiplication
        while True:
            # Random numbers for equation
            number_one = random.randint(0, 2)
            number_two = random.randint(0, 2)
            answer_one = number_one * number_two
            try:
                user_answered = int(
                    input(f"{number_one} X {number_two} = ?\n"))
                if user_answered == answer_one:
                    self.congratulations()
                    continue
            except ValueError:
                print("Invalid input")
            else:
                try:
                    user_answered = int(
                        input(f"{number_one} X {number_two} = ?\n"))
                    # Congratulations message if correct
                    self.congratulations()
                    continue
                except ValueError:
                    print("Invalid input")


if __name__ == "__main__":
    AlliesGame()
