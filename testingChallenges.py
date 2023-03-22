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

print('------------------------------------------')
print('Welcome to Knights of the round table RPG!')
print('------------------------------------------')
print('     - To move, use the arrow keys -      ')
print('  - Type the commands to exectute them -  ')
print('    - Use \'Look\' to inspect something -   ')
print('              - Good luck! -              ')