from typing import Tuple
from movement import posible, poss


def move(pl,bor) -> Tuple[Tuple[int,int],Tuple[int,int]]:
    # print(poss(pl,bor))
    sol=poss(pl,bor)
    for i in sol :
        # print(posible(i[0],i[1],bor))
        x=posible(i[0],i[1],bor)
        if x:
            return (i,x[0])
    # a = ((0, 0), (0, 0))
    return ((0, 0), (0, 0))
    