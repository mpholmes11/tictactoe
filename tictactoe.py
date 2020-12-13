def tictactoe():
    # open spots
    available_spots = ['1','2','3','4','5','6','7','8','9']

    # player positions
    game_board = {
        '1': ' ',
        '2': ' ',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': ' ',
        '8': ' ',
        '9': ' '
    }

    winning_combos = (
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7'])

    # Print available spots and game board
    def board_check():

        print("Available Spots:","Game Board:".rjust(15))
        print(f"{available_spots[0]} | {available_spots[1]} | {available_spots[2]}", f"{game_board['1']} | {game_board['2']} | {game_board['3']}".rjust(20))
        print(f"{available_spots[3]} | {available_spots[4]} | {available_spots[5]}", f"{game_board['4']} | {game_board['5']} | {game_board['6']}".rjust(20))
        print(f"{available_spots[6]} | {available_spots[7]} | {available_spots[8]}", f"{game_board['7']} | {game_board['8']} | {game_board['9']}".rjust(20))
    
    board_check()

    winner = False
    turns = 0
    x_spots = []
    o_spots = []

    while winner is False:

        # X's TURN

        if turns % 2 == 0:
            x = input("X's turn. Pick a spot: ")
              
            # INVALID INPUT CHECK
            if x not in available_spots or x.isdigit() == False:
                  print(f'"{x}" is not a valid selection...try again')
            
            # IF INPUT OK AND SPOT OPEN
            while x in available_spots and x.isdigit() == True:

                # SET POSITION ON GAME BOARD
                game_board[str(x)] = 'X'

                for n,i in enumerate(available_spots):
                    if x in i:
                        # ADD TO X POSITION LIST FOR CHECK LATER AGAINST WINNING COMBOS
                        x_spots.append(available_spots[n])
                        # REMOVE POSITION FROM AVAILABLE SPOTS BUT LEAVE SPACE FOR AESTHETICS lol
                        available_spots[n] = ' '
                        turns += 1
                        board_check()

        # O'S TURN

        elif turns % 2 != 0:
            o = input("O's turn. Pick a spot: ")
              
            # INVALID INPUT CHECK
            if o not in available_spots or o.isdigit() == False:
                  print(f'"{o}" is not a valid selection...try again')
            
            # IF INPUT OK AND SPOT OPEN
            while o in available_spots and o.isdigit() == True:

                # SET POSITION ON GAME BOARD
                game_board[str(o)] = 'O'

                for n,i in enumerate(available_spots):
                    if o in i:
                        # ADD TO X POSITION LIST FOR CHECK LATER AGAINST WINNING COMBOS
                        o_spots.append(available_spots[n])

                        # REMOVE POSITION FROM AVAILABLE SPOTS BUT LEAVE SPACE FOR AESTHETICS lol
                        available_spots[n] = ' '
                        turns += 1
                        board_check()

        # WINNER CHECK
        for combo in winning_combos:
            if all(c in x_spots  for c in combo):
                print("\nGAME OVER - X Wins!!!\n")
                winner = True
            elif all(c in o_spots  for c in combo):
                print("\nGAME OVER - O Wins!!!\n")
                winner = True

        # NO WINNER AFTER 9 TURNS
        if turns == 9 and winner is False:
            print ("Rats! Its a tie.. nobody wins...")
            break
        else:
            pass

tictactoe()

