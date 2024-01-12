def posible(x,y,t):
    out=[]
     
    def cheak(i,j):
        if (i<0 or i>7) or (j>7 or j<0) :
            return False
        if t[i][j] == 0 :
            out.append((i,j))
        else :
            if (abs(t[x][y])==t[x][y])!=(abs(t[i][j])==t[i][j]) :
                out.append((i,j))
            return False
        return True
                
                
    def digo(x,y):
        i=x-1;j=y-1
        while cheak(i,j) :
            i-=1;j-=1
            
        i=x-1;j=y+1
        while cheak(i,j) :
            i-=1;j+=1
            
        i=x+1;j=y-1
        while cheak(i,j) :
            i+=1;j-=1
            
        i=x+1;j=y+1
        while cheak(i,j):
            i+=1;j+=1
            
            
    def hogo(x,y):
        i=x-1;j=y
        while cheak(i,j) :
            i-=1
            
        i=x;j=y+1
        while cheak(i,j):
            j+=1
            
        i=x;j=y-1
        while cheak(i,j) :
            j-=1
            
        i=x+1;j=y
        while cheak(i,j) :
            i+=1
            
    def hor(x,y) :
        for i in (-1,1) :
            for j in (-2,2):                
                cheak(x+i,y+j)
                cheak(x+j,y+i)
    
    def king(x,y) :
        i=x-1;j=y-1
        cheak(i,j)
            
        i=x-1;j=y+1
        cheak(i,j)
            
        i=x+1;j=y-1
        cheak(i,j)
            
        i=x+1;j=y+1
        cheak(i,j)
            
        i=x-1;j=y
        cheak(i,j)
            
        i=x;j=y+1
        cheak(i,j)
            
        i=x;j=y-1
        cheak(i,j)
            
        i=x+1;j=y
        cheak(i,j)

    v=t[x][y]
    
    if v==1 :
        if x<7 :
            if t[x+1][y]==0:
                out.append((x+1,y))
                if x==1 and t[x+2][y]==0:
                    out.append((x+2,y))
                    
            if y<7 and t[x+1][y+1]<0 :
                out.append((x+1,y+1))
            if y>0 and t[x+1][y-1]<0 :
                out.append((x+1,y-1))
    elif v==-1 :
        if x>0 :
            if t[x-1][y]==0:
                out.append((x-1,y))
                if x==6 and t[x-2][y]==0:
                    out.append((x-2,y))
            if y<7 and t[x-1][y+1]>0 :
                out.append((x-1,y+1))
            if y>0 and t[x-1][y-1]>0 :
                out.append((x-1,y-1))
            
    elif abs(v)==20:
        king(x,y)
    elif abs(v)==9:
        digo(x,y)
        hogo(x,y)
    elif abs(v)==5:
        hogo(x,y)
    elif abs(v)==4:
        digo(x,y)
    elif abs(v)==3:
        hor(x,y)
    return out
    
def poss(o,t):
    out=[]
    if o<0 :
        for i in range(0,8) :
            for j in range(0,8) :
                if t[i][j]<0 :
                    out.append((i,j))
    elif o>0 :
        for i in range(0,8) :
            for j in range(0,8) :
                if t[i][j]>0 :
                    out.append((i,j))
    return out
    
    
    
    
    
ta=[[ 5,  4,  3,  20,  9, -3,  4,  5],
    [ 1,  1,  1,  -1, -1, -1,  1,  1], 
    [-1,  0, -1,   0,  0,  0,  0,  0], 
    [ 0,  0,  0,   0,  0,  0,  0,  0], 
    [ 0,  0,  0,   0,  9,  0,  0,  0], 
    [ 0,  0,  0,   0,  0,  0,  0,  0], 
    [-1, -1, -1,  -1, -1, -1, -1, -1], 
    [-5, -4, -3, -20, -9, -3, -4,  1]]    


# print(posible(4,4,ta))