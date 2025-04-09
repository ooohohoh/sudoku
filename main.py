import pygame
import time
from sudoku_generater import Sudoku

range_dict = {"easy": (10,20), "mid": (20, 30), "hard": (30, 40), "extreme": (40, 80), "": (27, 31)}

def draw_grids(screen, start_x, start_y, cell_size, line_width, thick_line_width):
    # 填充9x9格子颜色
    for row in range(9):
        for col in range(9):
            rect = (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 182, 193), rect)

    # 绘制9x9的格子
    # 绘制竖线
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (start_x + i * cell_size, start_y), (start_x + i * cell_size, start_y + 9 * cell_size), thick_line_width)
        else:
            pygame.draw.line(screen, (0, 0, 0), (start_x + i * cell_size, start_y), (start_x + i * cell_size, start_y + 9 * cell_size), line_width)

    # 绘制横线
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y + i * cell_size), (start_x + 9 * cell_size, start_y + i * cell_size), thick_line_width)
        else:
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y + i * cell_size), (start_x + 9 * cell_size, start_y + i * cell_size), line_width)

    # 填充1x9格子颜色
    new_start_y = start_y + 9 * cell_size + 20
    for col in range(9):
        rect = (start_x + col * cell_size, new_start_y, cell_size, cell_size)
        pygame.draw.rect(screen, (60, 179, 113), rect)

    # 在9x9的格子下方20像素处，与9x9格子对齐绘制1x9横置的格子，边界线加粗
    for i in range(10):
        if i == 0 or i == 9:
            pygame.draw.line(screen, (0, 0, 0), (start_x + i * cell_size, new_start_y), (start_x + i * cell_size, new_start_y + cell_size), thick_line_width)
        else:
            pygame.draw.line(screen, (0, 0, 0), (start_x + i * cell_size, new_start_y), (start_x + i * cell_size, new_start_y + cell_size), line_width)

    # 绘制下边界线
    pygame.draw.line(screen, (0, 0, 0), (start_x, new_start_y + cell_size), (start_x + 9 * cell_size, new_start_y + cell_size), thick_line_width)
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 0), (start_x, new_start_y + i * cell_size), (start_x + 9 * cell_size, new_start_y + i * cell_size), thick_line_width)

def draw_hover_effect(screen, start_x, start_y, cell_size, line_width, thick_line_width):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for row in range(9):
        for col in range(9):
            rect = pygame.Rect(start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size)
            if rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(screen, (255, 255, 255), rect, line_width)
                pygame.draw.rect(screen, (0, 0, 0), rect.inflate(2, 2), thick_line_width)

def draw_controls(screen, start_x, start_y, cell_size, line_width, thick_line_width, difficulty, start_time):
    # 绘制难度选择按钮
    difficulty_options = ["easy", "mid", "hard", "extreme"]
    button_height = 50
    button_width = 300
    button_x = (840-(start_x + 9 * cell_size)-button_width)/2+start_x + 9 * cell_size
    button_y = start_y + 100
    difficulty_rects = []
    for i, option in enumerate(difficulty_options):
        button_rect = pygame.Rect(button_x, button_y + i * (button_height +20), button_width, button_height)
        difficulty_rects.append(button_rect)
        pygame.draw.rect(screen, (60, 179, 113), button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render(option, True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 255), button_rect, line_width)
            pygame.draw.rect(screen, (0, 0, 0), button_rect.inflate(2, 2), thick_line_width)

    # 绘制开始按钮
    start_button_rect = pygame.Rect(button_x, start_y + 9 * cell_size +20, button_width, button_height)
    pygame.draw.rect(screen, (238, 169, 184), start_button_rect)
    font = pygame.font.Font(None, 24)
    text = font.render("start", True, (0, 0, 0))
    text_rect = text.get_rect(center=start_button_rect.center)
    screen.blit(text, text_rect)
    if start_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (255, 255, 255), start_button_rect, line_width)
        pygame.draw.rect(screen, (0, 0, 0), start_button_rect.inflate(2, 2), thick_line_width)

    # 绘制闯关用时统计
    if start_time is not None:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        time_text = f"TIME: {int(minutes):02d}:{int(seconds):02d}"
    else:
        time_text = "TIME: 00:00"
    font = pygame.font.Font(None, 40)
    text = font.render(time_text, True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(button_x, start_y))
    # 清除之前的用时显示
    pygame.draw.rect(screen, (255, 250, 240), (button_x, start_y, text_rect.width, text_rect.height))
    screen.blit(text, text_rect)

    # 显示当前难度信息
    difficulty_text = f"CURRENT DIFFICULTY: {difficulty}"
    difficulty_font = pygame.font.Font(None, 30)
    difficulty_text_render = difficulty_font.render(difficulty_text, True, (0, 0, 0))
    difficulty_text_rect = difficulty_text_render.get_rect(topleft=(button_x, start_y + 50))
    # 清除之前的难度显示
    pygame.draw.rect(screen, (255, 250, 240), (button_x, start_y + 50, difficulty_text_rect.width, difficulty_text_rect.height))
    screen.blit(difficulty_text_render, difficulty_text_rect)

    return start_button_rect, difficulty_rects, difficulty_options

