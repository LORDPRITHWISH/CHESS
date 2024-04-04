# calculate_moves.pyx

import cython

from cython import *
from libc.stdlib import cimport,abs

@cython.boundscheck(False)
@cython.wraparound(False)
cdef int shift(int[:] initial, int[:] final, int[:, ::1] board_arry, int ini=0):
    cdef int fival = board_arry[final[0]][final[1]]
    board_arry[final[0]][final[1]] = board_arry[initial[0]][initial[1]]
    board_arry[initial[0]][initial[1]] = ini
    return fival

@cython.boundscheck(False)
@cython.wraparound(False)
cdef int sel(int a, int b, int v):
    v = abs(v)
    if a == b:
        return v
    else:
        return -v

@cython.boundscheck(False)
@cython.wraparound(False)
cdef int last(bint tamp, int pl, int myside, int value, int score):
    if tamp:
        if pl == myside:
            if value > score:
                return value
        else:
            if value < score:
                return value
    return score

@cython.boundscheck(False)
@cython.wraparound(False)
cdef int recal(int pl, int[:, ::1] bor, int score, int myside, int level, bint tamp, int value):
    cdef int COU = 0
    if level == 0:
        return last(tamp, pl, myside, value, score)
    cdef int[:,:] sol = poss(pl, bor)
    cdef int ret = 0
    cdef bint fst = False
    cdef int rv = 0

    for i in sol:
        mov = posible(i[0], i[1], bor)
        for j in mov:
            val = shift(i, j, bor)
            if val != 0:
                score += sel(pl, myside, val
