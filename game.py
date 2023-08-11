# Camelot Castle textRPG
# Created by Karl Moody

import cmd
import textwrap
import sys
import threading
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
        self.loc = 'c3'
        self.game_over = False
        self.entered_input = False
player1 = player()

# Title Screen
def title_screen_selections():
    option = input('\n> ')
    option = option.lower().strip()
    if option.lower() == ('play'):
        start_game() 
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid option.')
        option = input('> ')
        if option.lower() == ('play'):
            start_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('cls')
    a = (len(dia['q13'][Q])) - (len(dia['q14'][Q]))
    b = (len(dia['q13'][Q])) - (len(dia['q15'][Q]))
    c = (len(dia['q13'][Q])) - (len(dia['q18'][Q]))
    d = (len(dia['q13'][Q])) - (len(dia['q19'][Q]))
    ai_chat(('\n' + (dia['q13'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (2 + a // 2)) + (dia['q14'][Q])), s['s0'][S])
    ai_chat((dia['q13'][Q]), s['s0'][S])
    ai_chat(('\n' + (' ' * (2 + b // 2)) + (dia['q15'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (2 + b // 2)) + (dia['q16'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (2 + b // 2)) + (dia['q17'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (2 + c // 2)) + (dia['q18'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (2 + d // 2)) + (dia['q19'][Q])), s['s0'][S])
    title_screen_selections()

def help_menu():
    os.system('cls')
    a = (len(dia['q13'][Q])) - (len(dia['q14'][Q]))
    b = (len(dia['q13'][Q])) - (len(dia['q20'][Q]))
    c = (len(dia['q13'][Q])) - (len(dia['q21'][Q]))
    d = (len(dia['q13'][Q])) - (len(dia['q32'][Q]))
    e = (len(dia['q13'][Q])) - (len(dia['q22'][Q]))
    f = (len(dia['q13'][Q])) - (len(dia['q31'][Q]))
    g = (len(dia['q13'][Q])) - (len(dia['q23'][Q]))
    h = (len(dia['q13'][Q])) - (len(dia['q26'][Q]))
    ai_chat(('\n' + (dia['q13'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (2 + a // 2)) + (dia['q14'][Q])), s['s0'][S])
    ai_chat((dia['q13'][Q]), s['s0'][S])
    ai_chat(('\n' + (' ' * (b // 2)) + (dia['q20'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (c // 2)) + (dia['q21'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (d // 2)) + (dia['q32'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (e // 2)) + (dia['q22'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (f // 2)) + (dia['q31'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (g // 2)) + (dia['q23'][Q])), s['s0'][S])
    ai_chat(('\n' + (' ' * (h // 2)) + (dia['q26'][Q])), s['s0'][S])
    done = input('\n> ').strip().lower()
    if done == 'yes':
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
LIT_EXAMINATION = 'study'
DESCRIPTION = 'describe'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
FLOOR = 'ladder', 'stairs'

solved_rooms = {              'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False, 'a5' : False, 
                              'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False, 'b5' : False, 'b6' : False, 'b7' : False, 'b8' : False, 'b9' : False,
                'c0' : False, 'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False, 'c5' : False,
                              'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False, 'd5' : False,
                              'e1' : False, 'e2' : False, 'e3' : False, 'e4' : False, 'e5' : False, 
                              'z1' : False, 'z2' : False }

room_map = {
    'a1' : {
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
Two water fountains with a path leading through the middle of them and round to the south, the water in these 
fountains glows an almost magical sparkle as the water shoots out from one, over your head into the other and 
back again. You can continue south or return to the east.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'The northwest corner in the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: 'a2',
        LEFT: '',
        RIGHT: 'b1',
        FLOOR: '',
    },
    'a2' : { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
You can see the path continues to the south, right up to the fence. On your left, against the castle wall are a 
series of support pillars that run the length of the castle wall each with window covered by a horn pane situated 
between them, in the soil below are some sunflowers. You can continue south or head back the way you came.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'South of the northwest corner in the castle gardens.',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'a3',
        LEFT: '',
        RIGHT: '',
        FLOOR: '', 
    },
    'a3': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
In this part of the garden there are two benches looking onto charred ground, what looks like it was once a flower 
bed; why would only the flower bed be charred? In the center of the flower bed stands a tall statue of a King, 
though no inscription is present. Behind the northern bench, the horn pane over the window looks loose enough to 
pry it open with your sword.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'Halfway between the northwest and southwest corners in the castle gardens.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'a4',
        LEFT: '',
        RIGHT: '',
        FLOOR: '',
    },
    'a4': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
In the overgrown grass of the gardens you can see what looks like a cellar door buried by some debris, you'll need 
to find some tools to clear this if you want to gain access through here.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'North of the southwest corner in the castle gardens.',
        SOLVED: False,
        UP: 'a3', 
        DOWN: 'a5',
        LEFT: '',
        RIGHT: 'z1',
        FLOOR: '', 
    },
    'a5': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
At the end of the path is another water fountain, functional but not completely. Water just trickling out of the 
top and dribbling down the sides. There must be a blockage somewhere.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'The southwest corner of the castle gardens.',
        SOLVED: False,
        UP: 'a4', 
        DOWN: '',
        LEFT: '',
        RIGHT: '',
        FLOOR: '', 
    },
    'b1': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
Two large flower beds sown into the garden either side of the path, both have lively looking plants that seem to be 
growing well, the soil looks rich with nutrients, as if someone has tended these patches recently, strange...\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'East of the northwest corner of the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'a1',
        RIGHT: 'c1',
        FLOOR: '',
    },
    'b2': { 
        ROOMNAME: '- West Tower -',
        EXAMINATION: '''
There are some arrow holes in the window panes, which leak a slither of light into the room. You can just about
make out a ladder and a table. Its too dark to see anything else.\n''',
        LIT_EXAMINATION: '''
The ground floor of the western tower. You can now see the ladder leads up through the tower. There are some armour 
stands with armour on them, though some pieces are missing. Along the wall there is a bow rack, there's room enough 
for four bows, however, only one bow is present and it has a snapped string. There are 4 empty quivers on a table 
below the bow rack.\n''',
        DESCRIPTION: 'The ground floor of the western tower inside the castle.',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: '',
        RIGHT: '',
        FLOOR: 'b6',
    },
    'b3': { 
        ROOMNAME: '- West Tower Passage -',
        EXAMINATION: '''
The window pane being removed illuminates this corridor enough for you to see you can head north or south. You also 
see torch hangings on the wall though there doesn't seem to be any torches in them.\n''',
        LIT_EXAMINATION: '''
An almost empty hallway leading to the tower on the west side of the castle. To the north is the west tower, south 
returns to the trophy room. There is a stool and a small table along the western wall and a huge crested shield 
hanging above it. To the right of the shield is the window which you entered the castle through. Along the eastern 
wall are empty oil lamp brackets and horn paned windows looking out into the courtyard.\n''',
        DESCRIPTION: 'A passage leading from the trophy room to the west tower.',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'b4',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'b4': { 
        ROOMNAME: '- Trophy Room -',
        EXAMINATION: '''
This room has very little light reaching it. You can only see the passage to the north from whence you came.\n''',
        LIT_EXAMINATION: '''
There are skulls of the fallen behemoth-like creatures slain by the knights, sitting on plinths around the room 
and others hanging from the walls. Most notably, a huge dragon-shaped head hanging from the wall. If only there 
was someone you could ask who knows the story of their origin.\n''',
        DESCRIPTION: 'A room full of age old trophies.',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'b5',
        LEFT: '',
        RIGHT: 'c4',
        FLOOR: '',
    },
    'b5': { 
        ROOMNAME: '- Staircase -',
        EXAMINATION: '''
You cannot see anything at all, if you want to navigate through this area it will need to be done solely by sense of touch.\n''',
        LIT_EXAMINATION: '''
A grand staircase leading up to the top floor of the castle, the stairs look to be in great shape. The 
banister rails not so much. The knights' living quarters must be up there.\n''',
        DESCRIPTION: 'A room with an old staircase.',
        SOLVED: False,
        UP: 'b4',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
        FLOOR: 'b6',
    },
    'b6': { 
        ROOMNAME: '- Landing -',
        EXAMINATION: '''
You cannot see anything at all, if you want to navigate through this area it will need to be done solely by sense of touch.\n''',
        LIT_EXAMINATION: '''
You can see two directions ahead, each leading to a large room. The northern passage has no door and 
the eastern passage has a thick, wooden door with a crown carved into its center.\n''',
        DESCRIPTION: 'An room with an old staircase.',
        SOLVED: False,
        UP: 'b7',
        DOWN: '',
        LEFT: '',
        RIGHT: 'b8',
        FLOOR: 'b5', 
    },
    'b7': { 
        ROOMNAME: '- Knights quarters -',
        EXAMINATION: '''
You cannot see anything at all, if you want to navigate through this area it will need to be done solely by sense of touch.\n''',
        LIT_EXAMINATION: '''
''',
        DESCRIPTION: 'A room with an old staircase.',
        SOLVED: False,
        UP: '',
        DOWN: 'b6',
        LEFT: '',
        RIGHT: '',
        FLOOR: '', 
    },
    'b8': { 
        ROOMNAME: '- Kings quarters -',
        EXAMINATION: '''
You cannot see anything at all, if you want to navigate through this area it will need to be done solely by sense of touch.\n''',
        LIT_EXAMINATION: '''
''',
        DESCRIPTION: 'An room with an old staircase.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'b6',
        RIGHT: '',
        FLOOR: '', 
    },
    'b9': { 
        ROOMNAME: '- Merlins quarters -',
        EXAMINATION: '''
As you climb up the ladder and enter the room you find a strange figure encapsulated within a glowing block of ice. 
As your mind races with excitement and fear you can only wonder as to what will happen if the ice thaws.\n''',
        LIT_EXAMINATION: '''''',
        DESCRIPTION: 'Merlins Tower! Unbelievable. Imagine what magic went on in here.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
        FLOOR: 'd2', 
    },
    'c0': { 
        ROOMNAME: '- Start -',
        EXAMINATION: '''
After a long climb you reach the top of the hill, you finally arrive at what you suspect to be the 
Castle of Camelot with nothing but your hammer and sword. It seems to be in good shape and looks 
safe to enter. The castle is surrounded by an 8ft tall weathered iron fence, however, it seems to 
be as sturdy as it was the day it was built.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'The entrance to the castle grounds.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'c1': { 
        ROOMNAME: '- Castle gardens / Front gate -',
        EXAMINATION: '''
A once mighty iron gate now rusted and creeks as it opens. You enter through the front gate it slams 
shut behind you. you notice either side of the path 2 statue plinths, one of them with the statue of 
a mighty looking king atop and a plaque that reads "Arthur - King of the Britons. The other has a 
broken statue, a damaged plaque with an unreadable inscription and the resemblance of mangled iron 
platemail lay beside it on the ground. The path before you splits into three directions: 
East, south and West.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'Inside the front gate of the castle grounds.',
        SOLVED: False,
        UP: '',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'd1', 
        FLOOR: '',
    },
    'c2': { 
        ROOMNAME: '- Courtyard Entrance -',
        EXAMINATION: '''
Either side of the arch are 2 huge support pillars reaching way up to the top of the towers on each 
side of the entrance. Both have ivy growing up them. If thats not kept in check it could cause 
structural damage to the castle. Through the portcullis which blocks the archway, you can see a 
large fountain. Each layer of the fountain bears the shape of a crown, definitely fit for a king!\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'An arch shaped tunnel leading into the courtyard of the castle.',
        SOLVED: False,
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
        FLOOR: '',
    },
    'c3': { 
        ROOMNAME: '- Castle courtyard -',
        EXAMINATION: '''
There is a huge, empty water fountain in the center and flower beds all around the perimeter of the courtyard. 
The flower beds are full of life. There are horn paned windows all around and a huge wooden door with iron 
trimmings and bronze handles. The windows all look sealed shut and the door is closed.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'A beautiful courtyard filled with statues, flowers and a fountain.',
        SOLVED: False,
        UP: '',
        DOWN: 'c4',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'c4': { 
        ROOMNAME: '- Main Hall -',
        EXAMINATION: '''
Light creeps in through the cracks of the door from the courtyard. It isn't much but it's enough to see the 
torch hanging on the wall in the back of the room beside the door to the next room. You can also see the 
outline of a large table in the center of the room.\n''',
        LIT_EXAMINATION: '''
What a sight, the table where Arthur and his 12 knights conferred about their adventures. The table looks 
strong! As you wipe away the thick layer of dust coating the table you can see the inscriptions of each 
knights name in the table as a placeholder for where they each sat. Many a feast must have been eaten 
at this table and ale drunk too.\n''',
        DESCRIPTION: 'A great hall with a large round table situated right in the center of the floor.',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'c5',
        LEFT: 'b4',
        RIGHT: 'd4',
        FLOOR: '', 
    },
    'c5': { 
        ROOMNAME: '- Kitchen / Cellar Entrance -',
        EXAMINATION: '''
''',
        LIT_EXAMINATION: '''
A large kitchen big enough to prepare a feast for at least 13 people each and every time. a large table 
covered in surface slits in the center of the room, presumably where they carved up their food. Along 
the northern wall sits a large open floor fire with a spitroast above. Shelves all around the room with 
large barrels lain on their side and little wooden pegs jammed in the tops of them. This must be where 
the ale was kept too! In the back corner of the room is a cellar door which is locked tight. There is a 
key hole, so maybe there is a key.\n''',
        DESCRIPTION: 'A large kitchen to prepare feasts and store ale.',
        SOLVED: False,
        UP: 'c4',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
        FLOOR: 'z1',
    },
    'd1': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
The small flower bed to the north has soil that looks like clay and definitely hasn't been tended to in a 
while. Surpirsingly there is life in the flowers here however they do seem to be dying out. The larger 
flower bed to the south looks much the same however there are no flowers in this flower bed and the soil 
looks to have been dug out; you suspect long ago as the mound of excavated soil is compact from where the 
rain has fallen on it over the years.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'West of the northeast corner of the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'c1',
        RIGHT: 'e1', 
        FLOOR: '',
    },
    'd2': { 
        ROOMNAME: '- East tower -',
        EXAMINATION: '''
A Ladder in the back of the room goes down into darkness and up through the tower. The ladder 
down has rotted and is not safe to use, however, the ladder going up is fine. The are a number of 
wall torch brackets around the room, one torch is present.\n''',
        LIT_EXAMINATION: '''
''',
        DESCRIPTION: 'The ground floor of the eastern tower inside the castle.',
        SOLVED: False,
        UP: '',
        DOWN: 'd3',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'd3': { 
        ROOMNAME: '- East Tower Passage -',
        EXAMINATION: '''
You can see the faint light of a blueish glow, shining from the back of the room. This room is blocked and you can't see a way through.\n''',
        LIT_EXAMINATION: '''
A passage filled with empty barrels and crates. Empty torch hangings on the walls and sealed windows. 
Must be a storage room of sorts. Either that or it was barricaded. There is room to just about clamber 
through to the other side to get to the east tower.\n''',
        DESCRIPTION: 'A passage leading from the armoury through to the eastern tower.',
        SOLVED: False,
        UP: 'd2',
        DOWN: 'd4',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'd4': { 
        ROOMNAME: '- Armoury -',
        EXAMINATION: '''
There is very little light in this room. To your north you can see a glowing light. South you can see very 
faint, natural light. West of is the light coming from the main hall.\n''',
        LIT_EXAMINATION: '''
The armoury! Shame there are no armour or weapons in here though! Just empty armour stands surrounding the 
edge of the room. Cobwebs reach from one armour stand to the next, built by spiders that are nowhere to be seen. 
This room hasn't be disturbed in a long time.\n''',
        DESCRIPTION: 'A room filled with mostly empty armour stands.',
        SOLVED: False,
        UP: 'd3',
        DOWN: 'd5',
        LEFT: 'c4',
        RIGHT: '', 
        FLOOR: '',
    },
    'd5': { 
        ROOMNAME: '- Blacksmith -',
        EXAMINATION: '''
The coldest room in the building, once the hottest. There sits a great forge at the back of the room, with a chimney that goes 
directly out the roof. There is a small amount of light entering through it. Enough to see a bucket of oil beside the furnace 
which has been covered with a plank of wood with a tinderbox beside it.\n''',
        LIT_EXAMINATION: '''
This room is filled with useful items. You can see a bench with an assortment of tools stacked on it, a coal chamber beside it 
filled half full with coal. Sitting on one of the anvils an unfinished sword. Whomever left here did so in a hurry.''',
        DESCRIPTION: 'A room for repairing armour, crafting tools and weapons out of metal.\n',
        SOLVED: False,
        UP: 'd4',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'e1': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
Two water fountains are in this corner of the gardens, both filled with thick green algae sludgey water, though there is a 
slight breeze, the surface of the water remain perfectly, eerily still. One of them has a crack running from the top of the 
fountain feature to its base and the water level is lower than the other fountain. The path here ends at the fountains. 
Against the fenceline of the castle are two benches both rotten, in need of repair and sinking into the boggy grass.\n''',
        LIT_EXAMINATION: '''
''',
        DESCRIPTION: 'The northeast corner of the castle gardens.',
        SOLVED: False,
        UP: '',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: '',  
        FLOOR: '',
    },
    'e2': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
The grass along this side of the castle is very boggy. There are support pillars along the length of the castle wall, with 
windows covered by horn panes. there are no flowers or flower beds, and a lot of moss growing across the ground. 
Best to watch your footing.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'South of the north east corner of the castle gardens.',
        SOLVED: False,
        UP: 'e1',
        DOWN: 'e3',
        LEFT: '',
        RIGHT: '',  
        FLOOR: '',
    },
    'e3': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
More boggy grass, still nothing of interest in the immediate area. You can see something sticking out of the ground at the 
end of the garden.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'Halfway between the northeast and southeast fences in the castle gardens.',
        SOLVED: False,
        UP: 'e2',
        DOWN: 'e4',
        LEFT: '',
        RIGHT: '',  
        FLOOR: '',
    },
    'e4': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
The ground gets significantly more boggy here. As you approch the end of the garden you can see more clearly the shape of 
a hand sticking out of the mud. Specifically an iron gauntlet reaching upwards. It might be too dangerous to step onto 
that part of the garden.\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'North of the southeast corner of the castle gardens.',
        SOLVED: False,
        UP: 'e3',
        DOWN: 'e5',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'e5': { 
        ROOMNAME: '- Castle gardens -',
        EXAMINATION: '''
You start to sink. Now its clear that the gauntlet once belonged to an adventurer. You better get out of here fast!\n''',
        LIT_EXAMINATION: 'examine',
        DESCRIPTION: 'The southeast corner of the castle gardens.',
        SOLVED: False,
        UP: 'e4',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
        FLOOR: '',
    },
    'z1': { 
        ROOMNAME: '- Cellar -',
        EXAMINATION: '''
Now that you have a lit torch you're able to see what's in the room. The king clearly trusted 
nobody with his wine collection! He must have kept the key with him and passed it down to the chef only when it was needed!\n''', # needs rewriting to align with merlins chat
        LIT_EXAMINATION: '''
''',
        DESCRIPTION: 'The cellar beneath the castle.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'a4',
        RIGHT: '', 
        FLOOR: 'c5',
    },
    'z2': { 
        ROOMNAME: '- Dungeon -',
        EXAMINATION: '''
After fixing the ladder you have gained access to the dungeon. With your torch lighting up the room you can clearly see 
that whatever it was that drew the king and his men away from the castle, they must have done so in a hurry. There's a 
skeleton in the cell who presumably died of starvation and has been here for a long time.\n''',
        LIT_EXAMINATION: '''
''',
        DESCRIPTION: 'The cellar beneath the castle.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '', 
        FLOOR: 'd2',
    },
}

# Room items
contents = {'plank' : False, 'bucket' : False, 'oil' : False, 'tinderbox' : False, 'tools' : False, 'materials' : False,}

# Game interactivity
# Style and display location with description 
def print_location():
    x = (len(room_map[player1.loc][DESCRIPTION])) - (len(room_map[player1.loc][ROOMNAME]))
    ai_chat('\n' + ('-' * (10 + len(room_map[player1.loc][DESCRIPTION]))), s['s0'][S])
    ai_chat('\n' + (' ' * (5 + x // 2)) + room_map[player1.loc][ROOMNAME], s['s0'][S])
    ai_chat('\n' + (' ' * 5) + room_map[player1.loc][DESCRIPTION], s['s0'][S])
    ai_chat('\n' + ('-' * (10 + len(room_map[player1.loc][DESCRIPTION]))), s['s0'][S])

# Prompt player for input
def prompt():
    ai_chat('\nWhat would you like to do?', s['s0'][S])
    ai_chat('\nMove options: Move, Go, Travel, Walk, Climb,', s['s0'][S])
    ai_chat('\nExamine options: Examine, Inspect, Look,', s['s0'][S])
    ai_chat('\nInteraction options: Interact, Use, Open.', s['s0'][S])
    ans = input('\n> ')
    action = ans.strip().lower()
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'locate', 'open', 'use', 'climb', 'study']
    while action not in acceptable_actions:
        ai_chat('You cannot do that, try again', s['s0'][S])
        break
    if action == 'quit' or action == 'exit':
        sys.exit()
    elif action in ['move', 'go', 'travel', 'walk', 'climb']:
        player_move()
    elif action in ['examine', 'inspect', 'look', 'study']:
        player_examine(action)
    elif action in ['interact', 'use', 'open']:
        interact()
    elif action in ['locate']:
        print_location()
    else:
        prompt()

# Move the player
def player_move():
    
    ai_chat(dia['q27'][Q], s['s2'][S])
    dest = input('> ').strip().lower()
    if dest in ['up', 'north']:
        destination = room_map[player1.loc][UP]
        if destination == '' and player1.loc == 'c3':
            ai_chat('The portcullis is locked and can only be opened using the winching mechanism beside you.\n', s['s1'][S])
            time.sleep(1)
        elif destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
        else:
            movement(destination)
    elif dest in ['down', 'south']:
        destination = room_map[player1.loc][DOWN]
        if destination == '' and player1.loc == 'c0':
            ai_chat('You try the latch on the gate but it\'s rusted solid! Try something else...\n', s['s1'][S])
            time.sleep(1)
        elif destination == '' and player1.loc == 'c2':
            ai_chat('The portcullis is locked and can only be opened from the inside. Maybe you can find the right way in somewhere else.\n', s['s1'][S])
            time.sleep(1)
        elif destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
            time.sleep(1)
        else:
            movement(destination)
    elif dest in ['left', 'west']:
        destination = room_map[player1.loc][LEFT]
        if destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
            time.sleep(1)
        else:
            movement(destination)
    elif dest in ['right', 'east']:
        destination = room_map[player1.loc][RIGHT]
        if destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
            time.sleep(1)
        elif destination == 'z1' and room_map['b8'][SOLVED] == False:
            ai_chat('The Door on the cellar is locked, maybe theres a key somewhere...\n', s['s0'][S])
            time.sleep(1)
        else:
            movement(destination)
    elif dest in ['ladder', 'stairs']:
        destination = room_map[player1.loc][FLOOR]
        if player1.loc == 'd2':
            ai_chat('Do you want to climb up or down?\n', s['s1'][S])
            ans = input('> ').strip().lower()
            if ans == 'up':
                room_map['d2'][FLOOR] = 'b9'
                destination = room_map[player1.loc][FLOOR]
                movement(destination)
            elif ans == 'down':
                if room_map['d5'][SOLVED] == False:
                    ai_chat('This ladder needs fixing before you can use it.\n', s['s1'][S])
                else:
                    room_map['d2'][FLOOR] = 'z2'
                    destination = room_map[player1.loc][FLOOR]
                    movement(destination)
            elif ans != 'up' or ans != 'down':
                ai_chat(dia['q10'][Q], s['s0'][S])
                time.sleep(1)
            else:
                movement(destination)
        elif destination == '':
            ai_chat('You can\'t go that way!\n', s['s0'][S])
            time.sleep(1)
        else:
            movement(destination)
    elif dest is 'cancel':
        prompt()

# Function for movement handling
def movement(destination):
    player1.loc = destination
    print_location()

# Examine surroundings 
def player_examine(action):
    a = action
    if a == 'study' and contents['tinderbox'] == False:
        ai_chat('It would be impossible to properly study this room while it\'s this dark...Try finding a light source.', s['s1'][S])
        return
    if a == 'study' or a == 'examine' and contents['tinderbox'] == True:
        if player1.loc == 'b2':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'b3':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'b4':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'b5':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'b6':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'b7':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'b8':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'b9':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'c4':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'c5':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'd2':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'd3':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'd4':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'd5':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'z1':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        elif player1.loc == 'z2':
            ai_chat(room_map[player1.loc][LIT_EXAMINATION], s['s1'][S])
        else:
            ai_chat(room_map[player1.loc][EXAMINATION], s['s1'][S])
        time.sleep(1)
    elif a == 'examine' and room_map[player1.loc][SOLVED] == False:
        ai_chat(room_map[player1.loc][EXAMINATION], s['s1'][S])
        time.sleep(1)
    else:
        ai_chat('This room has been completed already', s['s1'][S])
        time.sleep(1)

# Location based interaction with objects
def interact():
    print ('\nWhat would you like to interact with?')
    obj = input('> ').strip().lower()
    objects = ['dumbwaiter', 'torch', 'bucket', 'plank', 'tools', 'lock', 'portcullis', 'gate', 'window', 'ladder', 'winch', 'tinderbox', 'materials', 'winch']
    while obj not in objects:
        ai_chat('You cannot do that, try again', s['s0'][S])
        time.sleep(1)
        break
    if player1.loc == 'b8' and obj in objects:
        ai_chat('\nYou open the dumbwaiter and find a key, what could this be for?', s['s0'][S])
        time.sleep(1)
        room_map['b8'][SOLVED] = True
    if player1.loc == 'c5' and obj in objects:
        ai_chat('\nYou open the dumbwaiter and find that the pulley system is jammed, the tray must be somewhere else in the building.', s['s1'][S])
        time.sleep(1)
    if player1.loc == 'c3' and obj in objects:
        portcullis = 0
        winch = 0
        winch_count = 0
        if obj == 'portcullis':
            if portcullis == 0:
                ai_chat('\nThis is way to heavy to open by hand! Try interacting with something else...', s['s2'][S])
                time.sleep(1)
            elif portcullis == 1:
                ai_chat('\nIf you want to close the portcullis, use the winch again.', s['s2'][S])
            else:
                ai_chat('\nThe portcullis is broken', s['s2'][S])
        if obj == 'winch':
            if winch == 0:
                if winch_count == 0:
                    ai_chat('\nAs you wind the winch, the chains grind together and emit a cloud of rust into the air, luckily the chains are strong enough to lift the portcullis and it opens.', s['s1'][S])
                    time.sleep(1)
                    room_map['c2'][DOWN] = 'c3'
                    room_map['c3'][UP] = 'c2'
                    room_map['c3'][SOLVED] = True
                    portcullis += 1
                    winch += 1
                    winch_count += 1
                    print(portcullis)
                    print(winch)
                    print(winch_count)
                elif winch_count > 0:
                    ai_chat('\nThe portcullis opens.', s['s1'][S])
                    time.sleep(1)
                    room_map['c2'][DOWN] = 'c3'
                    room_map['c3'][UP] = 'c2'
                    room_map['c3'][SOLVED] = True
                    portcullis += 1
                    winch += 1
                    winch_count += 1
                    print(portcullis)
                    print(winch)
                    print(winch_count)
            elif winch == 1:
                ai_chat('\nYou wind the winch until the portcullis is fully closed.', s['s1'][S])
                time.sleep(1)
                room_map['c2'][DOWN] = ''
                room_map['c3'][UP] = ''
                room_map['c3'][SOLVED] = False
                portcullis -= 1
                winch -= 1
                winch_count += 1
                print(portcullis)
                print(winch)
                print(winch_count)

    if player1.loc == 'c0' and obj in objects:
        ai_chat(dia['q28'][Q], s['s0'][S])
        ans = input('> ').strip().lower()
        acceptable_answers = ['hammer', 'sword']
        while ans not in acceptable_answers:
            ai_chat('Please Choose a valid option. (hammer/Sword)', s['s1'][S])
        if ans == 'hammer':
            ai_chat('''\nYou swing your hammer down on the latch, breaking it free just enough to open the gate. You enter through and the gate slams shut behind you.''', s['s1'][S])
            time.sleep(1)
            room_map['c0'][DOWN] = 'c1'
            destination = room_map[player1.loc][DOWN]
            movement(destination)
        elif ans == 'sword':
            ai_chat('\nYou wedge your sword under the latch and use leverage to break the latch free but it doesn\'t work. Maybe there\'s another tool you could try?',s['s1'][S])
            time.sleep(1)
    if player1.loc == 'c4' and obj in objects:
        ai_chat(dia['q29'][Q], s['s0'][S])
        ans = input('> ').strip().lower()
        if ans == 'yes':
            ai_chat('You take the torch from the wall mount, now to find some fuel.\n', s['s1'][S])
            room_map['c4'][SOLVED] = True
        elif ans == 'no':
            ai_chat('You leave the torch on the wall.\n', s['s1'][S])     
        else:
            ai_chat(dia['q10'][Q], s['s1'][S])
    if player1.loc == 'd5' and room_map['c4'][SOLVED] == True and obj in objects:
        if obj == 'plank':
            if contents['plank'] == False:
                ai_chat('Would you like to remove the plank off the bucket of oil? (Yes/No)\n', s['s1'][S])
                ans = input('> ').strip().lower()
                if ans == 'yes':
                    contents['plank'] = True
                    ai_chat('You remove the plank from the bucket of oil.\n', s['s1'][S])
                    return
                elif ans == 'no':
                    ai_chat('You leave the plank where it is.\n', s['s1'][S])
                else:
                    ai_chat(dia['q10'][Q], s['s1'][S])
        if obj == 'bucket':
            if contents['plank'] == True and contents['bucket'] == False:
                ai_chat('Would you like to use the torch with the bucket of oil? (Yes/No)\n', s['s1'][S])
                ans = input('> ').strip().lower()
                if ans == 'yes':
                    contents['bucket'] = True
                    ai_chat('You soak the torch in oil.\n', s['s1'][S])
                    return
                elif ans == 'no':
                    ai_chat('You don\'t soak the torch in oil.\n', s['s1'][S])
                else:
                    ai_chat(dia['q10'][Q], s['s1'][S])
            else:
                ai_chat('The bucket is covered, uncover it first then use it.\n', s['s1'][S])
                time.sleep(1)
        if obj == 'tinderbox':
            if contents['bucket'] == True and contents['tinderbox'] == False:
                ai_chat('Would you like to use the tinderbox to light the torch? (Yes/No)\n', s['s1'][S])
                ans = input('> ').strip().lower()
                if ans == 'yes':
                    contents['tinderbox'] = True
                    ai_chat('After a few sparks of the tinderbox, you eventually light the torch.\n', s['s1'][S])
                    ai_chat('You Have a lit torch and are now able to see more of your surroundings... You should try examining other rooms you have already examined.\n', s['s1'][S])
                    return
                elif ans == 'no':
                    ai_chat('You decide not to light the torch.\n', s['s1'][S])
                else:
                    ai_chat(dia['q10'][Q], s['s1'][S])
            else:
                if contents['plank'] == False:
                    ai_chat('You need to remove the plank from the bucket before you can do that.\n', s['s1'][S])
                elif contents['bucket'] == False:
                    ai_chat('You need to douse the torch in oil first.\n', s['s1'][S])
                else:
                    ai_chat(dia['q10'][Q], s['s1'][S])
                time.sleep(1)
        if obj == 'tools':
            if contents['tinderbox'] == True and contents['tools'] == False:
                ai_chat('You see some nails, a saw, a hatchet, a few chisels, an auger and a mallet. Do you wish to take them?\n', s['s1'][S])
                ans = input('> ').strip().lower()
                if ans == 'yes':
                    contents['tools'] = True
                    ai_chat('You now have all the tools required to fix just about anything.\n', s['s1'][S])
                    return
                elif ans == 'no':
                    ai_chat('You leave the tools on the bench.\n', s['s1'][S])
                else:
                    ai_chat(dia['q10'][Q], s['s1'][S])
            else:
                ai_chat('Tools?! ', s['s1'][S])
                time.sleep(0.5)
                ai_chat('What tools?.\n', s['s2'][S])
        if obj == 'materials':
            if contents['tinderbox'] == True and contents['materials'] == False:
                ai_chat('\n', s['s1'][S])
                ans = input('> ').strip().lower()
                if ans == 'yes':
                    contents['materials'] = True
                    ai_chat('You take an inventory and grab a handful of materials, enough to make repairs.\n', s['s1'][S])
                    return
                elif ans == 'no':
                    ai_chat('You leave the materials in the workshop.\n', s['s1'][S])
                else:
                    ai_chat(dia['q10'][Q], s['s1'][S])
                room_map['d5'][SOLVED] = True
            else:
                ai_chat('With this amount of light it would be impossible to take inventory of materials.\n', s['s1'][S])

    if player1.loc == 'a3' and obj in objects:
        ai_chat('The window pane looks loose enough to pry off, would you like to use your hammer or sword?', s['s0'][S])
        ans = input('> ').strip().lower()
        acceptable_answers = ['hammer', 'sword']
        while ans not in acceptable_answers:
            ai_chat('Please Choose a valid option. (hammer/Sword)', s['s1'][S])
            break
        if ans == 'hammer':
            ai_chat('''\You wedge the claw end of your hammer into the window but fail to gain enough leverage to pry the window open.''', s['s1'][S])
            time.sleep(1)
        elif ans == 'sword':
            ai_chat('\nYou wedge your sword into the gap and use leverage to break the pane free from the window. Finally, a way into the castle!', s['s1'][S])
            time.sleep(0.5)
            room_map['a3'][RIGHT] = 'b3'
            ai_chat('\nWould you like to enter? (Yes/No)',s['s1'][S])
            ans = input('> ').strip().lower()
            if ans == 'yes':
                destination = room_map[player1.loc][RIGHT]
                movement(destination)
            elif ans == 'no':
                ai_chat('\nYou stay in the castle gardens.', s['s1'][S])
            else:
                ai_chat(dia['q10'][Q], s['s0'][S])
    if player1.loc == 'd2' and room_map['d5'][SOLVED] == True and obj in objects:
        ai_chat('Would you like to fix the ladder? (Yes/No)', s['s1'][S])
        ans = input('> ').strip().lower()
        if ans == 'yes':
            ai_chat('\nYou fix the ladder with the tools and materials you found in the blacksmith room.', s['s1'][S])
            room_map['d2'][FLOOR] = 'z2'
        elif ans == 'no':
            ai_chat('\nYou decide not to fix the ladder.', s['s1'][S])
        else:
            ai_chat(dia['q10'][Q], s['s0'][S])
    

# Game functionality
def main():
    while player1.game_over is False:
        prompt()
        player1.entered_input = False
        if player1.loc == 'e5':
            ai_chat('\nYOU ARE DYING! ', s['s1'][S])
            ai_chat('\nYou have 10 seconds to escape before its too late! (Esc/Run)', s['s1'][S])
            t = threading.Thread(target = death_timeout)
            t.start()
            esc = input('\n> ').strip().lower()
            player1.entered_input = True
            if player1.hp < 40:
                player1.entered_input = False
                ai_chat('\nYour remaining HP is: ' + str(player1.hp), s['s1'][S])
                ai_chat('\nYou have sunk too far into the bog to escape!', s['s3'][S])
                ai_chat('\nSay your prayers.', s['s5'][S])
                if player1.hp == 0:
                    time.sleep(4)
                    game_over()
                    return
            elif esc == 'esc' or esc == 'run':
                if player1.hp >= 60:
                    destination = room_map[player1.loc][UP]
                    movement(destination)
                    ai_chat('\nYour remaining HP is: ' + str(player1.hp), s['s1'][S])
                    ai_chat('\nYou have dodged death, this time..', s['s2'][S])
                    
                elif player1.hp >= 40:
                    destination = room_map[player1.loc][UP]
                    movement(destination)
                    ai_chat('\nYou narrowly escape with your life!', s['s1'][S])
                    ai_chat('\nYour remaining HP is: ' + str(player1.hp), s['s1'][S])
                        
            elif esc != 'esc' or esc != 'run':
                ai_chat(dia['q10'][Q], s['s1'][S])

# Death timer
def death_timeout():
    if player1.entered_input == False:
        while player1.hp > 0:
            player1.hp -= 10
            time.sleep(1)
            if player1.entered_input == True:
                break
    else:
        return
        
# Game over
def game_over():
    player1.game_over == True
    os.system('cls')
    ai_chat(dia['q30'][Q], s['s3'][S])
    time.sleep(2)

# AI dialogue
Q = '' 
dia = {
    'q1': {Q:'Would you like to explore Camelot Castle? (yes/no)\n'},
    'q2': {Q:'Welcome to Camelot Castle! What is your name?\n'},
    'q3': {Q:'What is your gender? (Male/Female/Anything)\n'},
    'q4': {Q:'Would you like to play solo or as a team (AI) (solo/team)\n'},
    'q5': {Q:'Lets create some knights for your round table!\n'},
    'q6': {Q:'Enter the name of your 1st Knight:\n'},
    'q7': {Q:'Enter the name of your 2nd Knight:\n'},
    'q8': {Q:'Enter the name of your 3rd Knight:\n'},
    'q9': {Q:'Please enter a valid name.\n'},
    'q10': {Q:'Please enter a valid selection\n'},
    'q11': {Q:'Oh that\'s too bad! See you again next time.\n'},
    'q12': {Q:'Oh so you\'re feeling brave?'},
    'q12a': {Q:' I hope your wits are as impressive as your confidence!'},
    'q12b': {Q:' Beware of the dangers that \nlurk within the Castle...\n'},
    'q12c': {Q:'Muahahahahaha...\n'},
    'q13': {Q:'-----------------------------------------------------------------------------------------'},
    'q14': {Q:'Welcome to the Camelot Castle textRPG!\n'},
    'q15': {Q:'- Play -'},
    'q16': {Q:'- Help -'},
    'q17': {Q:'- Quit -'},
    'q18': {Q:'- Copyright 2023 KarlosMoodios -'},
    'q19': {Q:'- Please type your selection -'},
    'q20': {Q:'- To move, type move and hit enter, then type the direction and hit enter -'},
    'q21': {Q:'- To examine, type examine then hit enter -'},
    'q22': {Q:'- To interact, type interact and hit enter, then type the object name and hit enter -'},
    'q23': {Q:'- Good luck! -'},
    'q24': {Q:'Your chosen knight names are: \n'},
    'q25': {Q:'Good luck on your adventure!\n'},
    'q26': {Q:'Finished? (Yes/No)'},
    'q27': {Q:'Where would you like to move?\n'},
    'q28': {Q:'Would you like to use your hammer or sword? (hammer/sword)\n'},
    'q29': {Q:'Would you like to take a torch from the wall?\n'},
    'q30': {Q:'You have died! Game over...\n'},
    'q31': {Q:'- If you die it will be game over and the application will close -'},
    'q32': {Q:'- Examine often in order to find clues -'},
    
}

# AI chat speed
S = ''
s = {'s0':{S:0.002},'s1':{S:0.01}, 's2':{S:0.02}, 's3':{S:0.04}, 's4':{S:0.05}, 's5':{S:0.1}}

def ai_chat(question, speed):
    s = speed
    q = question
    for c in q:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(s)


def coop_setup():
    round_table = 12
    knights_count = 0
    knight_list = []
    solo_team = input('> ')
    # Choose Knight names
    if solo_team.strip().lower() == 'team':
        ai_chat(dia['q5'][Q], s['s0'][S])
        while knights_count < round_table:
            if knights_count == 0:
                ai_chat(dia['q6'][Q], s['s1'][S])
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
    elif solo_team.strip().lower() == 'solo':
        # ai_chat(dia['q12'][Q], s['s3'][S])
        # time.sleep(1)
        # ai_chat(dia['q12a'][Q], s['s3'][S])
        # time.sleep(1)
        # ai_chat(dia['q12b'][Q], s['s4'][S])
        # time.sleep(2)
        # ai_chat(dia['q12c'][Q], s['s5'][S])
        time.sleep(1)
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
            time.sleep(2)
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




