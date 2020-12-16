import AIEnvironment


class Minimax:

    def __init__(self, depth):
        self.depth = depth  # the maximum depth of the minimax algorithm
    def minimax(self, curr_depth, max_turn, state, player, alpha=-float('inf'), beta=float('inf') ):
        if curr_depth == self.depth or AIEnvironment.terminal(state):
            return AIEnvironment.evaluation_function(state, player), ""

        best_val = float('inf') if not max_turn else -float('inf')
        list_actions = AIEnvironment.action(state)
        for action in list_actions:
            new_state = AIEnvironment.result(state, action)
            nextplayer = 'H'
            if player == 'H':
                nextplayer = 'A'
            eval_val, eval_action = self.minimax(curr_depth+1, not max_turn, new_state, nextplayer)
            if best_val == -1000 :
                print("best val: %d", best_val)
            if eval_val == - 1000:
                print("eval val: %d", eval_val)
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

