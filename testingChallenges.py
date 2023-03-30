# def main():
#     pass
#     while True:
      
#       try:
#         x = input()
#         if x == 1 or 2:
#           y = int(x)
#           print(int(y*2))
#       except ValueError:
#         print("ValueError! That was a String")
#       except EOFError:
#         print("End")
#         break

# main()

# def main():
#     pass

# main()
# for num in [4, 3, 2, 1]:
#   print(num)

# def main():
#     pass

# main()
# x = int(input())
# for x in range(x, 0, -1):
#   print (x)

#  Reading strings from a file and handling exceptions
# def main():
#     pass

# main()

# while True:
#   try:
#     string = input("Enter a word: ")
#     if string == "quit":
#       break
#     else:
#       print(string)
#   except ValueError:
#       break
#   except EOFError:
#      break

#  Printing the third element of any list
# def main():
#     pass

# main()
# nest = []
# first = []

# while True:
#     try:
#         word = input()
#     except EOFError:
#         break
#     if word == 'break':
#       nest.append(first)
#       first = []
#     else:
#       first.append(word)
#       size = len(first)
#       if size == 3:
#          print (first[2])

#  Appending blank spaces in a list with the letter a
# def main():
#     pass

# main()
# nest = []
# first = []

# while True:
#     try:
#         word = input()
#     except EOFError:
#         break
#     if word == 'break':
#       nest.append(first)
#       first = []
#       print("First: ", first)
#       print("Nest: ", nest)
#       print("--- break ---")
#     else:
#       if word == "":
#            first.append("a")
#       else:
#            first.append(word)
#       print("First: ", first)
#       print("Nest: ", nest)

# def main():
#     pass

# main()
# nest = []
# first = []
# break_count = 0
# while break_count < 2:
#     try:
#         word = input()
#     except EOFError:
#         break
#     if word == 'break':
#       nest.append(first)
#       first = []
#       break_count += 1
#     else:
#       if word == "":
#            first.append("a")
#       else:
#            first.append(word)
# for i in range(0, len(nest)):
#     for j in range(0, len(nest[i])):
#         if (nest[i][j] == ""):
#             nest[i][j] = "a"
# print(nest)
#############################################################################################

# import sys
# import time

# def ai_chat(question):
#     q = question
#     for c in q:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(0.02)

# QUESTION = ''

# # AI dialogue
# ai_dialogue = {
#     'q1': {
#     QUESTION:'Would you like to play: Knights of the round table? (yes/no)\n',
#     },
#     'q2': {
#     QUESTION:'Welcome to Camelot Castle! Whats is your name?\n',
#     },
#     'q3': {
#     QUESTION:'Lets create some knights for your round table!\n',
#     },
#     'q4': {
#     QUESTION:'Enter the name of your 1st Knight:\n',
#     },
#     'q5': {
#     QUESTION:'Enter the name of your 2nd Knight:\n',
#     },
#     'q6': {
#     QUESTION:'Enter the name of your 3rd Knight:\n',
#     },
#     'q7': {
#     QUESTION:'Please enter a valid name.\n',
#     },
#     'q8': {
#     QUESTION:'Please choose a valid option.\n',
#     },
#     'q9': {
#     QUESTION:'\n',
#     },
#     'q10': {
#     QUESTION:'\n',
#     }, 
# }
 
# # team = knight_list[0:11]
# # ai_chat(team)

# ai_chat(ai_dialogue['q1'][QUESTION])
# ans = input('>')
# if ans.strip().lower() == 'yes':
#     round_table = 12
#     knights_count = 0
#     knight_list = []

#     ai_chat(ai_dialogue['q2'][QUESTION])
#     playerName = input('>')
#     playerGender = input('Enter your gender: ')
#     if playerGender.strip().lower() == 'male':
#         playerGender = 'King'
#     elif playerGender.strip().lower() == 'female' :
#         playerGender = 'Queen'
#     else:
#         playerGender = playerGender
#     greet_msg = 'Greetings ' + playerGender + ' ' + playerName + '!\n' 
#     ai_chat(greet_msg)
#     time.sleep(1)
#     ai_chat(ai_dialogue['q3'][QUESTION])
#     while knights_count < round_table:
#         if knights_count == 0:
#             ai_chat(ai_dialogue['q4'][QUESTION])
#             name = input('> Sir: ')
#             if name == "":
#                 ai_chat(ai_dialogue['q7'][QUESTION])
#                 knights_count -= 1
#             else:
#                 knight_list.append('Sir ' + name)

#         elif knights_count == 1:
#             ai_chat(ai_dialogue['q5'][QUESTION])
#             name = input('> Sir: ')
#             if name == "":
#                 ai_chat(ai_dialogue['q7'][QUESTION])
#                 knights_count -= 1
#             else:
#                 knight_list.append('Sir ' + name)

#         elif knights_count == 2:
#             ai_chat(ai_dialogue['q6'][QUESTION])
#             name = input('> Sir: ')
#             if name == "":
#                 ai_chat(ai_dialogue['q7'][QUESTION])
#                 knights_count -= 1
#             else:
#                 knight_list.append('Sir ' + name)

#         elif knights_count < round_table:
#             n = str(knights_count + 1)
#             ai_chat('Enter the name of your '+ n + 'th Knight: \n')
#             name = input('> Sir: ')
#             if name == "":
#                 ai_chat(ai_dialogue['q7'][QUESTION])
#                 knights_count -= 1
#             else:
#                 knight_list.append('Sir ' + name)   
#         knights_count += 1
#         n = str(knights_count)
#         if knights_count == 1:
#             ai_chat("You have " + n + " Knight at the round table.\n")
#         else:
#             ai_chat("You have " + n + " Knights at the round table.\n")
#     print(knight_list)
# else:
#     ai_chat(ai_dialogue['q8'][QUESTION])

    #  End of choosing Knight names

    ###########################################################################################################

# import threading
# import time

# def run_simultaneously():
#     for i in range (11, 21):
#         time.sleep(.5)
#         print('£ '+str(i))

# # create thread object
# t = threading.Thread(target = run_simultaneously)
# # start thread
# t.start()

# for i in range (1, 11):
#     time.sleep(.5)
#     print('\n# '+str(i))


# print('end')


import threading
import time
import os

entered_input = False

def check_for_timeout():
    time.sleep(5)
    if entered_input == True:
        os._exit(0)
    else:
        print('timeout, try again')
        os._exit(0)


print('enter a number to calculate square: ')

# create thread object
t = threading.Thread(target = check_for_timeout)
# start thread
t.start()

number = int(input())
entered_input = True
print('the square of your number is: ' + str(number * number))