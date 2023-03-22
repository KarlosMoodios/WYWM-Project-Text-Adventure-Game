#  Initialise the Game
start = input("Would you like to play: Knights of the round table? (yes/no)")
if start.strip().lower() == "yes":
    round_table = 12
    knights_count = 0
    knight_list = []

    print("Welcome to Camelot Castle! Whats is your name?")
    playerName = input("Enter your name here: ")
    print("Greetings King ", playerName,"!", sep="")
    print("Lets create some knights for your round table!")
    while True:
        #  Choosing Knight names
        while knights_count < round_table:
            if knights_count == 0:
                name = input("Enter the name of your 1st Knight: ")
                if name == "":
                    print ("Please enter a valid name.")
                    knights_count -= 1
                else:
                    knight_list.append(name)

            elif knights_count == 1:
                name = input("Enter the name of your 2nd Knight: ")
                if name == "":
                    print ("Please enter a valid name.")
                    knights_count -= 1
                else:
                    knight_list.append(name)

            elif knights_count == 2:
                name = input("Enter the name of your 3rd Knight: ")
                if name == "":
                    print ("Please enter a valid name.")
                    knights_count -= 1
                else:
                    knight_list.append(name)

            elif knights_count < round_table:
                n = str(knights_count + 1)
                name = input("Enter the name of your "+ n + "th Knight: ")
                if name == "":
                    print ("Please enter a valid name.")
                    knights_count -= 1
                else:
                    knight_list.append(name)   
            knights_count += 1
            print("There are",knights_count, "Knight(s) at the round table")
        #  End of choosing Knight names

        #  Edit knight names 
        #  Select the knight you wish to rename
        #knights_list.insert('index', 'value')
        #  End of edit knights names

        print(knight_list)

        print("--- What would you like to update? ---")

        try:
            selection = int(input("Select your option: "))
            if selection == 1:
                if knights_count < round_table:
                    print("You have", knights_count, "Knight(s)")
                name = str(input("What is their new name: "))
                print("Your knights new name is: "+ name)
            else:
                print("--- Please select a valid option ---")
        except:
            print("--- Try again ---")

        print("Goodbye Sir " + name)