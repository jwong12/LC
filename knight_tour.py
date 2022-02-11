

def knight_tour(size):
    board = [[-1 for i in range(size)]for i in range(size)]
    board[0][0] = 0
    moves_x = [1, 1, 2, 2, -1, -1, -2, -2]
    moves_y = [2, -2, 1, -1, 2, -2, 1, -1]

    if backtrack(board, moves_x, moves_y, 0, 0, size, 1):
        print(board)


def is_valid(board):
    pass


def backtrack(board, moves_x, moves_y, curr_x, curr_y, size, moves):
    if moves == size**2:
        return True

    for i in range(size):
        new_x = curr_x + moves_x[i]
        new_y = curr_y + moves_y[i]
        if 0 <= new_x < size and 0 <= new_y < size and board[new_x][new_y] == -1:
            board[new_x][new_y] = moves
            if backtrack(board, moves_x, moves_y, new_x, new_y, size, moves+1):
                return True
            board[new_x][new_y] = -1
    return False


if __name__ == "__main__":
    n = 8
    knight_tour(8)
