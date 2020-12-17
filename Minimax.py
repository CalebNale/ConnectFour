import AIEnvironment


class Minimax:

    def __init__(self, depth):
        self.depth = depth  # the maximum depth of the minimax algorithm

    # def minimax(self, curr_depth, max_turn, state, player, alpha=-float('inf'), beta=float('inf') ):

    def minimax(self, curr_depth, max_turn, state, alpha=-float('inf'), beta=float('inf')):
        moves = AIEnvironment.action(state)
        is_terminal = AIEnvironment.terminal(state)
        if curr_depth == self.depth or is_terminal:
            if is_terminal:
                if AIEnvironment.win(state) == 'A':
                    return float('inf'), None
                elif AIEnvironment.win(state) == 'H':
                    return -float('inf'), None
                else:  # Game is over, no more valid moves
                    return 0, None
            else:  # Depth is at limit
                return AIEnvironment.heuristic(state, 'A'), None
        if max_turn:
            value = -float('inf')
            move = moves[0]
            for option in moves:
                new_board = AIEnvironment.result(state, option, 'A')
                new_score = self.minimax(curr_depth + 1, False, new_board, alpha, beta)[0]
                if new_score > value:
                    value = new_score
                    move = option
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value, move

        else:  # Minimizing player
            value = float('inf')
            move = moves[0]
            for option in moves:
                new_board = AIEnvironment.result(state, option, 'H')
                new_score = self.minimax(curr_depth + 1, True, new_board, alpha, beta)[0]
                if new_score < value:
                    value = new_score
                    move = option
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value, move

    """
    def minimax(self, curr_depth, max_turn, state, player, alpha=-float('inf'), beta=float('inf') ):
        if curr_depth == self.depth or AIEnvironment.terminal(state):
            return AIEnvironment.evaluation_function(state, player), ""

        best_val = float('inf') if not max_turn else -float('inf')
        list_actions = AIEnvironment.action(state)
        for action in list_actions:
            new_state = AIEnvironment.result(state, action, player)
            next_player = 'H'
            if player == 'H':
                next_player = 'A'
            eval_val, eval_action = self.minimax(curr_depth+1, not max_turn, new_state, next_player)
            if max_turn and best_val < eval_val:
                best_val = eval_val
                best_action = action
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break

            if not max_turn and best_val > eval_val:
                best_val = eval_val
                best_action = action
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break

        return best_val, best_action
        """