if __name__ == '__main__':
    # 初始化pygame
    pygame.init()

    # 设置窗口尺寸
    screen_width = 840
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 250, 240))
    # 设置窗口标题
    pygame.display.set_caption("sudoku")
    # 格子参数
    cell_size = 50
    line_width = 1
    thick_line_width = 2
    start_x = 20
    start_y = 20

    difficulty = "easy"
    start_time = None
    sudoku = Sudoku(empty_cells_range=(20, 30))
    user_input_board = [[0] * 9 for _ in range(9)]
    winning=False
    # 游戏主循环
    running = True
    selected_cell = None
    while running:
        draw_grids(screen, start_x, start_y, cell_size, line_width, thick_line_width)
        draw_hover_effect(screen, start_x, start_y, cell_size, line_width, thick_line_width)
        draw_controls(screen, start_x, start_y, cell_size, line_width, thick_line_width, difficulty, start_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_button_rect, difficulty_rects, difficulty_options = draw_controls(screen, start_x, start_y, cell_size, line_width, thick_line_width, difficulty, start_time)
                if start_button_rect.collidepoint(event.pos):
                    start_time = time.time()
                    sudoku = Sudoku(empty_cells_range=range_dict[difficulty])
                    user_input_board = [[0] * 9 for _ in range(9)]
                    print(f"开始游戏，难度: {difficulty}")
                for i, rect in enumerate(difficulty_rects):
                    if rect.collidepoint(event.pos):
                        difficulty = difficulty_options[i]
                        print(f"当前难度已更新为: {difficulty}")
                mouse_x, mouse_y = event.pos
                for row in range(9):
                    for col in range(9):
                        rect = pygame.Rect(start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size)
                        if rect.collidepoint(mouse_x, mouse_y):
                            selected_cell = (row, col)
            elif event.type == pygame.KEYDOWN and selected_cell is not None:
                if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                    row, col = selected_cell
                    user_input = int(event.unicode)
                    user_input_board[row][col] = user_input
                    if Sudoku.check_single_number(sudoku, row, col, user_input):
                        color = (255, 255, 255)
                    else:
                        color = (205, 0, 0)
                    font = pygame.font.Font(None, 42)
                    text = font.render(str(user_input), True, color)
                    text_rect = text.get_rect(topleft=(start_x+col*cell_size+0.3*cell_size, start_y+row*cell_size+0.25*cell_size))
                    screen.blit(text, text_rect)

        # 显示初始数字
        for row in range(9):
            for col in range(9):
                if sudoku.board[row][col] != 0:
                    font = pygame.font.Font(None, 42)
                    text = font.render(str(sudoku.board[row][col]), True, (0, 0, 0))
                    text_rect = text.get_rect(topleft=(start_x+col*cell_size+0.3*cell_size, start_y+row*cell_size+0.25*cell_size))
                    screen.blit(text, text_rect)

        # 显示用户输入的数字
        for row in range(9):
            for col in range(9):
                if user_input_board[row][col] != 0:
                    if user_input_board[row][col]== sudoku.solved_board[row][col]:
                        color = (255, 255, 255)
                    else:
                        color = (205, 0, 0)
                    font = pygame.font.Font(None, 42)
                    text = font.render(str(user_input_board[row][col]), True, color)
                    text_rect = text.get_rect(topleft=(start_x+col*cell_size+0.3*cell_size, start_y+row*cell_size+0.25*cell_size))
                    screen.blit(text, text_rect)

        solution=[[0]*9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
               solution[row][col]=user_input_board[row][col]+sudoku.board[row][col]

        if Sudoku.check_solution(sudoku, solution): 
            print("恭喜你完成了数独游戏！")
             
        # 更新显示
        pygame.display.flip()

    # 退出pygame
    pygame.quit()
