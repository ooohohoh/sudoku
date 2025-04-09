from sudoku_generater import Sudoku



if __name__ == '__main__':
    # 初始化pygame
    sudoku=Sudoku(empty_cells_range=(20, 30))


    print(sudoku.board)