import numpy as np

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

        blocks_range = np.full((1,1),1)

    # ■■■■
    elif block_idx == 2 :

        if rot == 1:

            blocks_range = np.full((4,1),2)

        elif rot == 2:

            blocks_range = np.full((1,4),2)

    # ■■■
    # □□■
    elif block_idx == 3:

        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,0,1],[0,1,2,2]] = 3

        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,2,2],[1,1,0,1]] = 3

        elif rot == 3:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,1,1,1],[0,0,1,2]] = 3

        elif rot == 4:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,0,1,2],[0,1,0,0]] = 3


    # ■■■
    # ■□□
    elif block_idx == 4:

        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,0,1],[0,1,2,0]] = 4

        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,2,2],[0,0,0,1]] = 4

        elif rot == 3:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,1,1,1],[2,0,1,2]] = 4

        elif rot == 4:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,0,1,2],[0,1,1,1]] = 4


    # ■■■
    # □■□
    elif block_idx == 5:

        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,0,1],[0,1,2,1]] = 5

        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[0,0,1,0]] = 5

        elif rot == 3:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,1,1,1],[1,0,1,2]] = 5

        elif rot == 4:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[1,0,1,1]] = 5


    # □■■□
    # □□■■
    elif block_idx == 6:

        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,1,1],[0,1,1,2]] = 6

        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[1,0,1,0]] = 6


    # □□■■
    # □■■□
    elif block_idx == 7:

        if rot == 1:

            blocks_range = np.zeros([2,3])

            blocks_range[[0,0,1,1],[1,2,0,1]] = 7

        elif rot == 2:

            blocks_range = np.zeros([3,2])

            blocks_range[[0,1,1,2],[0,0,1,1]] = 7


    return blocks_range







