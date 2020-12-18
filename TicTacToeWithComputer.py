import random
import sys
import os


board =[" ", " ", " ", " ", " ", " ", " ", " ", " "]

class Game:
    def __init__(self):
        self._place = 0

    def drawBoard(self):
        for i in range(3):
            print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
            if i != 2:
                print("---------")
    def isValidPosition(self, pos):
        if board[pos] == " ":
            self._place = pos
            return True
        return False
    def placeOnBoard(self, tac):
        board[self._place] = tac
    def isOver(self):
        if all(board[i] != " " for i in range(9)):
            return True
        return False
    def checkForWin(self):
        diagonal_left = [0, 4, 8]
        diagonal_right = [2, 4, 6]
        tac = board[self._place]
        for i in range(3):
            if all(board[i*3+j] == tac for j in range(3)):
                return True
            elif all(board[i+j*3] == tac for j in range(3)):
                return True
        if all(board[i] == tac for i in diagonal_left):
            return True
        elif all(board[i] == tac for i in diagonal_right):
            return True
    def restart(self):
        for i in range(9):
            board[i] = ' '
        os.system('cls')
        main()

class HumanPlayer:
    def __init__(self):
        self.tac = ""
    def choosePlace(self):
        pos = input("Enter your place between (0-8): ")
        return pos

class ComputerPlayer:
    def __init__(self):
        self.tac = ""
    def choosePlace(self):
        pos = random.randint(0, 8)
        return pos

def main():
    game = Game()
    player_a = HumanPlayer()
    player_b = ComputerPlayer()

    player_a.tac = input("Player 1, choose your TAC (X/O): ").upper()
    if player_a.tac == 'X':
        player_b.tac = 'O'
    else:
        player_b.tac = 'X'
    print(f"Player 2's TAC is \'{player_b.tac}\' \n")

    while True:
        while True:
            try:
                place = int(player_a.choosePlace())
                if game.isValidPosition(place):
                    game.placeOnBoard(player_a.tac)
                    break
                else:
                    print("Invalid Position")
            except Exception as e:
                print("Error: Invalid Input")
        if game.checkForWin():
            game.drawBoard()
            print("Player 1 won!")
            restart = input("Play Again?(y/n): ").lower()
            if restart == 'y':
                game.restart()
            else:
                sys.exit(0)
        if game.isOver():
            game.drawBoard()
            print("Game Over!")
            restart = input("Play Again?(y/n): ").lower()
            if restart == 'y':
                game.restart()
            else:
                sys.exit(0)
            
        while True:
            try:
                place = int(player_b.choosePlace())
                if game.isValidPosition(place):
                    game.placeOnBoard(player_b.tac)
                    break
            except:
                pass
        if game.checkForWin():
            game.drawBoard()
            print("Player 2 won!")
            restart = input("Play Again?(y/n): ").lower()
            if restart == 'y':
                game.restart()
            else:
                sys.exit(0)
        game.drawBoard()
        if game.isOver():
            print("Game Over!")
            restart = input("Play Again?(y/n): ").lower()
            if restart == 'y':
                game.restart()
            else:
                sys.exit(0)

if __name__ == "__main__":
    main()
