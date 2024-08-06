from search import *
import os

class Problem:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.current_winner = None

    def print_board(self):
        print("  " + "   ".join(map(str, range(8))))
        for i, row in enumerate(self.board):
            print(str(i) + " " + " | ".join(row) + " ")
            if i < 7:
                print("  " + "--+" + "---+" * 6 + "---")

    def empty_squares(self):
        return ' ' in [square for row in self.board for square in row]

    def is_valid(self, square):
        row, col = square
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        if self.board[row][col] != ' ':
            return False
        return True

    def make_move(self, square, marker):
        row, col = square
        if self.is_valid(square):
            self.board[row][col] = marker
            if self.check_winner(square, marker):
                self.current_winner = marker
            return True
        return False

    def undo_move(self, square):
        row, col = square
        self.board[row][col] = ' '

    def check_winner(self, square, marker):
        row, col = square
        # Check row
        count = 0
        for c in range(8):
            if self.board[row][c] == marker:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check column
        count = 0
        for r in range(8):
            if self.board[r][col] == marker:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check diagonals
        count = 0
        for i in range(-3, 4):
            r, c = row + i, col + i
            if 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == marker:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        count = 0
        for i in range(-3, 4):
            r, c = row + i, col - i
            if 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == marker:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False


    def available_moves(self):
        return [(r, c) for r in range(8) for c in range(8) if self.board[r][c] == ' ']

    def is_terminal(self):
        return self.current_winner is not None or not self.empty_squares()

    def utility(self, computer_marker):
        if self.current_winner == computer_marker:
            return 1
        elif self.current_winner is None:
            return 0
        else:
            return -1

class GamePlay:
    def __init__(self):
        self.player = None
        self.computer = None

    def choose_marker(self):
        while True:
            marker = input("Do you want to be X or O? ").upper()
            if marker == 'X':
                self.player = 'X'
                self.computer = 'O'
                return
            elif marker == 'O':
                self.player = 'O'
                self.computer = 'X'
                return
            else:
                print("Invalid choice. Please choose X or O.")

    def is_valid_move(self, move):
        if len(move) != 2 or not all(char.isdigit() for char in move):
            return False
        return True

    def player_turn(self, game):
        move = input("Enter your move (row col): ").split()
        if not self.is_valid_move(move):
            return False
        else:
            row, col = map(int, move)
            if game.make_move((row, col), self.player):
                os.system('cls')  # Nếu bạn dùng Windows
                # os.system('clear')  # Nếu bạn dùng MacOS
                game.print_board()
                return True
            else:
                return False

    def computer_turn(self, search_strategy, game):
        move = search_strategy.alpha_beta_search(game)
        game.make_move(move, self.computer)
        os.system('cls')  # Nếu bạn dùng Windows
        # os.system('clear')  # Nếu bạn dùng MacOS
        print(f"Computer moves to {move}")
        game.print_board()
     
    def check_result(self, game):
        if game.current_winner == self.player:
            print("You win!")
        elif game.current_winner == self.computer:
            print("Computer wins!")
        else:
            print("It's a tie!")
           
    def play_game(self, game):
        self.choose_marker()
        search_strategy = SearchStrategy(self.player, self.computer)
        
        game.print_board()
        
        current_marker = 'X'

        while game.empty_squares():
            if current_marker == self.player:
                if self.player_turn(game):
                    if game.is_terminal():
                        break
                    current_marker = self.computer
                else:
                    print("Invalid move. Try again.")
            else:
                self.computer_turn(search_strategy, game)
                if game.is_terminal():
                    break
                current_marker = self.player

        self.check_result(game)

if __name__ == '__main__':
    problem = Problem()
    game = GamePlay()
    game.play_game(problem)
