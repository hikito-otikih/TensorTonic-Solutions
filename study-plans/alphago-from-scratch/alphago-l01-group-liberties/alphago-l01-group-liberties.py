import numpy as np

def inboard(row: int, col: int, edge: int) -> bool:
    return 0 <= row < edge and 0 <= col < edge  

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """
    if (board[row][col] == 0) :
        return ([], [])
    zeros_array = np.zeros((len(board), len(board)))
    stack = [(row, col)]
    component = [(row, col)]
    liberty = []
    zeros_array[row][col] = 1
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while (len(stack) > 0) : 
        r, c = stack.pop()
        for i, j in direction :
                nr = r + i
                nc = c + j
                if inboard(nr, nc, len(board)) and (zeros_array[nr][nc] == 0):
                    zeros_array[nr][nc] = 1
                    if board[nr][nc] == board[row][col] :
                        component.append((nr, nc))
                        stack.append((nr, nc))
                    if board[nr][nc] == 0 :
                        liberty.append((nr, nc))
    component = sorted(component)
    liberty = sorted(liberty)
    return (component, liberty)
        
        