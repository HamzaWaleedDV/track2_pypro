theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        try:
            printBoard(theBoard)
            print(f'It is your turn, {turn}. Move to which place?')

            move = input()

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count +=  1

            else:
                print("That place is already filled. \nMove to whivhe place?")
                continue

            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    

                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})                        
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    

                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})                        
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    
            
                elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})                        
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    

                elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':  
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})                        
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    

                elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})                        
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    

                elif theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ':
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})                        
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    

                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print('\nGame Over')
                    print(f'**** {turn} won. *****')
                    print('You want play again?(Y/N) ')
                    play = input()
                    if play.upper() == 'Y':
                        theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})                        
                        game()
                    elif play.upper() == 'N':
                        exit()
                    else:
                        exit()    

            if count == 9:
                print("\nGame Over\n")
                print('It is Tie!!')

                print('You want play again?(Y/N) ')
                play = input()
                if play.upper() == 'Y':
                    theBoard.update({'7': ' ', '8': ' ', '9': ' ',
                                         '4': ' ', '5': ' ', '6': ' ',
                                         '1': ' ', '2': ' ', '3': ' '})
                    game()
                elif play.upper() == 'N':
                    exit()
                else:
                    exit()    

            if turn == 'X':
                turn = '0'
            else:
                turn = 'X' 
        except KeyError:
            print("Please enter a number from 1 to 9 Only!!")        

if __name__ == "__main__":
    game()