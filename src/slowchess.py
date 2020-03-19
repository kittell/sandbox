class Square:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.piece = None
        
    
class Row:
    def __init__(self, r):
        self.r = r
        
        n_squares = 8
        self.squares = []
        for i in range(n_squares):
            self.squares.append(Square(r, i))

class Board:
    def __init__(self):
        n_rows = 8
        self.rows = []
        for i in range(n_rows):
            self.rows.append(Row(i))
        
    def initiate(self):
        pass
        
class Game:
    def __init__(self):
        pass
    
    def new_game(self):
        self.board = Board()
        
    def load_game(self):
        pass


game = Game()
game.new_game()

board = game.board
for row in board.rows:
    for square in row.squares:
        print((square.r, square.c))
