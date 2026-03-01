from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Method 2
        row_dict = {}
        box_dict = {idx : [] for idx in range(len(board))}
        col_dict = {idx : [] for idx in range(len(board))}
        box_idx, col_idx = 0, 0
        board_valid = True
        for row in range(len(board)):
            # Preparation of row_dict
            row_dict[row] = [val for val in board[row] if val != '.']

            # Preparation of box_dict
            if len(box_dict.get(box_idx)) < 9:
                box_dict[box_idx] += board[row][0:3]
                box_dict[box_idx+1] += board[row][3:6]
                box_dict[box_idx+2] += board[row][6:9]
            else:
                box_idx = box_idx + 3
                box_dict[box_idx] += board[row][0:3]
                box_dict[box_idx+1] += board[row][3:6]
                box_dict[box_idx+2] += board[row][6:9]
            
            if board[row][0] != '.' : col_dict[0] += [board[row][0]]
            if board[row][1] != '.' : col_dict[1] += [board[row][1]]
            if board[row][2] != '.' : col_dict[2] += [board[row][2]]
            if board[row][3] != '.' : col_dict[3] += [board[row][3]]
            if board[row][4] != '.' : col_dict[4] += [board[row][4]]
            if board[row][5] != '.' : col_dict[5] += [board[row][5]]
            if board[row][6] != '.' : col_dict[6] += [board[row][6]]
            if board[row][7] != '.' : col_dict[7] += [board[row][7]]
            if board[row][8] != '.' : col_dict[8] += [board[row][8]]


        # checking row validation
        for row in row_dict.values():
            if len(row) != len(list(set(row))):
                board_valid = False
            
        # checking col validation
        for col in col_dict.values():
            if len(col) != len(list(set(col))):
                board_valid = False
            
        # checking box validation
        for box in box_dict.values():
            box_vals = [val for val in box if val != '.']
            if len(box_vals) != len(list(set(box_vals))):
                board_valid = False

        return board_valid