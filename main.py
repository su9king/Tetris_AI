import setting
import Tetris_Option
import pygame
import random
import numpy as np

board = np.zeros([20,10])
setting.set_window("test",320,640)

i = 0

while setting.program_run:

    if i >= 50000:

        block_idx = random.randint(1,7)
        rot_range = Tetris_Option.rot_range(block_idx)

        clear = 0


        for i in range(rot_range):
            rot = i + 1
            if clear == 0:

                block = Tetris_Option.get_block(block_idx,rot)
                block_height, block_width = block.shape
                max_row_case = Tetris_Option.get_row_case(block_idx,rot,block)

                for col in range(20 - block_height,0,-1):

                    for row in range(max_row_case):

                        part = board[col : col + block_height , row : row + block_width]

                        cel_mut = np.multiply(part,block)

                        if cel_mut.sum() == 0 and clear == 0:

                            board[col : col + block_height , row : row + block_width] += block
                            clear = 1
                            print(col,row)
                            print(block)


                        else:
                            pass


        setting.get_event(pygame.event.get())
        setting.set_board(board)
        i = 0

    i += 0.01




