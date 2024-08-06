import copy

class SearchStrategy:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def alpha_beta_search(self, problem):
        best_score = float('-inf')
        best_move = None
        for move in problem.available_moves():
            new_problem = copy.deepcopy(problem)
            new_problem.make_move(move, self.computer)
            score = self.min_value(new_problem, float('-inf'), float('inf'))
            new_problem.undo_move(move)
            if score > best_score :
                best_score = score
                best_move = move
        return best_move

    def max_value(self, problem, alpha = float('-inf'), beta = float('inf')):
        if problem.is_terminal():
            return problem.utility(self.computer)
        v = float('-inf')
        for move in problem.available_moves():
            problem.make_move(move, self.computer)
            v = self.min_value(problem, alpha, beta)
            problem.undo_move(move)
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, problem, alpha = float('-inf'), beta = float('inf')):
        if problem.is_terminal():
            return problem.utility(self.computer)
        v = float('inf')
        for move in problem.available_moves():
            problem.make_move(move, self.player)
            v = self.max_value(problem, alpha, beta)
            problem.undo_move(move)
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
