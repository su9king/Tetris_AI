import setting
import Tetris_Option
import pygame
import random
import numpy as np

board = np.zeros([20,10])
board[19,:] = 1
setting.set_window("test",320,640)
test = 0

t = 0

while setting.program_run:

    if t >= 80000: #TO CONTROL THE RUNNING SPEED

        block_idx = random.randint(1,7) #블럭의 형태 설정
        rot_range = Tetris_Option.rot_range(block_idx) #블럭의 돌릴수 있는 경우의 수 설정

        efficiency = -50 #현재 블럭 위치의 점수


        for i in range(rot_range):
            rot = i + 1

            board_temp = np.copy(board)
            board_goal = np.copy(board)

            block_set_count = 0 # 블럭을 놓은 횟수


            block = Tetris_Option.get_block(block_idx, rot)  # GETTING BLOCK
            block_height, block_width = block.shape
            max_col_case = Tetris_Option.get_col_case(block_idx, rot, block)  # HOW MUCH CAN TO SET COL BY
                                                                              # YOUR BLOCK

            for row in range(20 - block_height, 0, -1):

                if block_set_count < 30:

                    for col in range(max_col_case + 1):

                        part = board[row: row + block_height , col: col + block_width] #보드에 블럭을 놓을 행렬 부분을 가져오기

                        cel_mut = np.multiply(part,block)

                        if cel_mut.sum() == 0 and block_set_count < max_col_case:# 블럭을 놓을 자리가 있다면

                            board_temp[row: row + block_height , col: col + block_width] += block
                            block_set_count += 1


                            if efficiency < Tetris_Option.check_set_point(board_temp[row : row + block_height + 1,col: col + block_width + 1]):
                            #전 블럭의 위치가 현재 블럭 위치 점수보다 낮다면
                                efficiency = Tetris_Option.check_set_point(board_temp[row : row + block_height + 1,col: col + block_width + 1])
                                board_goal = np.copy(board_temp)
                                board_temp = np.copy(board)

                            else:
                                board_temp = np.copy(board)



        test += 1
        print(test)
        board = np.copy(board_goal)

        setting.get_event(pygame.event.get())
        setting.draw_screen(Tetris_Option.line_delete(board))
        t = 0

    t += 0.05




