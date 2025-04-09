import random

class Sudoku:
    def __init__(self, empty_cells_range=(7, 11)):
        # 初始化一个9x9的数独棋盘，全部填充为0
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        # 记录挖空数量范围
        self.empty_cells_range = empty_cells_range
        # 生成一个完整的数独解
        self.generate_sudoku()
        # 保留挖空前的完整数独

    def generate_sudoku(self):
        # 调用回溯算法填充数独棋盘
        self._backtrack(0, 0)
        # 保存挖空前的完整数独
        self.solved_board = [row[:] for row in self.board]
        # 挖空部分格子以创建谜题
        self._remove_numbers()

    def _backtrack(self, row, col):    
        # 如果已经填充完最后一行，数独已完成
        if row == 9:
            return True
        # 计算下一个格子的行和列
        next_row = row if col < 8 else row + 1
        next_col = (col + 1) % 9

        # 生成1到9的随机数字列表
        numbers = list(range(1, 10))
        random.shuffle(numbers)

        # 尝试每个数字
        for num in numbers:
            if self._is_valid(row, col, num):
                # 如果数字有效，填入该数字
                self.board[row][col] = num
                # 递归填充下一个格子
                if self._backtrack(next_row, next_col):
                    return True
                # 如果递归失败，回溯并清除当前格子
                self.board[row][col] = 0

        return False

    def _is_valid(self, row, col, num):   
        # 检查行是否合法
        for i in range(9):
            if self.board[row][i] == num:
                return False
        # 检查列是否合法
        for i in range(9):
            if self.board[i][col] == num:
                return False
        # 检查3x3子网格是否合法
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def _remove_numbers(self):
        # 挖空一定数量的格子以创建谜题
        empty_cells = random.randint(*self.empty_cells_range)
        while empty_cells > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                empty_cells -= 1

    def check_single_number(self, row, col, num):
        # 检查用户填入的单个数字是否正确
        return self._is_valid(row, col, num) and num == self.solved_board[row][col]

    def check_solution(self, solution):
        # 检查用户的解是否正确
        for i in range(9):
            for j in range(9):
                if solution[i][j] != self.solved_board[i][j]:
                    return False
        return True

    def get_board(self):
        # 返回当前数独棋盘
        return self.board

    def get_solved_board(self):
        # 返回挖空前的完整数独
        return self.solved_board
