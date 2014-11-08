from colorama import init, deinit
from colorama import Fore, Back, Style
import random


COLOUR_MAP = {'RED': Fore.RED,
              'GREEN': Fore.GREEN,
              'BLUE': Fore.BLUE,
              'YELLOW': Fore.YELLOW,
              'MAGENTA': Fore.MAGENTA,
              'CYAN': Fore.CYAN,
          }
          
          
def fish(index=None, colour=None):           
    if index is None:
        index = random.choice([0, 1])
    if colour is None:
        colour = random.choice(list(COLOUR_MAP.keys()))
    
    colour = colour.upper()
    
    colour = COLOUR_MAP.get(colour, Fore.WHITE)
    
    FISH_PICS = [
        '''
        |><>
        ''',
        '''
        <><|
        '''
    ]
    
    print (colour + FISH_PICS[index])
    print(Fore.RESET)

def main():
    init()
    fish()
    deinit()

if __name__ == '__main__':
    main()