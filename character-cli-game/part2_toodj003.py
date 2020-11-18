# File      : part2_toodj003.py
# Author    : Declan Toohey
# Email Id  : toodj003
# Version: 8.9 10 June 2019
# Description: Assessment 2 - Part 2 Manage Character Information.
# This is my own work as defined by the University's Academic Misconduct policy.

import character
import random
import os



# Function:     display_details() - Displays Uni info to output screen
def display_details():
    print("File     : part2_toodj003.py")
    print("Author   : Declan Toohey")
    print("Stud ID  : 110284360")
    print("Email ID : toodj003")
    print("This is my own work as defined by the University's Academic Misconduct Policy.\n")


# Function:     read_file() - Reads text file with all the characters details inside
# Parameters:   filename(string) - string of the name of the file to be opened and read from
# Returns:      character_list(list) - list of all the characters
def read_file(filename):
    # List to store information on heroes and villains
    character_list = []
    
    
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(CURRENT_FOLDER, filename)

    infile = open(file_path, "r")

    index = 0

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != "":

        # Get name
        name = line.strip("\n")

        # Read in next line
        line = infile.readline()
        
        # Get secret_identity
        secret_id = line.strip("\n")

        # Read in next line
        line = infile.readline()
        
        # Split line into no battles, no won, no lost, etc.
        info_list = line.split()
        is_hero = info_list[0]
        if is_hero == "h":
            is_hero = True
        else:
            is_hero = False
        no_battles = int(info_list[1])
        no_won = int(info_list[2])
        no_lost = int(info_list[3])
        no_drawn = int(info_list[4])
        health = int(info_list[5])        
        
        # Create new Character object with character (hero and villain) info
        new_character = character.Character(name, secret_id, is_hero, no_battles, no_won,
                                              no_lost, no_drawn, health)
        
        # Add new character to character_list
        character_list.append(new_character)
        
        # Read next line of file.
        line = infile.readline()
    
    return character_list


# Function:     display_characters() - Displays characters in a table with all their respected stats
# Parameters:   character_list(list) - list of all the characters
#               display_type(int) - 0 = all characters to be displayed
#                                 - 1 = only hero characters to be displayed
#                                 - 2 = only villain characters to be displayed
def display_characters(character_list, display_type):
    # Initial Formatting for table
    print("\n===================================================")
    print("-     Character (heroes and villains) Summary     -")
    print("===================================================")
    print("-                             P  W  L  D  Health  -")
    print("---------------------------------------------------")
    # Determine if to display all characters, only heroes or only villains.
    # only hero characters to be displayed
    if display_type == 1:
        for i in range(len(character_list)):
            if character_list[i].get_is_hero():
                print("-  ", end="")
                print(character_list[i], end="")
                print("  -")
                print("---------------------------------------------------")

    # only villain characters to be displayed
    elif display_type == 2:
        for i in range(len(character_list)):
            if not character_list[i].get_is_hero():
                print("-  ", end="")
                print(character_list[i], end="")
                print("  -")
                print("---------------------------------------------------")
    # all characters to be displayed
    else:
        for i in range(len(character_list)):
            print("-  ", end="")
            print(character_list[i], end="")
            print("  -")
            print("---------------------------------------------------")
    print("===================================================")

    
# Function:     write_to_file() - write to empty text file the finished list of character stats
# Parameters:   filename(string) - string of the name of the file to be opened and written into
#               character_list(list) - list of all the characters
def write_to_file(filename, character_list):
    # open file to be written to
    outfile = open(filename, "w")

    # for loop to add all character and all their respective stats
    for i in range(len(character_list)):
        # adding character name and secret identity
        outfile.write(character_list[i].get_name() + "\n")
        outfile.write(character_list[i].get_secret_identity() + "\n")

        # convert get_is_hero boolean to h (true) or v (false)
        if character_list[i].get_is_hero():
            outfile.write("h" + " ")
        else:
            outfile.write("v" + " ")

        # adding character total battles, battles won, battles lost, battles drawn and the current health as a %
        outfile.write(str(character_list[i].get_no_battles()) + " ")
        outfile.write(str(character_list[i].get_no_won()) + " ")
        outfile.write(str(character_list[i].get_no_lost()) + " ")
        outfile.write(str(character_list[i].get_no_drawn()) + " ")
        outfile.write(str(character_list[i].get_health()) + "\n")

    # stop editing file
    outfile.close()
    

# Function:     find_character() - finds character by name from character_list
# Parameters:   character_list(list) - list of all the characters
#               name(string) - name of character to be found
# Returns:      character_position(int) - position of character in character_list, if not found will be -1
def find_character(character_list, name):
    # set a default value for character_position if the name is not in character_list
    character_position = -1

    # for loop to determine the character_position of name in character_list
    for i in range(len(character_list)):
        if name == character_list[i].get_name():
            character_position = i

    return character_position


