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
    ai_chat(dia['q13'][Q], s['s0'][S])
    ai_chat(dia['q14'][Q], s['s0'][S])
    ai_chat(dia['q13'][Q], s['s0'][S])
    ai_chat(dia['q15'][Q], s['s0'][S])
    ai_chat(dia['q16'][Q], s['s0'][S])
    ai_chat(dia['q17'][Q], s['s0'][S])
    ai_chat(dia['q18'][Q], s['s0'][S])
    ai_chat(dia['q19'][Q], s['s2'][S])
    title_screen_selections()

def help_menu():
    os.system('cls')
    ai_chat(dia['q13'][Q], s['s0'][S])
    ai_chat(dia['q14'][Q], s['s0'][S])
    ai_chat(dia['q13'][Q], s['s0'][S])
    ai_chat(dia['q20'][Q], s['s0'][S])
    ai_chat(dia['q21'][Q], s['s0'][S])
    ai_chat(dia['q22'][Q], s['s0'][S])
    ai_chat(dia['q23'][Q], s['s0'][S])
    ai_chat(dia['q26'][Q], s['s0'][S])
    done = input('> ')
    if done.strip().lower() == 'yes':
        title_screen()
    else: 
        help_menu()

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

ROOMNAME = 'locate'
EXAMINATION = 'examine'
DESCRIPTION = 'describe'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
FLOOR = 'use'

solved_rooms = {              'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False, 'a5' : False, 
                              'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False, 'b5' : False,
                'c0' : False, 'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False, 'c5' : False,
                              'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False, 'd5' : False,
                              'e1' : False, 'e2' : False, 'e3' : False, 'e4' : False, 'e5' : False, }

room_map = {
    'a1' : {
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Castle gardens - Two water fountains with a path leading through the middle of them and round to the south,\n
the water in these fountains glows an almost magical sparkle as the water shoots out from one, over your head\n
into the other and back again.''',
        DESCRIPTION: 'The northwest corner in the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: 'a2',
        LEFT: '',
        RIGHT: 'b1',
    },
    'a2' : { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''You can see the path continues to the south, right up to the fence. On your left, 
against the castle wall are a series of support pillars that run the length of the castle wall each with 
window covered by a horn pane situated between them, in the soil below are some sunflowers. You can 
continue south or head back the way you came''',
        DESCRIPTION: 'South of the northwest corner in the castle gardens.',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'a3',
        LEFT: '',
        RIGHT: '', 
    },
    'a3': { 
        ROOMNAME: 'Castle gardens - Front Gate',
        EXAMINATION: '''Gardens - In this part of the garden there are two benches looking onto charred ground, 
what looks like it was once a flower bed; I wonder why only the flower bed is charred. In the center 
of the flower bed stands a tall statue of a King, though no inscription is present. Behind the northern 
bench the horn pane over the window looks loose enough to pry it open with your sword.''',
        DESCRIPTION: 'Halfway between the northwest and southwest corners in the castle gardens.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'a4',
        LEFT: '',
        RIGHT: '',
    },
    'a4': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Gardens / Cellar Entrance - In the overgrown grass of the gardens I can see what looks like 
a cellar door buried by some debris, I'll need to find some tools to clear this if i want to gain access through here''',
        DESCRIPTION: 'North of the southwest corner in the castle gardens.',
        SOLVED: False,
        UP: 'a3', 
        DOWN: 'a5',
        LEFT: '',
        RIGHT: 'c5', 
    },
    'a5': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Gardens - At the end of the path is another water fountain, functional but not completely. 
