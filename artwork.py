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
          

SMALL_FISH = ["""
   ___
|\\/  .\\
|/\\___/
""", 
"""
 ___
/.  \\/|
\\___/\\|
"""]

MEDIUM_FISH = ["""><(((@>""", 
               """<@)))><"""]
               
BIG_FISH = [
"""
       ,-.-,-,
     _/ / / /       /)
   ,'        `.   ,'')
 _/(@) `.      `./ ,')
(____,`  \\:`-.   \\ ,')
 (_      /::::}  / `.)
  \\    ,' :,-' ,)\\ `.)
   `.        ,')  `..)
     \\-....-'\\      \\)
      `-`-`-`-`
""",
"""
                                                           .
            ___---``````````````---____                  / |
       _--``   \)))))))))))))))))))))))`````___         /  |
    _-`` _       \))))))_-*|))))))))))))))))))))````---' __|
 _-``   / \       |))))|   |))))))))))))))))))))))))))/--  |
<___.   \_/       |))))|   |)))))))))))))))))))))))))<-    |
 ``-_             |))))|   |))))))))))))))))))))))))))\\--__|
    `_         /)))))) -_|)))))))))))))))))))))))___---.   |
       ``--__   /)))))))))))))))))))))))_____````       \\  |
            ````---______________---````                 \\ |
                                                           '
"""]     
      
FAT_FISH = [
"""
                  .-""L_                     
             ;`, /   ( o\                    
             \  ;    `, /                     
             ;_/"`.__.-"                       
""",
"""
               _J""-.
             /o )   \ ,';
             \ ,'    ;  /
              "-.__.'"\_;
      
"""]

PEOPLE = {
'Ellie': """
    .@@@@,
    aa`@@@,
    =  `@@@
       )_/`@'
      / || @
      | || @
      /~|| "`
     /__W__\\
       |||
      _|||
    ((___)
""",
'Mike': """
      ,,,,
     /   '
    /.. /
   ( c  D
    \- '\_
     `-'\)\\
        |_ \\
        |U \\\\
       (__,//
       |. \/
       LL__I
        |||
        |||
     ,,-``'\\
""",
'winning_smiley': """
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ *$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
*$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  ***$$$
   *$$$****$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     *$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     *$$$o
   o$$*   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$* *$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$*$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$********
 ****       $$$$    *$$$$$$$$$$$$$$$$$$$$$$$$$$$$*      o$$$
            *$$$o     ***$$$$$$$$$$$$$$$$$$*$$*         $$$
              $$$o          *$$**$$$$$$****           o$$$
               $$$$o                                o$$$*
                *$$$$o      o$$$$$$o*$$$$o        o$$$$
                  *$$$$$oo     **$$$$o$$$$$o   o$$$$**
                     **$$$$$oooo  *$$$o$$$$$$$$$***
                        **$$$$$$$oo $$$$$$$$$$
                                ****$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$*
                                      *$$$** 
""",
'correct_smiley': """
  _v_   _v_
   @    @
     ''
   \\____/ 
""",
}

PENGUINS = {
'big': """
       __
    -=(o '.
      '.-.\\
      /|  \\\\
      '|  ||
       _\\_):,_
""",
'eating': """
(o<)<
//\\
V_/_
""",
'fat': """
  (o_         
  //\\         
  V__)_
""",
'thin': """
  (o_         
  //|         
  V_|_
""",  
}

def print_picture(colour=None, thing=None):   
    '''thing is a string to be printed'''        
    if colour is None:
        colour = random.choice(list(COLOUR_MAP.keys()))
    if thing is None:
        thing = random.choice(SMALL_FISH)
    
    colour = colour.upper()
    
    colour = COLOUR_MAP.get(colour, Fore.WHITE)
    
    print (colour + thing)
    print(Fore.RESET)

def main():
    init()
    picture()
    deinit()

if __name__ == '__main__':
    main()