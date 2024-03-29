from typing import Tuple
from movement import posible, poss

COU=0

def shift(initial,final,board_arry,ini=0) :
    fival=board_arry[final[0]][final[1]]
    board_arry[final[0]][final[1]]=board_arry[initial[0]][initial[1]]
    board_arry[initial[0]][initial[1]]=ini
    return fival

def calculate(pl,bor,score,myside,level) :
    global COU
    
    if level==0 :
        return (score,(0, 0), (0, 0))
    sol=poss(pl,bor)
    scli=[]
    for i in sol :
        mov=posible(i[0],i[1],bor)
        for j in mov :
            val=shift(i,j,bor)
            if val !=0 :
                if pl == myside:
                    score += abs(val)
                else :
                    score -= abs(val)
            scli.append((calculate(-pl,bor,score,myside,level-1)[0],i,j))
            
            COU+=1
            shift(j,i,bor,val)

    if pl == myside:
        return max(scli)
    else :
        return min(scli)
    
            
            
            
    

def oldmove(pl,bor,lev=5) -> Tuple[Tuple[int,int],Tuple[int,int]]:
    
    ans=calculate(pl,bor,0,pl,lev)
    print('\n  old\n',COU,'\t',ans[0],'\n',ans[1],ans[2])
    return (ans[1],ans[2])
    
    
    
    
    
    
    
    
    

# ta=[[ 5,  4,  3,  20,  9,  3,  4,  5],
#     [ 1,  1,  1,   1,  1,  1,  1,  1], 
#     [ 0,  0,  0,   0,  0,  0, -1,  0], 
#     [ 0,  0,  0,   0,  0,  0,  0,  0], 
#     [ 0,  0,  0,   0,  0,  0,  0,  0], 
#     [ 0,  0,  0,   0,  0,  0,  0,  0], 
#     [-1, -1, -1,  -1, -1, -1, -1, -1], 
#     [-5, -4, -3, -20, -9, -3, -4, -1]]    


# print(oldmove(1,ta))