# define chess board rows and columns
rows = [i + 1 for i in range(8)]
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
legal_colors = ["white", "black"]
black_pieces = {}
white_pieces = {}
chess_board = {}
game = []
first_rank_start = ["a_rook", "b_knight", "c_bishop", "queen", "king", "f_bishop", "g_knight", "h_rook"]
second_rank_start = ["a_pawn", "b_pawn", "c_pawn", "d_pawn", "e_pawn", "f_pawn", "g_pawn", "h_pawn"]
piece_abbreviations = {"pawn": "", "rook": "R", "knight": "N", "bishop": "B", "king": "K", "queen": "Q"}

# create chess_board dictionary with key for each square
for column in columns:
    for row in rows:
        chess_board[column + str(row)] = ""


# define pawn class
class Pawn:
    piece = "pawn"

    def __init__(self, name, color, homesquare):
        self.name = name
        self.color = color  # set color
        chess_board[homesquare] = [self, color, self.piece]  # place piece on square by updating chess_board dictionary

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        self.square = destination_square  # set new square attribute
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square

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

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        self.square = destination_square  # set new destination square
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square

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

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        self.square = destination_square  # set new destination square
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square

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

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        self.square = destination_square  # set new destination square
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square

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

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        self.square = destination_square  # set new destination square
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square

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

        self.square = homesquare  # set starting square

    def __repr__(self):
        return self.name  # return piece name when called

    def move(self, destination_square):
        chess_board[self.square] = ""  # clear chess_board value for piece's previous square
        self.square = destination_square  # set new destination square
        chess_board[self.square] = [self, self.color, self.piece]  # update chess_board value for destination square

    def get_captured(self, capturing_piece):
        print(
            "A {color_captured} {captured_piece} on {captured_square} was captured by a {color_capturing} {capturing_piece}.".format(
                color_captured=self.color, captured_piece=self.piece, captured_square=self.square,
                color_capturing=capturing_piece.color,
                capturing_piece=capturing_piece.piece))  # print notice that piece was captured, by what, and where
        self.square = "captured"  # set destination to captured to indicate piece is no longer in play


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
pawn_eight_black = Pawn("pawn_eight_black", "black", "h8")


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
    starting_square = input("{color} player, where is the piece that you would like to move?".format(
        color=color.title()))  # get current location of piece to be moved

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
        print(game)

        return ""


# function for continuous play
def play_game():
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
