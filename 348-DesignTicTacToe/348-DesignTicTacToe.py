# Last updated: 5/25/2025, 1:08:19 PM
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n 
        self.cols = [0] * n
        self.dias = [0] * 2

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col: self.dias[0] += 1
            if row+col==self.n-1: self.dias[1] += 1
            if self.rows[row] == self.n or self.cols[col] == self.n or self.dias[0] == self.n or self.dias[1] == self.n: return 1

        else:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if row==col: self.dias[0] -= 1
            if row+col==self.n-1: self.dias[1] -= 1
            if self.rows[row] == -self.n or self.cols[col] == -self.n or self.dias[0] == -self.n or self.dias[1] == -self.n: return 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)