Water just trickling out of the top and dribbling down the sides. It's almost as if there's a blockage somewhere.''',
        DESCRIPTION: 'The southwest corner of the castle gardens.',
        SOLVED: False,
        UP: 'a4', 
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
    },
    'b1': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Castle gardens - Two large flower beds sown into the garden either side of the path, 
both have lively looking plants that seem to be growing well, the soil looks rich with nutrients 
as if someone has tended these patches recently, strange...''',
        DESCRIPTION: 'East of the northwest corner of the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'a1',
        RIGHT: 'c1',
    },
    'b2': { 
        ROOMNAME: 'West Tower',
        EXAMINATION: '''West Tower - Ladder Up, The bottom of the western tower. 
There are some armour stands in here with armour on them. Some pieces are missing from the suits. 
Along the wall there is a bow rack, there's room enough for four bows, only one bow is present 
and it has a snapped string. 
There are 4 empty quivers on the table below the bow rack.
You can see a ladder leading up through the tower.''',
        DESCRIPTION: 'The ground floor of the western tower inside the castle.',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: '',
        RIGHT: '',
        FLOOR: 'b6', # need to build upper floor map
    },
    'b3': { 
        ROOMNAME: 'West Tower Passage',
        EXAMINATION: '''West Tower Passage -  an almost empty halllway leading to the tower on the west side of the castle. 
There is a stool and a small table along the western wall and a huge crested shield hanging on the wall above it 
along the eastern wall are oil lamps and horn paned windows looking out into what must be the courtyard.''',
        DESCRIPTION: 'A passage leading from the trophy room to the west tower.',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'b4',
        LEFT: '',
        RIGHT: '', 
    },
    'b4': { 
        ROOMNAME: 'Trophy Room',
        EXAMINATION: '''Trophy Room - What looks like a trophy room. There are skulls of fallen behemoth-like 
creatures sitting around the room. A huge dragon shaped head hanging from the wall. 
If only there was someone I could talk with about these who knows the story of their origin.''',
        DESCRIPTION: 'A room full of age old trophies.',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'b5',
        LEFT: '',
        RIGHT: 'c4',
    },
    'b5': { 
        ROOMNAME: 'Staircase',
        EXAMINATION: '''A grand staircase leads up to the top floor of the castle, the stairs look to be in great shape.
The banister rails not so much. The knights' living quarters must be up there.''',
        DESCRIPTION: 'An room with an old staircase.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
        FLOOR: 'b7', # needs creating
    },
    'c0': { 
        ROOMNAME: '            - Start -\n',
        EXAMINATION: '''After a long climb you reach the top of the hill, you finally arrive at what 
you suspect to be the Castle of Camelot. It seems to be in good shape and looks safe to enter. 
The castle is surrounded by an 8ft tall weathered iron fence, however, it seems to be as 
sturdy as it was the day it was built. Would you like to enter? (yes/no) You try the latch 
on the gate and its rusted solid; you take your hammer and give it a good swing down on the latch, 
breaking it free just enough to open the gate.''',
        DESCRIPTION: 'The entrance to the castle grounds.',
        SOLVED: False,
        UP: '',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: '', 
    },
    'c1': { 
        ROOMNAME: 'Castle gardens / Front gate',
        EXAMINATION: '''Castle Gardens - A once mighty iron gate now rusted and creeks as it opens. \n
You enter through the front gate it slams shut behind you. you notice either side of the path 2 statue plinths, \n
one of them with the statue of a mighty looking king atop and a plaque that reads "Arthur - King of the Britons, \n
the other has a broken statue, a damaged plaque with an unreadable inscription and the resemblance of mangled \n
iron platemail lay beside it on the ground. \n
The path before you splits into three directions: East, south and west.''',
        DESCRIPTION: 'Inside the front gate of the castle grounds.',
        SOLVED: False,
        UP: '',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'd1', 
    },
    'c2': { 
        ROOMNAME: 'Courtyard Entrance',
        EXAMINATION: '''Courtyard Entrance - Either side of the arch are 2 huge support pillars reaching 
way up to the top of the towers on each side of the entrance. Both have ivy growing up them. If thats 
not kept in check it could cause structural damage to the castle. Through the archway you can see a 
large fountain. Each layer of the fountain bears the shape of a crown, definitely fit for a king!''',
        DESCRIPTION: 'An arch shaped tunnel leading into the courtyard of the castle.',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'c3',
        LEFT: '',
        RIGHT: '',
    },
    'c3': { 
        ROOMNAME: 'Castle courtyard',
        EXAMINATION: '''There is a huge, empty water fountain in the center and flower beds all around the perimeter 
of the courtyard. The flower beds are full of life. There are horn paned windows all around and a huge 
wooden door with iron trimmings and bronze handles. The windows all look sealed shut and the door is closed. 
Would you like to enter the door? (yes/no) 
The door is barred from the inside, maybe you can find another way in?''',
        DESCRIPTION: 'A beautiful courtyard filled with statues, flowers and a fountain.',
        SOLVED: False,
        UP: 'c2',
        DOWN: 'c4',
        LEFT: '',
        RIGHT: '', 
    },
    'c4': { 
        ROOMNAME: 'Main Hall',
        EXAMINATION: '''What a sight, the table where Arthur and his 12 knights conferred about their adventures. 
The table looks strong! As you wipe away the thick layer of dust coating the table you can see the 
inscriptions of each knights name in the table as a placeholder for where they each sat. Many a feast 
must have been eaten at this table and ale drunk too.''',
        DESCRIPTION: 'A great hall with a large round table situated right in the center of the floor.',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'c5',
        LEFT: 'b4',
        RIGHT: 'c4', 
    },
    'c5': { 
        ROOMNAME: 'Kitchen / Cellar Entrance',
        EXAMINATION: '''Kitchen / Cellar Entrance - a large kitchen big enough to prepare 
a feast for at least 13 people each and every time. a large table covered in surface 
slits in the center of the room, presumably where they carved up their food. 
Along the northern wall sits a large open floor fire with a spitroast above. 
Shelves all around the room with large barrels lain on their side and little wooden 
pegs jammed in the tops of them. This must be where the ale was kept too! In the back 
corner of the room is a cellar door which is locked tight. 
There is a key hole, so maybe there is a key.''',
        DESCRIPTION: 'A large kitchen to prepare feasts and store ale.',
        SOLVED: False,
        UP: 'c4',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
        FLOOR: 'z1' # cellar could be a room, needs coding
    },
    'd1': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Gardens - The small flower bed to the north has soil 
