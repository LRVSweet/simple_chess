# create list of chess board rows and columns
rows = [i + 1 for i in range(8)]
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

# create empty chess_board dictionary.  Keys will be square names, values will be piece names
chess_board = {}

# create empty dictionary for square objects where keys will be square names and values will be square objects
square_objects = {}

# create a list of 8 empty lists, one for each row of chessboard.  First list will be 8th rank, second will be 7th, etc.  Will be populated with square objects in order conducive to printing their symbols for visualization
square_objects_for_viz = [[] for i in range(8)]

# empty list that will be populated with the pgn code for each move made
game = []

# dictionary of each piece's pgn abbreviation, used for building game list
piece_abbreviations = {"pawn": "", "rook": "R", "knight": "N", "bishop": "B", "king": "K", "queen": "Q"}

# create chess_board dictionary with key for each square
for column in columns:
    for row in rows:
        chess_board[column + str(row)] = ""

# define square class - squares on the chessboard
class Square:

    def __init__(self, name):
        self.name = name
        self.file = name[0]
        self.rank = name[1]
        self.file_index = columns.index(self.file)
        self.rank_index = rows.index(int(self.rank))
        self.symbol = "."
        self.occupant = ""
        square_objects[self.name] = self
        square_objects_for_viz[-self.rank_index + 7].append(self) # assembles square_objects_for_viz with eigth rank list at index 0, proceeding in reverse order to subsequent ranks (i.e. [[rank_8],[rank_7],...,[rank_1]]).  This facilitates printing the visualiztion.

    def __repr__(self):
        return self.name

# method for adding a new occupant to a square
    def change_occupant(self, new_occupant):
        self.occupant = new_occupant
        self.symbol = new_occupant.abbreviation

# method for removing an occupant from a square
    def remove_occupant(self):
        self.symbol = "."

# define pawn class
class Pawn:
    piece = "pawn"

    def __init__(self, name, color, homesquare):
        self.name = name
        self.color = color  # set color
        chess_board[homesquare] = [self, color, self.piece]  # place piece on square by updating chess_board dictionary
        if self.color == "white":
            self.abbreviation = "P"
        else:
            self.abbreviation = "p"
        square_objects[homesquare].change_occupant(self)

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        square_objects[self.square].remove_occupant()
        self.square = destination_square  # set new square attribute
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square
        square_objects[destination_square].change_occupant(self)
        
    def get_captured(self, capturing_piece):
        print(
            "A {color_captured} {captured_piece} on {captured_square} was captured by a {color_capturing} {capturing_piece}.".format(
                color_captured=self.color, captured_piece=self.piece, captured_square=self.square,
                color_capturing=capturing_piece.color,
                capturing_piece=capturing_piece.piece))  # print notice that piece was captured, by what, and where
        self.square = "captured"  # set destination to captured to indicate piece is no longer in play


# define rook class
class Rook:
    piece = "rook"

    def __init__(self, name, color, homesquare):
        self.name = name
        self.color = color  # set color
        chess_board[homesquare] = [self, color, self.piece]  # place piece on square by updating chess_board dictionary
        if self.color == "white":
            self.abbreviation = "R"
        else:
            self.abbreviation = "r"
        square_objects[homesquare].change_occupant(self)

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        square_objects[self.square].remove_occupant()
        self.square = destination_square  # set new square attribute
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square
        square_objects[destination_square].change_occupant(self)

    def get_captured(self, capturing_piece):
        print(
            "A {color_captured} {captured_piece} on {captured_square} was captured by a {color_capturing} {capturing_piece}.".format(
                color_captured=self.color, captured_piece=self.piece, captured_square=self.square,
                color_capturing=capturing_piece.color,
                capturing_piece=capturing_piece.piece))  # print notice that piece was captured, by what, and where
        self.square = "captured"  # set destination to captured to indicate piece is no longer in play


# define knight class
class Knight:
    piece = "knight"

    def __init__(self, name, color, homesquare):
        self.name = name
        self.color = color  # set color
        chess_board[homesquare] = [self, color, self.piece]  # place piece on square by updating chess_board dictionary
        if self.color == "white":
            self.abbreviation = "N"
        else:
            self.abbreviation = "n"
        square_objects[homesquare].change_occupant(self)

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        square_objects[self.square].remove_occupant()
        self.square = destination_square  # set new square attribute
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square
        square_objects[destination_square].change_occupant(self)

    def get_captured(self, capturing_piece):
        print(
            "A {color_captured} {captured_piece} on {captured_square} was captured by a {color_capturing} {capturing_piece}.".format(
                color_captured=self.color, captured_piece=self.piece, captured_square=self.square,
                color_capturing=capturing_piece.color,
                capturing_piece=capturing_piece.piece))  # print notice that piece was captured, by what, and where
        self.square = "captured"  # set destination to captured to indicate piece is no longer in play


