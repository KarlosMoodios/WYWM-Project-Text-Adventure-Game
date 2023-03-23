# Reclaim Camelot Castle textRPG
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
        self.gender = ''
        self.hp = 100
        self.mp = 100
        self.inv = 10
        self.status_effects = []
        self.loc = 'c0'
        self.game_over = False
player1 = player()

# Title Screen
def title_screen_selections():
    option = input('> ')
    option = option.lower().strip()
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
    os.system('cls')
    print('------------------------------------------')
    print('Welcome to Knights of the round table RPG!')
    print('------------------------------------------')
    print('                 - Play -                 ')
    print('                 - Help -                 ')
    print('                 - Quit -                 ')
    print('     - Copyright 2023 KarlosMoodios -     ')
    title_screen_selections()

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
# '''
#   a  b  c  d  e
# -----------------
# |  |  |  |  |  |  1
# -----------------
# |  |  |  |  |  |  2
# -----------------
# |  |  |  |  |  |  3
# -----------------
# |  |  |  |  |  |  4
# -----------------
# |  |  |  |  |  |  5
# -----------------
# '''

ROOMNAME = ''
DESCRIPTION = 'describe'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south' 
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_rooms = {              'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False, 'a5' : False, 
                              'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False, 'b5' : False,
                'c0' : False, 'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False, 'c5' : False,
                              'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False, 'd5' : False,
                              'e1' : False, 'e2' : False, 'e3' : False, 'e4' : False, 'e5' : False, }

