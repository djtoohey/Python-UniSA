#
# Dice Poker
# Dice module - Assignment 1, sp2, 2019.
#

# Function display_hand to display the face value of dice to the screen.
# This function takes a list of integers as a parameter (i.e. the values of the
# five die to display) and displays the dice to the screen.
# Parameters:  List storing five die face values.
# Returns: Nothing is returned from the function.
def display_hand(hand, max_dice):
    
    # Display die number to the screen.
    print(format("", '<15s'), end='')
    for i in range(max_dice):
        print(format("Die " + str(i+1), '<10s'), end='')
    print()
    
    # Display face value of die to the screen.
    print(format("", '<16s'), end='')
    for i in range(max_dice):
          print(format("[" + str(hand[i]) + "]", '<10s'), end='')
    print()

    # Display the top row of face value to the screen.
    print(format("", '<16s'), end='')
    for i in range(max_dice):
        if hand[i] == 1:
            print(format(" ", '<10s'), end='')
        elif hand[i] == 2 or hand[i] == 3:
            print(format("*", '<10s'), end='')
        elif hand[i] == 4 or hand[i] == 5 or hand[i] == 6:
            print(format("* *", '<10s'), end='')
    print()

    # Display the middle row of face value to the screen.
    print(format("", '<16s'), end='')
    for i in range(max_dice):       
        if hand[i] == 1 or hand[i] == 3 or hand[i] == 5:
           print(format(" *", '<10s'), end='')
        elif hand[i] == 6:
           print(format("* *", '<10s'), end='')
        else:
           print(format(" ", '<10s'), end='')
    print()

    # Display the bottom row of face value to the screen.
    print(format("", '<16s'), end='')
    for i in range(max_dice):
        if hand[i] == 1:
            print(format(" ", '<10s'), end='')
        elif hand[i] == 2 or hand[i] == 3:
            print(format("  *", '<10s'), end='')
        elif hand[i] == 4 or hand[i] == 5 or hand[i] == 6:
            print(format("* *", '<10s'), end='')
    print()
    

    
