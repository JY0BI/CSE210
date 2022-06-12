# Assignment for Week 1
# Author: Jordan Ellington

# Defining some variables

first = 1
second = 2
third = 3
fourth = 4
fifth = 5
sixth = 6
seventh = 7
eighth = 8
ninth = 9

# Update function to run at beginning and after every input
def update_numbers(a, b, c, d, e, f, g, h, i):
    number_values = [a, b, c, d, e, f, g, h, i]
    return number_values

# Print Game function prints the game as it currently exists.
def print_game(num):
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(num[0],num[1],num[2],sep=" | ")
    print("--+---+--")
    print(num[3],num[4],num[5],sep=" | ")
    print("--+---+--")
    print(num[6],num[7],num[8],sep=" | ")
    print("")

# TurnChange Defines which turn it is currently
def turn_change(turn):
    if turn == "X":
        turn = "O"
        return turn
    elif turn == "O":
        turn = "X"
        return turn
    else:
        print("error")

#If input switcher
def position_mapper(input):
    position = input - 1
    return position

#Turn process for each player.    
def take_your_turn(turn, number_values):
    question = turn + "'s turn to choose a square (1-9): "
    user_input = int(input(question))
    num_position = position_mapper(user_input)
    number_values[num_position] = turn

#WinChecker
def win_checker(num):
    if num[0] == num[1] and num[0] == num[2]:
        won = 1
        return won
    elif num[3] == num[4] and num[3] == num[5]:
        won = 1
        return won
    elif num[6] == num[7] and num[6] == num[8]:
        won = 1
        return won
    elif num[0] == num[3] and num[0] == num[6]:
        won = 1
        return won
    elif num[1] == num[4] and num[1] == num[7]:
        won = 1
        return won
    elif num[2] == num[5] and num[2] == num[8]:
        won = 1
        return won
    elif num[0] == num[4] and num[0] == num[8]:
        won = 1
        return won
    elif num[2] == num[4] and num[2] == num[6]:
        won = 1
        return won
    else:
        won = 0
        return won

# The Actual Game
def main():
    won = 0
    turn = "X"
    turns_passed = 0
    number_values = update_numbers(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth)
    print("Let's Play Tic-Tac Toe!")
    print_game(number_values)
    turn = "X"
    while won != 1:
        take_your_turn(turn, number_values)
        won = win_checker(number_values)
        print_game(number_values)
        if won == 1:
            print("The winner is team ", turn)
            print("")
        else:
            turn = turn_change(turn)
        turns_passed = turns_passed + 1
        if turns_passed == 9:
            won = 1
            print("It's a Draw!")
            print("")

main()