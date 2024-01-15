from typing import Tuple
from movement import posible, poss

COU=0
# LEV=2


def shift(initial,final,board_arry,ini=0) :
    fival=board_arry[final[0]][final[1]]
    board_arry[final[0]][final[1]]=board_arry[initial[0]][initial[1]]
    board_arry[initial[0]][initial[1]]=ini
    return fival

def sel(a,b,v) :
    v=abs(v)
    if a==b :
        return v
    else :
        return -v

def last(tamp,pl,myside,value,score):
    if tamp :
        # return score
        if pl == myside:
            if value>score :
                return value
        else :
            if value<score :
                return value
    return score




def recal(pl,bor,score,myside,level,tamp,value) :
    global COU
    if level==0 :
        return last(tamp,pl,myside,value,score)
    sol=poss(pl,bor)
    ret=0
    fst=False;rv=0
    
    for i in sol :
        mov=posible(i[0],i[1],bor)
        for j in mov :
            val=shift(i,j,bor)
            if val != 0 :
                score += sel(pl,myside,val)
            ret = recal(-pl,bor,score,myside,level-1,fst,rv)
            COU+=1
            shift(j,i,bor,val)
            if tamp :
                # print(99)
                if pl == myside:
                    if ret>value :
                        # print('>')
                        return value
                else :
                    if ret<value :
                        # print('<')
                        return value
            
            # print(fst)
            if fst :
                if pl == myside:
                    if ret>rv :
                        rv=ret
                else :
                    if ret<rv :
                        rv=ret
            else :
                fst=True
                rv=ret
    return rv
                






def calculate(pl,bor,score,myside,level) -> Tuple[int,Tuple[int,int],Tuple[int,int]] :
    global COU
    sol=poss(pl,bor)
    ret=0
    fst=False;rv=(0,(0,0),(0,0))
    
    for i in sol :
        mov=posible(i[0],i[1],bor)
        for j in mov :
            val=shift(i,j,bor)
            if val != 0 :
                score += sel(pl,myside,val)
            ret = recal(-pl,bor,score,myside,level-1,fst,rv[0])
            COU+=1
            shift(j,i,bor,val)            
           
            # print(fst)

            if fst :
                if pl == myside:
                    if ret>rv[0] :
                        rv=(ret,i,j)
                else :
                    if ret<rv[0] :
                        rv=(ret,i,j)
            else :
                fst=True
                rv=(ret,i,j)
    return rv
            
            
    

def move(pl,bor,lev=5) -> Tuple[Tuple[int,int],Tuple[int,int]]:
    
    ans=calculate(pl,bor,0,pl,lev)
    print('\n  new\n',COU,'\t',ans[0],'\n',ans[1],ans[2])
    return (ans[1],ans[2])
    
    
    
    
    
    
    
    
    

# ta=[[ 5,  4,  3,  20,  9,  3,  4,  5],
#      [ 1,  1,  1,   1,  1,  1,  1,  1], 
#      [ 0,  0,  0,   0,  0,  0,  0,  0], 
#      [ 0,  0,  0,   0,  0,  0,  0,  0], 
#      [ 0,  0,  0,   0,  0,  0,  0,  0], 
#      [ 0,  0,  0,   0,  0,  0,  0,  0], 
#      [-1, -1, -1,  -1, -1, -1, -1, -1], 
#      [-5, -4, -3, -20, -9, -3, -4, -1]]   

# print(move(1,ta,3))