that looks like clay and definitely hasn\'t been tended to in a while. 
Surpirsingly there is life in the flowers here however they do seem to be dying out. 
The larger flower bed to the south looks much the same however there are no flowers in this 
flower bed and the soil looks to have been dug out; you suspect long ago as the mound of excavated soil 
is compact from where the rain has fallen on it over the years.''',
        DESCRIPTION: 'West of the northeast corner of the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'c1',
        RIGHT: 'e1', 
    },
    'd2': { 
        ROOMNAME: 'East tower',
        EXAMINATION: '''A Ladder in the back of the room that goes down goes to the dungeons and up through the tower, 
the ladder down has rotted and theres no way down, however, the ladder going up seems sturdy. The are a number of 
empty wall torch brackets around the room. Only one has a torch and it's unlit. Do you want to take the torch? (yes/no)''',
        DESCRIPTION: 'The ground floor of the eastern tower inside the castle.',
        SOLVED: False,
        UP: '',
        DOWN: 'd3',
        LEFT: '',
        RIGHT: '', 
    },
    'd3': { 
        ROOMNAME: 'East Tower Passage',
        EXAMINATION: '''East Tower Passage - a passage filled with empty barrels and crates. 
Empty torch hangings on the walls and sealed windows. Must be a storage room of sorts. 
Either that or it was barricaded. There is room to just about clamber through to the 
other side to get to the east tower. ''',
        DESCRIPTION: 'A passage leading from the armoury through to the eastern tower.',
        SOLVED: False,
        UP: 'd2',
        DOWN: 'd4',
        LEFT: '',
        RIGHT: '', 
    },
    'd4': { 
        ROOMNAME: 'Armoury',
        EXAMINATION: '''The armoury! Shame there are no armour or weapons in here though! Just empty 
armour stands surrounding the edge of the room. Cobwebs reach from armour stand to armour stand, 
built by spiders that are nowhere to be seen. This room hasn't be disturbed in a long time.''',
        DESCRIPTION: 'A room filled with mostly empty armour stands.',
        SOLVED: False,
        UP: 'd3',
        DOWN: 'd5',
        LEFT: 'c4',
        RIGHT: '', 
    },
    'd5': { 
        ROOMNAME: 'Blacksmith',
        EXAMINATION: '''The coldest room in the building, once the hottest. There sits a great forge at 
the back of the room, with a chimney that goes directly out the roof. The coal chamber beside it 
filled half full with coal. Sitting on one of the anvils an unfinished sword. Whomever left here 
did so in a hurry. There's a bucket of oil beside the furnace which has been covered with a plank of wood.''',
        DESCRIPTION: 'A room for repairing armour, crafting tools and weapons out of metal.',
        SOLVED: False,
        UP: 'd4',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
    },
    'e1': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Two water fountains are in this corner of the gardens, both filled 
with thick green algae sludgey water, though there is a slight breeze, the surface of the 
water remain perfectly, eerily still. One of them has a crack running from the top of the 
fountain feature to its base and the water level is lower than the other fountain. The path 
here ends at the fountains. Against the fenceline of the castle are two benches both rotten, 
in need of repair and sinking into the boggy grass.''',
        DESCRIPTION: 'The northeast corner of the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: '',  
    },
    'e2': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Gardens - The grass along this side of the castle is very boggy. There are support 
pillars along the length of the castle wall, with windows covered by horn panes. there are no 
flowers or flower beds, and a lot of moss growing across the ground. Best to watch your footing.''',
        DESCRIPTION: 'South of the north east corner of the castle gardens.',
        SOLVED: False,
        UP: 'e1',
        DOWN: 'e3',
        LEFT: '',
        RIGHT: '',  
    },
    'e3': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Gardens - More boggy grass, still nothing of interest in the immediate area. 
