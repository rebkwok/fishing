import random
import artwork
from colorama import init, deinit
from colorama import Fore, Back, Style

init(autoreset=True)
NUM_QUESTIONS = 3
                 
class Game(object):
    
    def __init__(self):
        self.level = 1
        self.player = ""
        self.level_score = 0
        
        self.ACTION_MAP = {1 : ["+", self.add, "magenta", artwork.SMALL_FISH],
                  2 : ["-", self.subtract, "cyan", artwork.MEDIUM_FISH],
                  3 : ["x", self.multiply, "yellow", artwork.FAT_FISH],
                  4 : ["/", self.divide, "red", artwork.BIG_FISH]
                 }
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
            
    def choose_player(self):
        initial = input("Choose your player.\n\nEnter E for Ellie or M for Mike\n")
        initial = initial.upper()
        players = {'E': 'Ellie',
                   'M': 'Mike'}
        self.player = players[initial]
        print()
        print("You are {}!".format(self.player))
        artwork.print_picture(thing=artwork.PEOPLE[self.player])
        
        print("Here is your companion, Pingy Penguin!")
        artwork.print_picture(thing=artwork.PENGUINS['big'])
    
    def play_level(self):
        print(Back.RED + Fore.YELLOW + "LEVEL {}".format(self.level))
        print()
        input("Press enter to start.")

        action_symbol = self.ACTION_MAP[self.level][0] 
        action = self.ACTION_MAP[self.level][1]
               
        for i in range(1, NUM_QUESTIONS + 1):
            
            self._catch_fish()
            
            number1 = random.choice(range(1, 11))
            number2 = random.choice(range(1, 11))
 
            question = str(number1) + " " + action_symbol + " " + str(number2) + " = ?\n"
            question_title = "Question " + str(i)
            print(Back.YELLOW + Fore.BLUE + Style.BRIGHT + question_title) 
            sum_answer = input(question)

            try:
                if int(sum_answer) == action(number1, number2):
                    print('Correct!')
                    artwork.print_picture(thing=artwork.PEOPLE["correct_smiley"])
                    self.level_score = self.level_score + 1
                else:
                    print('Incorrect! The right answer is', number1 + number2)
                    print('Pingy eats your fish!')
                    artwork.print_picture(thing=artwork.PENGUINS["eating"])
                    print('Pingy is stuffed!')
                    artwork.print_picture(thing=artwork.PENGUINS["fat"])
            except ValueError:
                print('Incorrect! The right answer is', number1 + number2)
                print('Incorrect! The right answer is', number1 + number2)
                print('Pingy eats your fish!')
                artwork.print_picture(thing=artwork.PENGUINS["eating"])
                print('Pingy is stuffed!')
                artwork.print_picture(thing=artwork.PENGUINS["fat"])
            print()
            if i < NUM_QUESTIONS:
                input("Press enter to fish for the next question.\n")
            
        if self.level_score == NUM_QUESTIONS:
            print("PERFECT SCORE! YOU PASSED LEVEL {}!".format(self.level))
            artwork.print_picture(thing=artwork.PEOPLE["winning_smiley"])
        
        if self.level < 4:
            self.level += 1
            self.level_score = 0
            self.play_level()
        
    def _catch_fish(self):
            
        print("{} goes fishing!\n".format(self.player))
        artwork.print_picture(colour=self.ACTION_MAP[self.level][2], 
                              thing=self.ACTION_MAP[self.level][3][random.choice([0, 1])])
        
    
game = Game()
print("\n\n\n")
print(Back.RED + Fore.YELLOW + "==========================================")
print(Back.RED + Fore.YELLOW + "WELCOME TO HOLLY'S MATHS AND FISHING GAME!")
print(Back.RED + Fore.YELLOW + "==========================================")
print("\n\n")

game.choose_player()
game.play_level()

deinit()