room_map = {
    'a1' : {
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Castle gardens - Two water fountains with a path leading through the middle of them and round to the south,\n
        the water in these fountains glows an almost magical sparkle as the water shoots out from one, over your head\n
        into the other and back again.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'a2',
        LEFT: '',
        RIGHT: 'b1',
    },
    'a2' : { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''You can see the path continues to the south, right up to the fence. On your left, 
        against the castle wall are a series of support pillars that run the length of the castle wall each with 
        window covered by a horn pane situated between them, in the soil below are some sunflowers. You can 
        continue south or head back the way you came''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'a3',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'a3': { 
        ROOMNAME: 'Castle gardens - Front Gate',
        DESCRIPTION: '''Gardens - In this part of the garden there are two benches looking onto charred ground, 
        what looks like it was once a flower bed; I wonder why only the flower bed is charred. In the center 
        of the flower bed stands a tall statue of a King, though no inscription is present. Behind the northern 
        bench the horn pane over the window looks loose enough to pry it open with your sword.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'a4',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'a4': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Gardens / Cellar Entrance - In the overgrown grass of the gardens I can see what looks like 
        a cellar door buried by some debris, I'll need to find some tools to clear this if i want to gain access through here''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up', 
        DOWN: 'a5',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'a5': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Gardens - At the end of the path is another water fountain, functional but not completely. 
        Water just trickling out of the top and dribbling down the sides. It's almost as if there's a blockage somewhere.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4', 
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
    },
    'b1': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Castle gardens - Two large flower beds sown into the garden either side of the path, 
        both have lively looking plants that seem to be growing well, the soil looks rich with nutrients 
        as if someone has tended these patches recently, strange...''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'a1',
        RIGHT: 'c1',
    },
    'b2': { 
        ROOMNAME: 'West Tower',
        DESCRIPTION: '''West Tower - Ladder Up, The bottom of the western tower. 
        There are some armour stands in here with armour on them. Some pieces are missing from the suits. 
        Along the wall there is a bow rack, there's room enough for four bows, only one bow is present 
        and it has a snapped string. 
        There are 4 empty quivers on the table below the bow rack.''',# ladder needs mentioning
        EXAMINATION: 'Your quarters look the same, nothing has changed',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: '',
        RIGHT: '', 
    },
    'b3': { 
        ROOMNAME: 'West Tower Passage',
        DESCRIPTION: '''West Tower Passage -  an almost empty halllway leading to the tower on the west side of the castle. 
        There is a stool and a small table along the western wall and a huge crested shield hanging on the wall above it 
        along the eastern wall are oil lamps and horn paned windows looking out into what must be the courtyard.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'b4',
        LEFT: '',
        RIGHT: '', 
    },
    'b4': { 
        ROOMNAME: 'Kitchen / Cellar Entrance',
        DESCRIPTION: '''Kitchen / Cellar Entrance - a large kitchen big enough to prepare 
        a feast for at least 13 people each and every time. a large table covered in surface 
        slits in the center of the room, presumably where they carved up their food. 
        Along the northern wall sits a large open floor fire with a spitroast above. 
        Shelves all around the room with large barrels lain on their side and little wooden 
        pegs jammed in the tops of them. This must be where the ale was kept too! In the back 
        corner of the room is a cellar door which is locked tight. 
        There is a key hole, so maybe there is a key.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'b5': { 
        ROOMNAME: 'Trophy Room',
        DESCRIPTION: '''Trophy Room - What looks like a trophy room. There are skulls of fallen behemoth-like 
        creatures sitting around the room. A huge dragon shaped head hanging from the wall. 
        If only there was someone I could talk with about these who knows the story of their origin.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'c0': { 
        ROOMNAME: 'Start',
        DESCRIPTION: '''After a long climb you reach the top of the hill, you finally arrive at what 
        you suspect to be the Castle of Camelot. It seems to be in good shape and looks safe to enter. 
        The castle is surrounded by an 8ft tall weathered iron fence, however, it seems to be as 
        sturdy as it was the day it was built. Would you like to enter? (yes/no) You try the latch 
        on the gate and its rusted solid; you take your hammer and give it a good swing down on the latch, 
        breaking it free just enough to open the gate.''',
        EXAMINATION: '''After a long climb you reach the top of the hill, you finally arrive at what 
you suspect to be the Castle of Camelot. It seems to be in good shape and looks safe to enter. 
The castle is surrounded by an 8ft tall weathered iron fence, however, it seems to be as 
sturdy as it was the day it was built. Would you like to enter? (yes/no) You try the latch 
on the gate and its rusted solid; you take your hammer and give it a good swing down on the latch, 
breaking it free just enough to open the gate.''',
        SOLVED: False,
        UP: '',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: '', 
    },
    'c1': { 
        ROOMNAME: 'Castle gardens / Front gate',
        DESCRIPTION: '''Castle Gardens - A once mighty iron gate now rusted and creeks as it opens. \n
        You enter through the front gate it slams shut behind you. you notice either side of the path 2 statue plinths, \n
        one of them with the statue of a mighty looking king atop and a plaque that reads "Arthur - King of the Britons, \n
        the other has a broken statue, a damaged plaque with an unreadable inscription and the resemblance of mangled \n
        iron platemail lay beside it on the ground. \n
        The path before you splits into three directions: East, south and west.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
    },
    'c2': { 
        ROOMNAME: 'Courtyard Entrance',
        DESCRIPTION: '''Courtyard Entrance - Either side of the door there are 2 huge support pillars reaching 
        way up to the top of the towers on each side of the entrance. Both have ivy growing up them. If thats 
        not kept in check it could cause structural damage to the castle. Through the archway you can see a 
        large fountain. Each layer of the fountain bears the shape of a crown, definitely fit for a king!''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'c3': { 
        ROOMNAME: 'Castle courtyard',
        DESCRIPTION: '''There is a huge, empty water fountain in the center and flower beds all around the perimeter 
        of the courtyard. The flower beds are full of life. There are horn paned windows all around and a huge 
        wooden door with iron trimmings and bronze handles. The windows all look sealed shut and the door is closed. 
        Would you like to enter the door? (yes/no) 
        The door is barred from the inside, maybe you can find another way in?''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'c4': { 
        ROOMNAME: 'Main Hall',
        DESCRIPTION: '''What a sight, the table where Arthur and his 12 knights conferred about their adventures. 
        The table looks strong! As you wipe away the thick layer of dust coating the table you can see the 
        inscriptions of each knights name in the table as a placeholder for where they each sat. Many a feast 
        must have been eaten at this table and ale drunk too.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'c5': { 
        ROOMNAME: 'Staircase',
        DESCRIPTION: '''A grand staircase leads up to the top floor of the castle, the stairs look to be in great shape.
        The banister rails not so much. The knights' living quarters must be up there.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd1': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Gardens - The small flower bed to the north has soil 
        that looks like clay and definitely hasn\'t been tended to in a while. 
        Surpirsingly there is life in the flowers here however they do seem to be dying out. 
        The larger flower bed to the south looks much the same however there are no flowers in this 
        flower bed and the soil looks to have been dug out; you suspect long ago as the mound of excavated soil 
        is compact from where the rain has fallen on it over the years.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd2': { 
        ROOMNAME: 'East tower',
        DESCRIPTION: '''A Ladder in the back of the room that goes down goes to the dungeons and up through the tower, 
        the ladder down has rotted and theres no way down, however, the ladder going up seems sturdy. The are a number of 
        empty wall torch brackets around the room. Only one has a torch and it's unlit. Do you want to take the torch? (yes/no)''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd3': { 
        ROOMNAME: 'East Tower Passage',
        DESCRIPTION: '''East Tower Passage - a passage filled with empty barrels and crates. 
        Empty torch hangings on the walls and sealed windows. Must be a storage room of sorts. 
        Either that or it was barricaded. There is room to just about clamber through to the 
        other side to get to the east tower. ''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'd4': { 
        ROOMNAME: 'Armoury',
        DESCRIPTION: '''The armoury! Shame there are no armour or weapons in here though! Just empty 
        armour stands surrounding the edge of the room. Cobwebs reach from armour stand to armour stand, 
        built by spiders that are nowhere to be seen. This room hasn't be disturbed in a long time.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'd5': { 
        ROOMNAME: 'Blacksmith',
        DESCRIPTION: '''The coldest room in the building, once the hottest. There sits a great forge at 
        the back of the room, with a chimney that goes directly out the roof. The coal chamber beside it 
        filled half full with coal. Sitting on one of the anvils an unfinished sword. Whomever left here 
        did so in a hurry. There's a bucket of oil beside the furnace which has been covered with a plank of wood.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'e1': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Two water fountains are in this corner of the gardens, both filled 
        with thick green algae sludgey water, though there is a slight breeze, the surface of the 
        water remain perfectly, eerily still. One of them has a crack running from the top of the 
        fountain feature to its base and the water level is lower than the other fountain. The path 
        here ends at the fountains. Against the fenceline of the castle are two benches both rotten, 
        in need of repair and sinking into the boggy grass.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'e2': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Gardens - The grass along this side of the castle is very boggy. There are support 
        pillars along the length of the castle wall, with windows covered by horn panes. there are no 
        flowers or flower beds, and a lot of moss growing across the ground. Best to watch your footing.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'e3': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Gardens - More boggy grass, still nothing of interest in the immediate area. 
        You can see something sticking out of the ground at the end of the garden.''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right', 
    },
    'e4': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Gardens - The ground gets significantly more boggy here. As you approch the end of the garden you 
        can see more clearly the shape of a hand sticking out of the mud. Specifically an iron gauntlet reaching upwards. 
        It might be too dangerous to step onto that part of the garden, Are you sure you want to proceed? (yes/no)''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
    'e5': { 
        ROOMNAME: 'Castle gardens',
        DESCRIPTION: '''Gardens - bog of death, for every second the player enters this room they will lose 5 hp. 
        If the player dies They will be reset to inside the Front Gate. 
        You start to sink! now its clear that the gauntlet once belonged to an adventurer. you better get out of here fast''',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up',
        DOWN: 'down',
        LEFT: 'left',
        RIGHT: 'right',
    },
}

# Game interactivity
# Function to notify player of location and description
def print_location():
    print('\n' + ('-' * (4 + len(player.loc))))
    print(' - ' + len(player.loc + ' - '))
    print(' - ' + room_map[player1.position][DESCRIPTION] + ' - ')
    print('\n' + ('-' * (4 + len(player.loc))))

# Function to prompt player for input
def prompt():
    print('\n----------------------------')
    print('\n What would you like to do?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print('You cannot do that, try again')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

# Function to move the player through the map
def player_move(myAction):
    ask = 'Where would you like to move?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = room_map[player1.loc][UP]
        movement(destination)
    elif dest in ['down', 'south']:
        destination = room_map[player1.loc][DOWN]
        movement(destination)
    elif dest in ['left', 'west']:
        destination = room_map[player1.loc][LEFT]
        movement(destination)
    elif dest in ['right', 'east']:
        destination = room_map[player1.loc][RIGHT]
        movement(destination)

# Function for movement handling
def movement(destination):
    print('You have moved to the ' + destination + '.')
    player1.loc = destination

def player_examine(action):
    if room_map[player1.loc][SOLVED]:
        print('This room has been completed already')
    else:
        print(room_map[player1.loc][EXAMINATION])

# Game functionality
def main():
    while player1.game_over is False:
        prompt()

def ai_chat(question):
    q = question
    for c in q:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

# AI dialogue
QUESTION = '', '' + player1.name + '', '' + player1.gender + '' 
ai_dialogue = {
    'q1': {QUESTION:'Would you like to reclaim Camelot? (yes/no)\n'},
    'q2': {QUESTION:'Welcome to Camelot Castle! Whats is your name?\n'},
    'q3': {QUESTION:'What is your gender? (Male/Female/Anything)\n'},
    'q4': {QUESTION:'Would you like to play solo or as a team (AI)'},
    'q5': {QUESTION:'Lets create some knights for your round table!\n'},
    'q6': {QUESTION:'Enter the name of your 1st Knight:\n'},
    'q7': {QUESTION:'Enter the name of your 2nd Knight:\n'},
    'q8': {QUESTION:'Enter the name of your 3rd Knight:\n'},
    'q9': {QUESTION:'Please enter a valid name.\n'},
    'q10': {QUESTION:'\n'},
    'q11': {QUESTION:'\n'},
    'q12': {QUESTION:'\n'},
    'q13': {QUESTION:'\n'},
    'q14': {QUESTION:'\n'},
    'q15': {QUESTION:'\n'},
    'q16': {QUESTION:'\n'},
    'q17': {QUESTION:'\n'},
    'q18': {QUESTION:'\n'},
    'q19': {QUESTION:'\n'},
    'q20': {QUESTION:'\n'},
    'q21': {QUESTION:'Your chosen knight names are: \n'},
    'q22': {QUESTION:'Good luck on your adventure!\n'},
}

def start_game():
    
    os.system('cls')

    ai_chat(ai_dialogue['q1'][QUESTION])
    ans = input('> ')
    if ans.strip().lower() == 'yes':
        round_table = 12
        knights_count = 0
        knight_list = []

        ai_chat(ai_dialogue['q2'][QUESTION])
        player1.name = input('> ')
        ai_chat(ai_dialogue['q3'][QUESTION])
        player1.gender = input('> ') 
        if player1.gender.strip().lower() == 'male':
            player1.gender = 'King'
        elif player1.gender.strip().lower() == 'female' :
            player1.gender = 'Queen'
        else:
            player1.gender = player1.gender
        greet_msg = 'Greetings ' + player1.gender + ' ' + player1.name + '!\n'
        ai_chat(greet_msg)
        time.sleep(1)
        ai_chat(ai_dialogue['q4'][QUESTION])
        solo_coop = input('> ')
        if solo_coop.strip().lower() == 'coop':
            ai_chat(ai_dialogue['q5'][QUESTION])
            while knights_count < round_table:
                if knights_count == 0:
                    ai_chat(ai_dialogue['q6'][QUESTION])
                    name = input('> Sir: ')
                    if name == "":
                        ai_chat(ai_dialogue['q9'][QUESTION])
                        knights_count -= 1
                    else:
                        knight_list.append('Sir ' + name)

                elif knights_count == 1:
                    ai_chat(ai_dialogue['q7'][QUESTION])
                    name = input('> Sir: ')
                    if name == "":
                        ai_chat(ai_dialogue['q9'][QUESTION])
                        knights_count -= 1
                    else:
                        knight_list.append('Sir ' + name)

                elif knights_count == 2:
                    ai_chat(ai_dialogue['q8'][QUESTION])
                    name = input('> Sir: ')
                    if name == "":
                        ai_chat(ai_dialogue['q9'][QUESTION])
                        knights_count -= 1
                    else:
                        knight_list.append('Sir ' + name)

                elif knights_count < round_table:
                    n = str(knights_count + 1)
                    ai_chat('Enter the name of your '+ n + 'th Knight: \n')
                    name = input('> Sir: ')
                    if name == "":
                        ai_chat(ai_dialogue['q9'][QUESTION])
                        knights_count -= 1
                    else:
                        knight_list.append('Sir ' + name)   
                knights_count += 1
                n = str(knights_count)
                if knights_count == 1:
                    ai_chat("You have " + n + " Knight at the round table.\n")
                else:
                    ai_chat("You have " + n + " Knights at the round table.\n")
            ai_chat(ai_dialogue['q21'][QUESTION])
            for x in knight_list:
                sys.stdout.write(x)
                sys.stdout.write(', ')
                sys.stdout.flush()
                time.sleep(0.5)
            print('\n')
            #  End of choosing Knight names

    else:
        ai_chat(ai_dialogue['q9'][QUESTION])
    
    os.system('cls')
    ai_chat(ai_dialogue['q22'][QUESTION])
    main()


title_screen()


