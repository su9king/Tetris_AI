import numpy as np
import pygame
import setting

## block list
## idx :  1     2      3     4     5     6      7
##       ■■ ■■■■ ■■■ ■■■ ■■■ ■■□□ □□■■
##       ■■ □□□□ □□■ ■□□ □■□ □■■□ □■■□
##


def get_block( block_idx , rot ):

    blocks_range = []

    # block image
    # ■■
    # ■■
    if block_idx == 1 :

        blocks_range = np.full((2,2),1)

    elif block_idx == 2 :

        # ■■■■
        if rot == 1:

            blocks_range = np.full((4,1),1)
        # ■
        # ■
        # ■
        # ■
        elif rot == 2:

            blocks_range = np.full((1,4),1)


    elif block_idx == 3:

        # ■■■
        # □□■
        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,0,1],[0,1,2,2]] = 1

        # □■
        # □■
        # ■■
        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,2,2],[1,1,0,1]] = 1

        # ■□□
        # ■■■
        elif rot == 3:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,1,1,1],[0,0,1,2]] = 1

        # ■■
        # ■□
        # ■□
        elif rot == 4:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,0,1,2],[0,1,0,0]] = 1



    elif block_idx == 4:

        # ■■■
        # ■□□
        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,0,1],[0,1,2,0]] = 1

        # ■□
        # ■□
        # ■■
        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,2,2],[0,0,0,1]] = 1

        # □□■
        # ■■■
        elif rot == 3:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,1,1,1],[2,0,1,2]] = 1

        # ■■
        # □■
        # □■
        elif rot == 4:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,0,1,2],[0,1,1,1]] = 1



    elif block_idx == 5:

        # ■■■
        # □■□
        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,0,1],[0,1,2,1]] = 1

        # ■□
        # ■■
        # ■□
        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[0,0,1,0]] = 1

        # □■□
        # ■■■
        elif rot == 3:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,1,1,1],[1,0,1,2]] = 1

        # □■
        # ■■
        # □■
        elif rot == 4:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[1,0,1,1]] = 1


    elif block_idx == 6:

        # □■■□
        # □□■■
        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,1,1],[0,1,1,2]] = 1

        # □■
        # ■■
        # ■□
        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[1,0,1,0]] = 1


    elif block_idx == 7:

        # □□■■
        # □■■□
        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,1,1],[1,2,0,1]] = 1

        # ■□
        # ■■
        # □■
        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[0,0,1,1]] = 1


    return blocks_range


#이걸로 블럭 표시할때 쓰일 함수가 될것임.
#def get_color(block_idx):


def rot_range(block_idx):

    if block_idx == 1:

        rot_range = 1

    elif block_idx == 2 or block_idx == 6 or block_idx == 7:

        rot_range =  2

    elif block_idx == 3 or block_idx == 4 or block_idx == 5:

        rot_range =  4

    return rot_range

def get_row_case(block_idx,rot,blocks):

    if block_idx == 1:

        row_case = 8

    elif block_idx == 2:

        if rot == 1:

            row_case = 9

        elif rot == 2:

            row_case = 6

    elif block_idx >= 3:

        if blocks.shape == (2,3):

            row_case = 7

        else:

            row_case = 8

    return row_case


