# define bishop class
class Bishop:
    piece = "bishop"

    def __init__(self, name, color, homesquare):
        self.name = name
        self.color = color  # set color
        chess_board[homesquare] = [self, color, self.piece]  # place piece on square by updating chess_board dictionary
        if self.color == "white":
            self.abbreviation = "B"
        else:
            self.abbreviation = "b"
        square_objects[homesquare].change_occupant(self)

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        square_objects[self.square].remove_occupant()
        self.square = destination_square  # set new square attribute
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square
        square_objects[destination_square].change_occupant(self)

    def get_captured(self, capturing_piece):
        print(
            "A {color_captured} {captured_piece} on {captured_square} was captured by a {color_capturing} {capturing_piece}.".format(
                color_captured=self.color, captured_piece=self.piece, captured_square=self.square,
                color_capturing=capturing_piece.color,
                capturing_piece=capturing_piece.piece))  # print notice that piece was captured, by what, and where
        self.square = "captured"  # set destination to captured to indicate piece is no longer in play


# define king class
class King:
    piece = "king"

    def __init__(self, name, color, homesquare):
        self.name = name
        self.color = color  # set color
        chess_board[homesquare] = [self, color, self.piece]  # place piece on square by updating chess_board dictionary
        if self.color == "white":
            self.abbreviation = "K"
        else:
            self.abbreviation = "k"
        square_objects[homesquare].change_occupant(self)

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        square_objects[self.square].remove_occupant()
        self.square = destination_square  # set new square attribute
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square
        square_objects[destination_square].change_occupant(self)

    def get_captured(self, capturing_piece):
        print(
            "A {color_captured} {captured_piece} on {captured_square} was captured by a {color_capturing} {capturing_piece}.".format(
                color_captured=self.color, captured_piece=self.piece, captured_square=self.square,
                color_capturing=capturing_piece.color,
                capturing_piece=capturing_piece.piece))  # print notice that piece was captured, by what, and where
        self.square = "captured"  # set destination to captured to indicate piece is no longer in play


# define queen class
class Queen:
    piece = "queen"

    def __init__(self, name, color, homesquare):
        self.name = name
        self.color = color  # set color
        chess_board[homesquare] = [self, color, self.piece]  # place piece on square by updating chess_board dictionary
        if self.color == "white":
            self.abbreviation = "Q"
        else:
            self.abbreviation = "q"
        square_objects[homesquare].change_occupant(self)

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        square_objects[self.square].remove_occupant()
        self.square = destination_square  # set new square attribute
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square
        square_objects[destination_square].change_occupant(self)

    def get_captured(self, capturing_piece):
        print(
            "A {color_captured} {captured_piece} on {captured_square} was captured by a {color_capturing} {capturing_piece}.".format(
                color_captured=self.color, captured_piece=self.piece, captured_square=self.square,
                color_capturing=capturing_piece.color,
                capturing_piece=capturing_piece.piece))  # print notice that piece was captured, by what, and where
        self.square = "captured"  # set destination to captured to indicate piece is no longer in play


# build square objects for entire chessboard
a1 = Square("a1")
b1 = Square("b1")
c1 = Square("c1")
d1 = Square("d1")
e1 = Square("e1")
f1 = Square("f1")
g1 = Square("g1")
h1 = Square("h1")
a2 = Square("a2")
b2 = Square("b2")
c2 = Square("c2")
d2 = Square("d2")
e2 = Square("e2")
f2 = Square("f2")
g2 = Square("g2")
h2 = Square("h2")
a3 = Square("a3")
b3 = Square("b3")
c3 = Square("c3")
d3 = Square("d3")
e3 = Square("e3")
f3 = Square("f3")
g3 = Square("g3")
h3 = Square("h3")
a4 = Square("a4")
b4 = Square("b4")
c4 = Square("c4")
d4 = Square("d4")
e4 = Square("e4")
f4 = Square("f4")
g4 = Square("g4")
h4 = Square("h4")
a5 = Square("a5")
b5 = Square("b5")
c5 = Square("c5")
d5 = Square("d5")
e5 = Square("e5")
f5 = Square("f5")
g5 = Square("g5")
h5 = Square("h5")
a6 = Square("a6")
b6 = Square("b6")
c6 = Square("c6")
d6 = Square("d6")
e6 = Square("e6")
f6 = Square("f6")
g6 = Square("g6")
h6 = Square("h6")
a7 = Square("a7")
b7 = Square("b7")
c7 = Square("c7")
d7 = Square("d7")
e7 = Square("e7")
f7 = Square("f7")
g7 = Square("g7")
h7 = Square("h7")
a8 = Square("a8")
b8 = Square("b8")
c8 = Square("c8")
d8 = Square("d8")
e8 = Square("e8")
f8 = Square("f8")
g8 = Square("g8")
h8 = Square("h8")

# build first rank for white
a_rook_white = Rook("a_rook_white", "white", "a1")
b_knight_white = Knight("b_knight_white", "white", "b1")
c_bishop_white = Bishop("c_bishop_white", "white", "c1")
queen_white = Queen("queen_white", "white", "d1")
king_white = King("king_white", "white", "e1")
f_bishop_white = Bishop("f_bishop_white", "white", "f1")
g_knight_white = Knight("g_knight_white", "white", "g1")
h_rook_white = Rook("h_rook_white", "white", "h1")

