def alphabeta(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        max_val = -float('inf')
        for i in range(0, 2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_val = max(max_val, val)
            alpha = max(alpha, max_val)
            if beta <= alpha:
                break
        return max_val
    else:
        min_val = float('inf')
        for i in range(0, 2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_val = min(min_val, val)
            beta = min(beta, min_val)
            if beta <= alpha:
                break
        return min_val

values = [-1 ,4 ,2 ,6 ,-3 ,-5 ,0 ,7]
print("The optimal value is :", alphabeta(0 ,0 ,True ,values, -float('inf'), float('inf')))