You can see something sticking out of the ground at the end of the garden.''',
        DESCRIPTION: 'Halfway between the northeast and southeast fences in the castle gardens.',
        SOLVED: False,
        UP: 'e2',
        DOWN: 'e4',
        LEFT: '',
        RIGHT: '',  
    },
    'e4': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Gardens - The ground gets significantly more boggy here. As you approch the end of the garden you 
can see more clearly the shape of a hand sticking out of the mud. Specifically an iron gauntlet reaching upwards. 
It might be too dangerous to step onto that part of the garden, Are you sure you want to proceed? (yes/no)''',
        DESCRIPTION: 'North of the southeast corner of the castle gardens.',
        SOLVED: False,
        UP: 'e3',
        DOWN: 'e5',
        LEFT: '',
        RIGHT: '', 
    },
    'e5': { 
        ROOMNAME: 'Castle gardens',
        EXAMINATION: '''Gardens - bog of death, for every second the player enters this room they will lose 5 hp. 
If the player dies They will be reset to inside the Front Gate. 
You start to sink! now its clear that the gauntlet once belonged to an adventurer. you better get out of here fast''',
        DESCRIPTION: 'The southeast corner of the castle gardens.',
        SOLVED: False,
        UP: 'e4',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
    },
}

# Game interactivity
# Function to notify player of location and description
def print_location():
    print('\n' + ('-' * (6 + len(room_map[player1.loc][DESCRIPTION]))))
    print(' - ' + room_map[player1.loc][ROOMNAME] + ' - ')
    print(' - ' + room_map[player1.loc][DESCRIPTION] + ' - ')
    print('\n' + ('-' * (6 + len(room_map[player1.loc][DESCRIPTION]))))

# Function to prompt player for input
def prompt():
    print('\n What would you like to do?')
    ai_chat('Move options: Move, Go, Travel, Walk\n', s['s0'][S])
    ai_chat('Examine: Examine, Inspect, Interact, Look\n', s['s0'][S])
    ans = input('> ')
    action = ans.strip().lower()
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'locate']
    while action not in acceptable_actions:
        print('You cannot do that, try again')
        break
    if action == 'quit':
        sys.exit()
    elif action in ['move', 'go', 'travel', 'walk']:
        player_move(action)
    elif action in ['examine', 'inspect', 'interact', 'look']:
        print('Options: Examine, Inspect, Interact, Look')
        player_examine(action)
    elif action in ['locate']:
        print_location()
    else:
        prompt()

# Function to move the player through the map
def player_move(myAction):
    
    ai_chat(dia['q27'][Q], s['s2'][S])
    dest = input('> ')
    if dest in ['up', 'north']:
        destination = room_map[player1.loc][UP]
        if destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
        else:
            movement(destination)
    elif dest in ['down', 'south']:
        destination = room_map[player1.loc][DOWN]
        if destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
        else:
            movement(destination)
    elif dest in ['left', 'west']:
        destination = room_map[player1.loc][LEFT]
        if destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
        else:
            movement(destination)
    elif dest in ['right', 'east']:
        destination = room_map[player1.loc][RIGHT]
        if destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
        else:
            movement(destination)
    elif dest is 'cancel':
        prompt()          
# Function for movement handling
def movement(destination):
    print_location()
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

S = ''
s = {'s0':{S:0.002},'s1':{S:0.01}, 's2':{S:0.02}, 's3':{S:0.04}, 's4':{S:0.05}, 's5':{S:0.1}}
def ai_chat(question, speed):
    s = speed
    q = question
    for c in q:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(s)

# AI dialogue
Q = '' 
dia = {
    'q1': {Q:'Would you like to reclaim Camelot Castle? (yes/no)\n'},
    'q2': {Q:'Welcome to Camelot Castle! What is your name?\n'},
    'q3': {Q:'What is your gender? (Male/Female/Anything)\n'},
    'q4': {Q:'Would you like to play solo or as a team (AI)\n'},
    'q5': {Q:'Lets create some knights for your round table!\n'},
    'q6': {Q:'Enter the name of your 1st Knight:\n'},
    'q7': {Q:'Enter the name of your 2nd Knight:\n'},
    'q8': {Q:'Enter the name of your 3rd Knight:\n'},
    'q9': {Q:'Please enter a valid name.\n'},
    'q10': {Q:'Please enter a valid selection\n'},
    'q11': {Q:'Oh that\'s too bad! See you again next time.\n'},
    'q12': {Q:'''Oh so you're feeling brave? I hope your wits are as impressive as your confindence!
Beware of the dangers that lurk within the Castle...\n'''},
    'q13': {Q:'------------------------------------------\n'},
    'q14': {Q:'Welcome to Knights of the round table RPG!\n'},
    'q15': {Q:'                 - Play -                 \n'},
    'q16': {Q:'                 - Help -                 \n'},
    'q17': {Q:'                 - Quit -                 \n'},
    'q18': {Q:'     - Copyright 2023 KarlosMoodios -     \n'},
    'q19': {Q:'     - Please type your selection: -     \n'},
    'q20': {Q:'     - To move, use the arrow keys -      \n'},
    'q21': {Q:'  - Type the commands to exectute them -  \n'},
    'q22': {Q:'    - Use \'Look\' to inspect something -   \n'},
    'q23': {Q:'              - Good luck! -            \n'},
    'q24': {Q:'Your chosen knight names are: \n'},
    'q25': {Q:'Good luck on your adventure!\n'},
    'q26': {Q:'Finised? (Yes/No)\n'},
    'q27': {Q:'Where would you like to move?\n'},
}

