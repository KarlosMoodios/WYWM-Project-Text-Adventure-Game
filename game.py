# Knights of the round table RPG
# Created by Karl Moody

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# Player 
class player:
    def __init__(self):
        self.name = ''
        self.hp = 100
        self.mp = 100
        self.sp = 100
        self.gold = 50
        self.inv = 20
        self.status_effects = []
        self.loc = 'start'    
Player1 = player()

# Title Screen
def title_screen():
    option = input('> ')
    if option.lower() == ('play'):
        start_game() # Needs writing
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter an option')
        option = input('> ')
        if option.lower() == ('play'):
            start_game() # Needs writing
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('clear')
    print('------------------------------------------')
    print('Welcome to Knights of the round table RPG!')
    print('------------------------------------------')
    print('                 - Play -                 ')
    print('                 - Help -                 ')
    print('                 - Quit -                 ')
    print('     - Copyright 2023 KarlosMoodios -     ')
    title_screen()

def help_menu():
    print('------------------------------------------')
    print('Welcome to Knights of the round table RPG!')
    print('------------------------------------------')
    print('     - To move, use the arrow keys -      ')
    print('  - Type the commands to exectute them -  ')
    print('    - Use \'Look\' to inspect something -   ')
    print('              - Good luck! -              ')
    title_screen()

# Game map
'''
 x1 x2 x3 x4
-------------
|  |  |  |  | y1
-------------
|  |  |  |  | y2
-------------
|  |  |  |  | y3
-------------
|  |  |  |  | y4
-------------

'''
ROOMNAME = ''
DESCRIPTION = 'describe'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south' 
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_rooms = {'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False, 
                'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False,
                'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False,
                'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False, }

room_map = {
    'a1' : {
        ROOMNAME: 'Western courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2' : { 
        ROOMNAME: 'West-central courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'a3': { 
        ROOMNAME: 'East-central courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'a4': { 
        ROOMNAME: 'Eastern courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up', 
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'b1': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'b2': { 
        ROOMNAME: 'Kings quarters',
        DESCRIPTION: 'Home sweet home',
        EXAMINATION: 'Your quarters look the same, nothing has changed',
        SOLVED: False,
        UP: 'x2y1',
        DOWN: 'x2y3',
        LEFT: '',
        RIGHT: '', 
    },
    'b3': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'b4': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c1': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'c2': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'c3': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'c4': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd1': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd2': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd3': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd4': { 
        ROOMNAME: 'Courtyard',
        DESCRIPTION: 'describe',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    
}

# Game interactivity
def print_location():
    print('\n' + ('-' * (4 + len(player.loc))))
    print(' - ' + len(player.loc + ' - '))
    print('\n' + ('-' * (4 + len(player.loc))))

def prompt():
    print('\n----------------------------')
    print('\n What would you like to do?')

# Game functionality
def start_game():
    return






