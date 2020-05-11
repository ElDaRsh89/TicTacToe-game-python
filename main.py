import random
import time

board = ("""
   |   |  
 ---------- 
   |   |  
 ----------
   |   |   
    """)
empty_board = ("""
   |   |  
 ---------- 
   |   |  
 ----------
   |   |   
    """)
# The keys of this dictionary are the positions of the numbers corresponding to cells on a Tic Tac Toe board that
# the user or the computer will choose. The valuse are the index positions of these number in the "The board" string.
positions_dict = {1: 2, 2: 6, 3: 10, 4: 26,
                  5: 30, 6: 34, 7: 49, 8: 53, 9: 57
                  }

# A list of all the possible combinations that will cause a user to win.
win_positions = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
    (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)
]

# Converting the win patterns to index positions in "The board" string
converted_win_positions = []
for tup in win_positions:
    converted_list = []
    for pos in tup:
        converted_num = positions_dict[pos]
        converted_list.append(converted_num)
    converted_win_positions.append(converted_list)


# print(converted_win_positions)

# The "Win" function will take a board as an argument and checks if this board has a winning pattern
# from the above list.
# It loops over each line in the win patterns and checks if the indices of that line in the given board
# are filled with "X" or "O". If so, it will return True.
def win(boarda):
    for line in converted_win_positions:
        if boarda[line[0]] == "X" \
                and boarda[line[1]] == "X" \
                and boarda[line[2]] == "X":
            return True
        if boarda[line[0]] == "O" \
                and boarda[line[1]] == "O" \
                and boarda[line[2]] == "O":
            return True


# This function just replaces the space at the index position in a board corresponding to the input number the user or
# the computer chose. The position is the user input. Symbol is either "X" or "O". Boarda is any board passed to it.
# The function returns the given board with the indicated space replaced with the Symbol.
def put_symbol_on_board(position, symbol, boarda):
    converted_position = positions_dict[position]
    first_part = boarda[0:converted_position]
    sec_part = symbol
    third_part = boarda[converted_position + 1:]
    joined_string = first_part + sec_part + third_part
    return joined_string


# Takes a user input and returns a valid integer between 1-9.
# If the user wrote a letter ( cannot convert letter to int on line 69), it will cause a ValueError and the function
# will print "Invalid input"and ask the user again for a valid input and restart the while loop(pass).
# If the user put an integer, on line 72 the function will make sure it is in range(10). if not it will ask the user
# for a valid number.
# The loop will ONLY break if and ONLY if the user put a valid number.(the break statement on line 78)
def choice_validator(user_inp):
    inner_number = user_inp
    while True:
        try:
            inner_number = int(inner_number)
            if inner_number not in range(1, 10):
                print("Choice must be between 1 and 9")
                inner_number = input("Enter a number from 1 to 9: ")
                continue
            break
        except ValueError:
            print("Invalid Input")
            inner_number = input("Enter a number from 1 to 9: ")
            pass
    return inner_number


# There are 3 while loops:
# The first (while yes) will keep the program running until the user doesn't want to play, only then will the program
# end.
# The second (while game) will keep the game running until either the user or the computer wins.
# The third (while not cycle_finished) will keep each cycle running (the cycle is 2 choices; one for each player) until
# both players have chosen a cell or until one of them wins.
def play_game():
    yes = True
    while yes:
        game = True
        new_board = board
        # a list with numbers from 1 to 9. During a game the number chosen by a user or computer will be removed from it.
        positions_list = list(range(1, 10))
        while game:
            cycle_finished = False  # the cycle finished when computer puts an "O" in a cell.
            while not cycle_finished:
                print("\n", "         Tic Tac Toe           ", end="\n" * 2)
                # The first board that will appear to the user. Of course an empty one. (line 88)
                print("First", new_board, end="\n" * 2)
                # 1) the user input will be validated by the validator function and the correct input will be stored in
                # the choice variable.
                choice = choice_validator(input("Choose a cell by entering a number from 1 to 9 \nYour Choice: "))
                # 2) If choice is not in positions list, that means it is played already
                while choice not in positions_list:
                    print("Cell already has an input")
                    choice = choice_validator(input("Pick a cell: "))
                else:  # choice not played before.
                    positions_list.remove(choice)
                    # 3) After choice is OK. put the choice on the empty board and store the new board in
                    # the same variable.
                    new_board = put_symbol_on_board(choice, "X", new_board)
                    print("One", new_board)  # Showing the user his symbol on the board.

                    # 4) In this cycle in the game, if that choice made a win pattern complete, game will be false and
                    # the cycle will break skipping the computer choice. When the next lines check if cycle_finished
                    # is still false, it will find it true and will check game which will be False and the game will end
                    if win(new_board):
                        print("You Won")
                        game = False
                        cycle_finished = True

                    else:  # meaning the user choice didn't make him win.
                        time.sleep(1)
                        if not cycle_finished:
                            positions_list = positions_list  # update positions list after removing the previous users
                            # choice
                            # 5) Check if the user picked the last cell in the board which corresponds to an
                            # empty positions list. If so, then it is a tie. If this choice was a winning pattern,
                            # the game would have ended on line 128.
                            if len(positions_list) == 0:
                                print("       TIE    ")
                                game = False
                                cycle_finished = True
                            else:  # There are still numbers not picked.
                                if game:
                                    # 6) Where should the computer put the next "O"?
                                    # Firstly : The program will loop over each position left and put an "O" in
                                    # that position.
                                    for position in positions_list:
                                        fict_ai_board_two = put_symbol_on_board(position, "O", new_board)
                                        # If the resulting board has a winning pattern, the board will be updated like
                                        # that and the game will finish as the computer has won. else (line 164),
                                        # continue to the next position.
                                        if win(fict_ai_board_two):
                                            cycle_finished = True
                                            game = False
                                            new_board = put_symbol_on_board(position, "O", new_board)
                                            # time.sleep(1)
                                            print(new_board)
                                            time.sleep(1)
                                            print("You Lost")
                                            break  # the for loop. Stop trying other positions.
                                        else:  # This position will not result in a winning pattern.
                                            continue
                                    # After finishing looping over all positions, check if game is still True. if not
                                    # break the cycle and the game is finished.

                                    if game:
                                        # Secondly: The program will loop again over each position but this time it will
                                        # put an "X" in the position and see if the user will win if the user put "X" in
                                        # the next cycle.
                                        # If so, the computer will put an "O" in that position.
                                        for position in positions_list:
                                            fict_ai_board = put_symbol_on_board(position, "X", new_board)
                                            if win(fict_ai_board):  # if this position will make the user win
                                                new_board = put_symbol_on_board(position, "O", new_board)
                                                positions_list.remove(position)
                                                cycle_finished = True
                                                break
                                            else:
                                                continue
                                        # After the 2 loops finished and still no "O' was put (cycle_finished still
                                        # False) then, choose a random position from positions list and put "O" in it.
                                        if not cycle_finished:
                                            comp_choice = random.choice(positions_list)
                                            new_board = put_symbol_on_board(comp_choice, "O", new_board)
                                            positions_list.remove(comp_choice)
        #  If for any reason, game is False and its while loop finished looping, then before going to the uppermost
        # while loop(yes loop) ask the user if he wants to play again. Then check the "While yes" loop.
        check_play_again = input("Do you want to play again? (Y/N) : ").upper()
        while check_play_again.upper() not in ("Y", "N"):
            check_play_again = input("Do you want to play again? (Y/N) : ").upper()
        if check_play_again == "N":
            yes = False
        else:
            yes = True


play_game()
