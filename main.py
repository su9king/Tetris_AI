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

        block_set_clear = 0 #DID SET THE BLOCK? 0 : no / 1 : yes


        for i in range(rot_range):
            rot = i + 1
            if block_set_clear == 0:

                block = Tetris_Option.get_block(block_idx,rot) #GETTING BLOCK OF RANDOM
                block_height, block_width = block.shape
                max_col_case = Tetris_Option.get_col_case(block_idx, rot, block)  #HOW MUCH CAN TO SET COL BY YOUR BLOCK

                for row in range(20 - block_height, 0, -1):

                    for col in range(max_col_case + 1):

                        part = board[row: row + block_height , col: col + block_width] #보드에 블럭을 놓을 행렬 부분을 가져오기

                        cel_mut = np.multiply(part,block)

                        if cel_mut.sum() == 0 and block_set_clear == 0:# 블럭을 놓을 자리가 있다면

                            board[row: row + block_height , col: col + block_width] += block
                            block_set_clear = 1
                            print(row, col)
                            print(block)


                        else:
                            pass


        setting.get_event(pygame.event.get())
        Tetris_Option.line_delete(board)
        setting.draw_screen(board)
        i = 0

    i += 0.01




