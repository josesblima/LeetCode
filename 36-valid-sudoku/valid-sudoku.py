class Solution:
    def isValidSudoku(self, board) -> bool:
        c_sets = [set() for _ in range(9)]
        sq_sets = [set() for _ in range(9)]
        for row, rowval in enumerate(board):
            
            h_line = set()
            for column, number in enumerate(board[row]):
                if number == '.':
                    continue
                
                if number in h_line:
                    return False
                else:
                    h_line.add(number)
                
                if number in c_sets[column]:
                    return False
                else:
                    c_sets[column].add(number)
                if column <= 2:
                    if row <= 2:
                        if number in sq_sets[0]:
                            return False
                        sq_sets[0].add(number)
                    elif row >= 3 and row <= 5:
                        if number in sq_sets[1]:
                            return False
                        sq_sets[1].add(number)
                    elif row >= 6:
                        if number in sq_sets[2]:
                            return False
                        sq_sets[2].add(number)
                elif column >= 3 and column <= 5:
                    if row <= 2:
                        if number in sq_sets[3]:
                            return False
                        sq_sets[3].add(number)
                    elif row >= 3 and row <= 5:
                        if number in sq_sets[4]:
                            return False
                        sq_sets[4].add(number)
                    elif row >= 6:
                        if number in sq_sets[5]:
                            return False
                        sq_sets[5].add(number)
                elif column >= 6:
                    if row <= 2:
                        if number in sq_sets[6]:
                            return False
                        sq_sets[6].add(number)
                    elif row >= 3 and row <= 5:
                        if number in sq_sets[7]:
                            return False
                        sq_sets[7].add(number)
                    elif row >= 6:
                        if number in sq_sets[8]:
                            return False
                        sq_sets[8].add(number)
        print(True)
        return True
    print(isValidSudoku(1, [[".",".",".",".",".",".","5",".","."],
                            [".",".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".",".","."],
                            ["9","3",".",".","2",".","4",".","."],
                            [".",".","7",".",".",".","3",".","."],
                            [".",".",".",".",".",".",".",".","."],
                            [".",".",".","3","4",".",".",".","."],
                            [".",".",".",".",".","3",".",".","."],
                            [".",".",".",".",".","5","2",".","."]]))