from pysat.solvers import Glucose3

class Board:
    def __init__(self, N):
        self.N = N
        self.current_board = self.create_empty_board()
        self.vars = self.init_vars()

    def create_empty_board(self): # tạo bàn cờ trống
        return [[' ' for _ in range(self.N)] for _ in range(self.N)]

    def init_vars(self): # gán một số vào mỗi ô trên bàn cờ 
        count = 1
        vars_dict = {}
        for i in range(self.N):
            for j in range(self.N):
                vars_dict[(i, j)] = count
                count += 1
        return vars_dict

    def place_queen(self, row, col): # đặt hậu tại ví trí được chỉ định
        self.current_board[row][col] = 'Q'

    def get_board_state(self): # trả về trạng thái hiện tại của bàn cờ
        return self.current_board

    def print_board(self): # in trạng thái hiện tại của bàn cờ
        for i in range(self.N):
            print(' ---' * self.N)
            row = '|'
            for j in range(self.N):
                if self.current_board[i][j] == 'Q':
                    row += ' Q |'
                else:
                    row += '   |'
            print(row)
        print(' ---' * self.N)

class NQueenSolver:
    def __init__(self, N):
        self.N = N
        self.g = Glucose3()
        self.board = Board(N)
        self.solution = None
    
    def _constraint(self):
        # ràng buộc mỗi hàng có đúng 1 hậu
        for i in range(self.N):
            row_vars = [self.board.vars[(i, j)] for j in range(self.N)]
            self.g.add_clause(row_vars)
            for m in range(self.N): # Không có 2 hậu trên cùng một hàng
                for n in range(m+1, self.N):
                    self.g.add_clause([-row_vars[m], -row_vars[n]])
                    
        # ràng buộc mỗi cột có đúng 1 hậu
        for j in range(self.N):
            col_vars = [self.board.vars[(i, j)] for i in range(self.N)]
            self.g.add_clause(col_vars)
            for m in range(self.N): # Không có 2 hậu trên cùng một cột
                for n in range(m+1, self.N):
                    self.g.add_clause([-col_vars[m], -col_vars[n]])
                    
        # ràng buộc đường chéo chính
        for d in range(-self.N + 1, self.N):
            pos_diag = []
            for i in range(self.N):
                if 0 <= i - d < self.N:
                    pos_diag.append(self.board.vars[(i, i - d)])
            for p in range(len(pos_diag)):
                for q in range(p + 1, len(pos_diag)):
                    self.g.add_clause([-pos_diag[p], -pos_diag[q]])

        # ràng buộc đường chéo phụ
        for d in range(2 * self.N - 1):
            neg_diag = []
            for i in range(self.N):
                if 0 <= d - i < self.N:
                    neg_diag.append(self.board.vars[(i, d - i)])
            for p in range(len(neg_diag)):
                for q in range(p + 1, len(neg_diag)):
                    self.g.add_clause([-neg_diag[p], -neg_diag[q]])

    def solve_n_queens(self):
        self._constraint()
        if self.g.solve():
            self.solution = self.g.get_model()
            if self.solution:
                for var in self.solution:
                    if var > 0:
                        var -= 1
                        row = var // self.N
                        col = var % self.N
                        self.board.place_queen(row, col)
                self.board.print_board()
        else:
            print("Không có đáp án")



if __name__=="__main__":
    while True:
        N = int(input("Nhập vào số nguyên dương N (N >= 4): "))
        if N < 4:
            print("Vui lòng nhập N lớn hơn hoặc bằng 4.")
        else:
            break
    nq = NQueenSolver(N)
    nq.solve_n_queens()
    