# Function:     add_character() - adds character by name from character_list
# Parameters:   character_list(list) - list of all the characters
#               name(string) - name of character to be added,
#               secret_id(string) - secret identity of character
#               is_hero(string) - if a character is a hero(h) or a villain (v).
# Returns:      new_character_list(list) - updated character list with added character
def add_character(character_list, name, secret_id, is_hero):
    # set new_character_list by default to the current character_list
    new_character_list = character_list

    # check if character already exists in character_list
    character_index = find_character(character_list, name)

    # if not, add it
    if character_index == -1:
        # add new character to the new list
        new_character = character.Character(name, secret_id, is_hero)
        new_character_list.append(new_character)

        print("\nSuccessfully added", name, "to character list.\n")

    # if it does, return print statement
    else:
        print(name, "already exists in character list.")

    return new_character_list


# Function:     remove_character() - removes character by name from character_list
# Parameters:   character_list - list of all the characters
#               name - name of character to be removed
# Returns:      new_character_list - updated character list with removed character
def remove_character(character_list, name):
    # create new_character_list to add remaining characters to list
    new_character_list = []

    # run find_character function to find the index in the list where the character is
    character_index = find_character(character_list, name)

    # if it returns -1, it does not exits
    if character_index == -1:
            print("\n" + name, "is not found in characters.")

    # otherwise it does
    else:
        # for loop that adds all characters from old list to new list, except for the removed character
        for i in range(len(character_list)):
            if character_list[i] != character_list[character_index]:
                new_character_list.append(character_list[i])
            else:
                print("Successfully removed", name, "from character list.\n")

    return new_character_list


# Function:     do_battle() - Simulates a battle between two opponents.
# Parameters:   character_list(list) - list of character objects.
#               opponent1_pos(int)  - position/index of character in character_list.
#               opponent2_pos(int)  - position/index of character in character_list.
def do_battle(character_list, opponent1_pos, opponent2_pos):
    # ask for user input on how many rounds to battle
    set_rounds = int(input("Please enter number of battle rounds: "))

    # error checking that the rounds are between 1-5
    while set_rounds < 1 or set_rounds > 5:
        print("Must be between 1-5 inclusive\n")
        set_rounds = int(input("Please enter number of battle rounds: "))

    # set a counting variable
    rounds = 0

    print("\n\n-- Battle --\n")

    # run while rounds is less than the set rounds, and both characters are alive
    while rounds < set_rounds and character_list[opponent1_pos].get_health() != 0 and character_list[opponent2_pos].get_health() != 0:
        print(character_list[opponent1_pos].get_name(), "versus", character_list[opponent2_pos].get_name(), "-", set_rounds, "rounds")

        # generate damage for each character
        opponent1_damage = random.randint(0, 50)
        opponent2_damage = random.randint(0, 50)

        # apply damage to the respected character
        character_list[opponent1_pos].update_health(opponent1_damage)
        character_list[opponent2_pos].update_health(opponent2_damage)

        # display damage
        print("\nRound:", (rounds+1))
        print("  >", character_list[opponent1_pos].get_name(), "- Damage:", opponent1_damage, "- Current health:", character_list[opponent1_pos].get_health())
        print("  >", character_list[opponent2_pos].get_name(), "- Damage:", opponent2_damage, "- Current health:", character_list[opponent2_pos].get_health())

        # increase rounds counter variable
        rounds = rounds + 1

    print("\n-- End of battle --\n")

    # setting health to 0 if it is less than, and displaying character died
    if character_list[opponent1_pos].get_health() <= 0:
        character_list[opponent1_pos].set_health(0)
        print("--", character_list[opponent1_pos].get_name(), "has died!  :(")

    # setting health to 0 if it is less than, and displaying character died
    if character_list[opponent2_pos].get_health() <= 0:
        character_list[opponent2_pos].set_health(0)
        print("--", character_list[opponent2_pos].get_name(), "has died!  :(")

    # determine winner, and increase won/lost/draw stat for each character
    if character_list[opponent1_pos].get_health() < character_list[opponent2_pos].get_health():
        print("**", character_list[opponent2_pos].get_name(), "wins! **")
        character_list[opponent1_pos].increment_no_lost()
        character_list[opponent2_pos].increment_no_won()

    elif character_list[opponent1_pos].get_health() > character_list[opponent2_pos].get_health():
        print("**", character_list[opponent1_pos].get_name(), "wins! **")
        character_list[opponent1_pos].increment_no_won()
        character_list[opponent2_pos].increment_no_lost()

    else:
        print("** Draw! **")
        character_list[opponent1_pos].increment_no_drawn()
        character_list[opponent2_pos].increment_no_drawn()

    # increase number of battles stat for each character
    character_list[opponent1_pos].increment_no_battles()
    character_list[opponent2_pos].increment_no_battles()


