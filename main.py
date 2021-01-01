import setting
import Tetris_Option
import pygame
import random
import numpy as np

board = np.zeros([20,10])
setting.set_window("test",320,640)

i = 0

while setting.program_run:

    if i >= 50000: #TO CONTROL THE RUNNING SPEED

        block_idx = random.randint(1,7)
        rot_range = Tetris_Option.rot_range(block_idx)

        block_set_case = 0
        max_col_case = 10


        for i in range(rot_range):
            rot = i + 1

            board_temp = np.copy(board)
            block_set_case = 0
            max_col_case = 10

            if block_set_case < max_col_case:

                block = Tetris_Option.get_block(block_idx,rot) #GETTING BLOCK
                block_height, block_width = block.shape
                max_col_case = Tetris_Option.get_col_case(block_idx, rot, block)  #HOW MUCH CAN TO SET COL BY YOUR BLOCK


                for row in range(20 - block_height, 0, -1):

                    if block_set_case < max_col_case:

                        for col in range(max_col_case + 1):

                            part = board[row: row + block_height , col: col + block_width] #보드에 블럭을 놓을 행렬 부분을 가져오기

                            cel_mut = np.multiply(part,block)

                            if cel_mut.sum() == 0 and block_set_case < max_col_case:# 블럭을 놓을 자리가 있다면

                                board_temp[row: row + block_height , col: col + block_width] += block
                                block_set_case += 1

                                if row == 20 - block_height :#블럭이 맨 아래 행에 놓였다면

                                    cost = Tetris_Option.check_set_point("under",board_temp[row: row + block_height ,
                                                                                 col: col + block_width])
                                    board_temp = np.copy(board)

                                else:

                                    cost = Tetris_Option.check_set_point("default",board_temp[row - 1 : row + block_height ,
                                                                         col: col + block_width])
                                    board_temp = np.copy(board)


                            else:
                                pass


        setting.get_event(pygame.event.get())
        setting.draw_screen(Tetris_Option.line_delete(board))
        i = 0

    i += 0.05




