class Spot:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.set = {}
        self.latin_square = (self.row//3, self.col//3) # n×n array filled with n different symbols/numbers

    def set_valid_val(self, B):
        A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.set = A.difference(B)
        print(self.set)

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
        self.bo = [[Spot(i, j, self.board[i][j]) for j in range(len(self.board[0]))] for i in range(len(self.board))]

    def print_board(self):
        for row in range(len(self.bo)):
            for col in range(len(self.bo[row])):
                print(self.bo[row][col].val, end=' ')
            print("")

    def find_unvalid(self, row, col):
        unvalid_set = set()
        print(type(unvalid_set))
        # adding the values that is on same col
        for i in range(len(self.bo)):
            unvalid_set.add(self.bo[i][col].val)

        # adding the values that is on same row
        for j in range(len(self.bo[row])):
            unvalid_set.add(self.bo[row][j].val)

        # adding the values that is in the same Latin Square
        x, y = self.bo[row][col].return_Lsquare_range()
        for i, j in zip(range(x, x+3), range(y, y+3)):
            unvalid_set.add(self.bo[i][j].val)

        self.bo[row][col].set_valid_val(unvalid_set)



g = Grid()
# g.print_board()
g.find_unvalid(1, 1)
