class Spot:
    def __init__(self, row, col, val, board):
        self.row = row
        self.col = col
        self.val = val
        self.board = board
        self.set = None
        self.latin_square = ((self.row//3)*3, (self.col//3)*3) # n×n array filled with n different symbols/numbers

    def change_val(self, value):
        self.temp_val = self.val
        self.val = value
        self.board[self.row][self.col] = self.val

    def set_valid_val(self):
        A = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        unvalid_set = set()

        # adding the values that is on same col
        for i in range(len(self.board)):
            unvalid_set.add(self.board[i][self.col])

        # adding the values that is on same row
        for j in range(len(self.board[self.row])):
            unvalid_set.add(self.board[self.row][j])

        # adding the values that is in the same Latin Square
        x, y = self.return_Lsquare_range()
        for i in range(x, x+3):
            for j in range(y, y+3):
                unvalid_set.add(self.board[i][j])

        self.set = A.difference(unvalid_set)
        # print(self.set)

        return True if len(self.set) != 0 else False

    def return_Lsquare_range(self):
        return self.latin_square


class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self):
        self.bo = [[Spot(i, j, self.board[i][j], self.board) for j in range(len(self.board[0]))] for i in range(len(self.board))]

    def find_empty(self):
        for i in range(len(self.bo)):
            for j in range(len(self.bo[i])):
                if self.bo[i][j].val == 0:
                    return self.bo[i][j]
        return None

    def print_board(self):
        for row in range(len(self.bo)):
            for col in range(len(self.bo[row])):
                print(self.bo[row][col].val, end=' ')
            print("")


def backtrack(spot):
    if spot == None:
        print("Its done :) \n")
        return True

    if spot.set_valid_val():
        while len(spot.set) != 0:
            spot.change_val(spot.set.pop())
            if backtrack(g.find_empty()) == True:
                return True
            else:
                spot.change_val(0)

    return False
    

g = Grid()

if backtrack(g.find_empty()):
    g.print_board()