def coop_setup():
    round_table = 12
    knights_count = 0
    knight_list = []
    solo_coop = input('> ')
    # Choose Knight names
    if solo_coop.strip().lower() == 'coop':
        ai_chat(dia['q5'][Q], s['s0'][S])
        while knights_count < round_table:
            if knights_count == 0:
                ai_chat(dia['q6'][Q])
                name = input('> Sir: ')
                if name == "":
                    ai_chat(dia['q9'][Q], s['s0'][S])
                    knights_count -= 1
                else:
                    knight_list.append('Sir ' + name)

            elif knights_count == 1:
                ai_chat(dia['q7'][Q], s['s0'][S])
                name = input('> Sir: ')
                if name == "":
                    ai_chat(dia['q9'][Q], s['s0'][S])
                    knights_count -= 1
                else:
                    knight_list.append('Sir ' + name)

            elif knights_count == 2:
                ai_chat(dia['q8'][Q], s['s0'][S])
                name = input('> Sir: ')
                if name == "":
                    ai_chat(dia['q9'][Q], s['s0'][S])
                    knights_count -= 1
                else:
                    knight_list.append('Sir ' + name)

            elif knights_count < round_table:
                n = str(knights_count + 1)
                ai_chat('Enter the name of your '+ n + 'th Knight: \n', s['s0'][S])
                name = input('> Sir: ')
                if name == "":
                    ai_chat(dia['q9'][Q], s['s0'][S], s['s0'][S])
                    knights_count -= 1
                else:
                    knight_list.append('Sir ' + name)   
            knights_count += 1
            n = str(knights_count)
            if knights_count == 1:
                ai_chat("You have " + n + " Knight at the round table.\n", s['s0'][S])
            else:
                ai_chat("You have " + n + " Knights at the round table.\n", s['s0'][S])
        ai_chat(dia['q24'][Q], s['s0'][S])
        for x in knight_list:
            sys.stdout.write(x)
            sys.stdout.write(', ')
            sys.stdout.flush()
            time.sleep(0.5)
        print('\n')
        #  End of choosing Knight names
    elif solo_coop.strip().lower() == 'solo':
        ai_chat(dia['q12'][Q], s['s0'][S])
        time.sleep(4)
    else:
        ai_chat(dia['q10'][Q], s['s0'][S])
        coop_setup()


def start_game():
        os.system('cls')
        ai_chat(dia['q1'][Q], s['s0'][S]) # play
        ans = input('> ')
        if ans.strip().lower() == 'yes':
            ai_chat(dia['q2'][Q], s['s0'][S]) # name?
            player1.name = input('> ')
            ai_chat(dia['q3'][Q], s['s0'][S]) # gender?
            player1.gender = input('> ') 
            if player1.gender.strip().lower() == 'male':
                player1.gender = 'King'
            elif player1.gender.strip().lower() == 'female' :
                player1.gender = 'Queen'
            else:
                player1.gender = player1.gender
            greet_msg = 'Greetings ' + player1.gender + ' ' + player1.name + '!\n'
            ai_chat(greet_msg, s['s0'][S])
            time.sleep(1)
            ai_chat(dia['q4'][Q], s['s0'][S]) # Solo or Co-op?
            coop_setup()
        elif ans.strip().lower() == 'no':
            ai_chat(dia['q11'][Q], s['s0'][S])
            time.sleep(3)
            title_screen()
        else: 
            ai_chat(dia['q10'][Q], s['s0'][S])
            time.sleep(2)
            start_game()
        os.system('cls')
        ai_chat(dia['q25'][Q], s['s0'][S])
        
        print_location()
        main()


title_screen()




