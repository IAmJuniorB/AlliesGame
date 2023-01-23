import random
import cowsay


class AllieGame:

    # Initialize class. This sets the minimum and maximum values, that way these values can be used anywhere through the class
    def __init__(self, min, max):
        self.min = min
        self.max = max

    # This is made to be easily modified in the future, and also so we don't repeat this anytime we want to add a different game mode
    def SetNumberValues(self):
        self.num1 = self.GetRandomNum()
        self.num2 = self.GetRandomNum()

    # Set the win logic as a seperate function that way it is easily modified in the future. Can also change its behavior much easier. Optional.
    def Win(self, answer):
        cowsay.get_output_string(cowsay.char_names[random.randint(0, len(
            cowsay.char_names) - 1)], f"Number {answer} is correct!!! ALLIE IS A WINNER!!!!")

    # Add Game
    def AddGame(self):
        # Set the numbers every time the game starts
        self.SetNumberValues()
        # Logic for addition, prompt generation
        correctAnswer = self.num1 + self.num2
        prompt = "{} + {} = ? ".format(self.num1, self.num2)
        # Throw the answer and prompt into the game loop.
        self.GameLoop(prompt, correctAnswer)
        # Restart when over, or change this to something else
        self.AddGame()

    # Subtract Game
    def SubtractGame(self):
        self.SetNumberValues()
        if self.num1 - self.num2 < 0:
            temp = self.num1
            self.num1 = self.num2
            self.num2 = temp

        correctAnswer = self.num1 - self.num2
        prompt = "{} - {} = ? ".format(self.num1, self.num2)
        self.GameLoop(prompt, correctAnswer)
        self.SubtractGame()

    # Multiply Game
    def MultiplyGame(self):
        self.SetNumberValues()
        correctAnswer = self.num1 * self.num2
        prompt = "{} * {} = ? ".format(self.num1, self.num2)
        self.GameLoop(prompt, correctAnswer)
        self.MultiplyGame()

    # Core game loop.
    def GameLoop(self, prompt, answer):
        while int(input(prompt)) != answer:
            continue
        self.Win(answer)

    # Gets a random number with the restraints set in the class creation
    def GetRandomNum(self):
        return random.randint(self.min, self.max)