# build first rank for black
a_rook_black = Rook("a_rook_black", "black", "a8")
b_knight_black = Knight("b_knight_black", "black", "b8")
c_bishop_black = Bishop("c_bishop_black", "black", "c8")
queen_black = Queen("queen_black", "black", "d8")
king_black = King("king_black", "black", "e8")
f_bishop_black = Bishop("f_bishop_black", "black", "f8")
g_knight_black = Knight("g_knight_black", "black", "g8")
h_rook_black = Rook("h_rook_black", "black", "h8")

# build second rank for white
pawn_one_white = Pawn("pawn_one_white", "white", "a2")
pawn_two_white = Pawn("pawn_two_white", "white", "b2")
pawn_three_white = Pawn("pawn_three_white", "white", "c2")
pawn_four_white = Pawn("pawn_four_white", "white", "d2")
pawn_five_white = Pawn("pawn_five_white", "white", "e2")
pawn_six_white = Pawn("pawn_six_white", "white", "f2")
pawn_seven_white = Pawn("pawn_seven_white", "white", "g2")
pawn_eight_white = Pawn("pawn_eight_white", "white", "h2")

# build second rank for black
pawn_one_black = Pawn("pawn_one_black", "black", "a7")
pawn_two_black = Pawn("pawn_two_black", "black", "b7")
pawn_three_black = Pawn("pawn_three_black", "black", "c7")
pawn_four_black = Pawn("pawn_four_black", "black", "d7")
pawn_five_black = Pawn("pawn_five_black", "black", "e7")
pawn_six_black = Pawn("pawn_six_black", "black", "f7")
pawn_seven_black = Pawn("pawn_seven_black", "black", "g7")
pawn_eight_black = Pawn("pawn_eight_black", "black", "h7")

# function for creating printable chessboard visualization
def visualize_chessboard():
    for rank_list in square_objects_for_viz:
        rank_visualization = str(-square_objects_for_viz.index(rank_list) + 8) # identifies row number and adds to rank_visualization string
        for square in rank_list:
            rank_visualization += " " + square.symbol # adds a space and then the symbol of each square in rank_list to rank_visualization string
        print(rank_visualization) # prints rank_visualization
    print("  a b c d e f g h") # prints file names at bottom of chessboard visualization

# function for creating and outputting pgn of game
def pgn_out():
    game_pgn = ""  # create empty string for pgn
    i = 0  # iterator used to determine when to add move number and which number to add

    for move in game:
        if (i + 2) % 2 == 0:  # if iterator is even, add move number before the move
            game_pgn += str(int((i + 2) / 2)) + "." + move + " "
        else:  # if iterator is not even, append only move
            game_pgn += (move + " ")

        i += 1

    return game_pgn  # print completed pgn


def single_move(color):
    visualize_chessboard()
    
    starting_square = input("{color} player, where is the piece that you would like to move?".format(color=color.title()))  # get current location of piece to be moved

    if starting_square == "end game":  # end game if player responds 'end game'
        print("Good game!  Here's the pgn of this chess game:")
        print(pgn_out())  # create and print pgn of game played
        game.append("STOP")  # append stop signal to game list

    else:
        type_being_moved = chess_board.get(starting_square)[2]  # get type of piece being moved
        piece_being_moved = chess_board.get(starting_square)[0]  # get piece object being moved
        destination_square = input(
            "{color} player, where would you like your {piece} to go?".format(color=color.title(),
                                                                              piece=type_being_moved))  # ask user for destination square
        is_capture = False

        if chess_board.get(destination_square) != "":  # if square is occupied,
            is_capture = True
            captured_piece = chess_board.get(destination_square)[0]  # get captured_piece
            captured_piece.get_captured(piece_being_moved)  # execute get_captured method on captured_piece

        piece_being_moved.move(destination_square)  # move piece_being_moved

        if type_being_moved == "pawn" and is_capture == True:  # make starting column first part of pgn code if pawn is capturing (e.g. exd5)
            pgn_piece_code = starting_square[0]
        else:
            pgn_piece_code = piece_abbreviations.get(type_being_moved)  # make piece abbreviation first part of pgn code

        if is_capture == True:
            pgn_destination_code = "x" + destination_square  # if move is a capture, add 'x' before destination square in end of pgn code
        else:
            pgn_destination_code = destination_square  # make destination square end of pgn code

        game.append(pgn_piece_code + pgn_destination_code)  # append complete pgn code to the list game

        return ""


# function for continuous play
def play_game():
    print(
        """Welcome to simple_chess!  Simple_chess allows you to play chess games in the terminal.  When you are done playing, just type "end game" on your turn.  Have fun!
        """
        )

    single_move("white")

    while True:  # will continue looping until break keyword reached
        if game[-1] == "STOP":  # black's turn if white did not discontinue game
            break
        else:
            single_move("black")

        if game[-1] == "STOP":  # black's turn if white did not discontinue game
            break
        else:
            single_move("white")

    print("End of game")

play_game()