# Function:     main() - holds interactive code
def main():
    display_details()

    # constant for maximum health of characters
    MAX_HEALTH = 100

    # Define the character list to store character (hero and villain) information
    character_list = read_file("characters.txt")

    # define choice
    choice = ""

    # loop program as long as choice is not 'quit'
    while choice != "quit":

        # ask for user input from a list of commands
        print("\nPlease enter choice")
        choice = input("[list, heroes, villains, search, reset, add, remove, battle, quit]: ")

    # run through commands as user inputs

        # quit program, run write_to_file function
        if choice == "quit":
            write_to_file("new_characters.txt", character_list)

        # run display_characters function, showing all characters
        elif choice == "list":
            display_characters(character_list, 0)

        # run display_characters function, showing only hero characters
        elif choice == "heroes":
            display_characters(character_list, 1)

        # run display_characters function, showing only villain characters
        elif choice == "villains":
            display_characters(character_list, 2)

        # run find_character function, and display all individual stats
        elif choice == "search":
            character_name = input("\nPlease enter name: ")
            character_index = find_character(character_list, character_name)

            # determine if character exists
            if character_index == -1:
                print("\n" + character_name, "is not found in character (heroes and villains) list.\n")

            else:
                # determine if character is hero or villain
                if character_list[character_index].get_is_hero():
                    print("\nAll about", character_list[character_index].get_name(), "--> HERO")

                else:
                    print("\nAll about", character_list[character_index].get_name(), "--> VILLAIN")

                # display all character stats
                print("")
                print("Secret identity: " + character_list[character_index].get_secret_identity())
                print("")
                print("Battles fought: " + str(character_list[character_index].get_no_battles()))
                print("  > No won:   " + str(character_list[character_index].get_no_won()))
                print("  > No lost:  " + str(character_list[character_index].get_no_lost()))
                print("  > No drawn: " + str(character_list[character_index].get_no_drawn()))
                print("")
                print("Current health:  " + str(character_list[character_index].get_health())+"%\n") # #

        # run find_character to find the index of the character, and reset health to MAX_HEALTH
        elif choice == "reset":
            # ask user for name of character to reset health
            character_name = input("\nPlease enter name: ")

            # find index for character
            reset_character_index = find_character(character_list, character_name)

            # check if the character exists
            if reset_character_index == -1:
                print("\n" + character_name, "is not found in character (heroes and villains) list.\n")

            # reset health and display to the user that it has happened
            else:
                character_list[reset_character_index].set_health(MAX_HEALTH)
                print("\nSuccessfully updated", character_list[reset_character_index].get_name() + "'s health to", str(character_list[reset_character_index].get_health()), "\n")

        # ask for new character details, add new character to character list
        elif choice == "add":
            # ask user for character details
            character_name = input("\nPlease enter name: ")
            secret_identity = input("Please enter secret_identity: ")
            hero = input("Is this character a hero or a villain [h|v]? ")

            # change hero letter to boolean variable
            if hero == "h":
                hero = True

            else:
                hero = False

            # run add_character function to add new character to character list
            character_list = add_character(character_list, character_name, secret_identity, hero)

        # ask for character name and run remove_character function
        elif choice == "remove":
            # ask for character name
            name = input("\nPlease enter name: ")

            character_list = remove_character(character_list, name)

        # ask for both opponent's names, find them using find_character, run do_battle
        elif choice == "battle":
            # ask for opponent1 name and check that they exist
            opponent1 = input("\nPlease enter opponent one's name: ")
            while opponent1 not in character_list:
                if opponent1 not in character_list:
                    print(opponent1, "is not found in character list - please enter another opponent!\n")
                opponent1 = input("Please enter opponent one's name: ")

            # ask for opponent2 name and check that they exist
            opponent2 = input("Please enter opponent two's name: ")
            while opponent2 not in character_list:
                if opponent2 not in character_list:
                    print(opponent2, "is not found in character list - please enter another opponent!\n")
                opponent2 = input("Please enter opponent two's name: ")

            # find both opponent's position in character_list using find_character
            opponent1_pos = find_character(character_list, opponent1)
            opponent2_pos = find_character(character_list, opponent2)

            # run do_battle
            do_battle(character_list, opponent1_pos, opponent2_pos)

        # command is invalid
        else:
            print("\nNot a valid command - please try again.\n")

    print("\n\n-- Program terminating --\n")


main()
