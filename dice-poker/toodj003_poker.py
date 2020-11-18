# File      : toodj003_poker.py
# Author    : Declan Toohey
# Email Id  : toodj003
# Version: 5.0 30 April 2019
# Description: Assessment 1 - Dice Poker Game.
# This is my own work as defined by the University's
# Academic Misconduct policy.

# importing dice and random modules
import dice
import random

NUM_ROLLS = 5   # Declaring the number of rolls that the player and dealer roll as a constant

games_played = 0    # Declaring the amount of games played
games_won = 0       # Declaring the amount of games won
games_lost = 0      # Declaring the amount of games lost
games_draw = 0      # Declaring the amount of games drew


# Function that displays Uni details to program
def display_details():
    print("File     : toodj003_poker.py")
    print("Author   : Declan Toohey")
    print("Stud ID  : 110284360")
    print("Email ID : toodj003")
    print("This is my own work as defined by the")
    print("University's Academic Misconduct Policy.")
    print("")


# Function that generates random number between 1 and 6, and returns value generated
def roll_die():
    roll = random.randint(1, 6)     # Generate random number between 1 and 6, and assign it to roll
    return roll     # Return random number generated


# Function that takes the maximum amount of rolls (5), creates a new list and puts random numbers generated
# from roll_die, into the new list and returns this list
def deal_hand(max_dice):
    current_hand = []   # Declaring list
    current_roll = 0    # Set loop to 0
    while current_roll < max_dice:
        roll = roll_die()   # set roll to a random number generated from roll_die function
        current_hand.append(roll)   # adds roll to list
        current_roll += 1   # moves loop along
    return current_hand     # returns list


# Function that counts how many of each number is in the respective player's hand.
def count_die(hand, hand_die_count):
    for num in range(len(hand)):    # declare num as the control variable and loops through the length of the list of the hand
        die_value = hand[num]       # To access the list element
        hand_die_count[die_value] = hand_die_count[die_value] + 1   # To update the list element


# Function that checks what rank the current player is in an integer value.
def rank_check(current_rank, possible_new_rank):
    if current_rank < possible_new_rank:    # checking if current rank is smaller than the new rank
        current_rank = possible_new_rank    # set current rank to the value of new rank
    return current_rank                     # return back the rank


# Function that ranks the hand into an integer value
def rank_hand(hand, max_dice):
    rank = 0    # Declare what the current rank is
    for i in range(max_dice):   # Loop looping through the die_counters for the repected hand.
        if hand[i] == 2:        # if i is two, therefore there is a pair
            # print("pair")
            new_rank = 1
            for j in range(max_dice):   # loop a second time to see if there is a second pair
                if hand[j] == 2:        # if j is two, therefore there is a pair
                    if j != i:          # but if i is j, it is the same pair, otherwise there is a second pair
                        # print("2 pairs")
                        new_rank = 2
        elif hand[i] == 3:      # check if there is three of a kind
            # print("three of a kind")
            new_rank = 3
            for j in range(max_dice):   # loop a second time to see if there is a pair as well as a three of a kind
                if hand[j] == 2:        # check to see if there is a pair, if so, it is a full house
                    # print("full house")
                    new_rank = 4
        elif hand[i] == 4:              # check if there is a four of a kind
            # print("four of a kind")
            new_rank = 5
        elif hand[i] == 5:              # check if there is a five of a kind
            # print("five of a kind")
            new_rank = 6
        else:                           # if there is nothing special, set rank to 0
            # print("Nothing special")
            new_rank = 0
        rank = rank_check(rank, new_rank)   # run rank_check to see if the new rank is better than the previous rank
    return rank     # return the rank value


# Function that displays the rank that the player and dealer got, using the integer values gotten from rank_hand
def display_rank(rank):
        if rank == 1:                   # if rank is 1, it was a pair
            print("One pair")
        elif rank == 2:                 # if rank is 2, there were two pair
            print("Two pairs")
        elif rank == 3:                 # if rank is 3, there were three of a kind
            print("Three of a kind")
        elif rank == 4:                 # if rank is 4, there was a pair and a three of a kind, a full house
            print("Full house")
        elif rank == 5:                 # if rank is 5, there were four of a kind
            print("Four of a kind")
        elif rank == 6:                 # if rank is 6, there were five of a kind
            print("Five of a kind")
        else:                           # otherwise, nothing special
            print("Nothing special")


# Begin of program running
display_details()

play = input("Would you like to play dice poker [y|n]? ").lower()       # declare play and ask for input y or n
while play != "y" and play != "n":                              # loop to ensure that y or n has been input
    print("Please enter either 'y' or 'n'.")
    print("")
    play = input("Would you like to play Dice Poker? [y|n]? ").lower()

if play == "n":         # if from start up player does not want to play, print the below
    print("No worries... another time perhaps... :)")

while play == "y":      # loop as long as the player wants to play

    player_die_count = [0, 0, 0, 0, 0, 0, 0]    # declare the player's die counter
    dealer_die_count = [0, 0, 0, 0, 0, 0, 0]    # declare the dealers's die counter

    games_played += 1   # increase games played by one each time the game is played
    player_hand = deal_hand(NUM_ROLLS)      # declare player hand and set it with deal_hand function
    dealer_hand = deal_hand(NUM_ROLLS)      # declare dealer hand and set it with deal_hand function

    count_die(player_hand, player_die_count)    # count how many times each dice number came up for the player's hand
    count_die(dealer_hand, dealer_die_count)    # count how many times each dice number came up for the dealer's hand

    print("Player's hand:")
    dice.display_hand(player_hand, NUM_ROLLS)   # display visual dice for player's rolls
    print("Dealer's hand:")
    dice.display_hand(dealer_hand, NUM_ROLLS)   # display visual dice for dealer's rolls

    player_rank = rank_hand(player_die_count, len(player_die_count))    # declare player's rank and set it using rank_hand
    dealer_rank = rank_hand(dealer_die_count, len(dealer_die_count))    # declare player's rank and set it using rank_hand

    # printing the player's and dealer's rank with spacing
    print("")
    print("-- Player has ", end="")
    display_rank(player_rank)
    print("-- Dealer has ", end="")
    display_rank(dealer_rank)
    print("")

    # determine who the winner is, display the result and add it to the running total of games won/lost/drew
    if player_rank > dealer_rank:
        print("** Player wins! **")
        games_won += 1
    elif player_rank < dealer_rank:
        print("** Dealer wins! **")
        games_lost += 1
    else:
        print("** Draw! **")
        games_draw += 1
    print("")
    print("")

    # asking if player wants to play again and error checking to ensure correct input y or n.
    play = input("Play again [y|n]? ").lower()
    while play != "y" and play != "n":
        print("Please enter either 'y' or 'n'.")
        print("")
        play = input("Play again [y|n]? ").lower()
        

# once player is done playing, print game summary
if games_played > 0:        # if statement ensures that the game was played at least once.
    print("")
    print("")
    print("Game Summary")
    print("============")
    print("You played", games_played, " games")
    print("  |--> Games won: ", games_won)
    print("  |--> Games lost: ", games_lost)
    print("  |--> Games drawn: ", games_draw)
    print("")
    print("Thanks for playing!")

