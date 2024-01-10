def posible(x,y,t):
    out=[]
     
    def cheak(i,j):        
        if t[i][j] == 0 :
            out.append((i,j))
        else :
            if (abs(t[x][y])==t[x][y])!=(abs(t[i][j])==t[i][j]) :
                out.append((i,j))
            return True
        return False
                
                
    def digo(x,y):
        i=x-1;j=y-1
        while i>=0 and j>=0 :
            if cheak(i,j):
                break
            i-=1;j-=1
            
        i=x-1;j=y+1
        while i>=0 and j<8 :
            if cheak(i,j):
                break
            i-=1;j+=1
            
        i=x+1;j=y-1
        while i<8 and j>=0 :
            if cheak(i,j):
                break
            i+=1;j-=1
            
        i=x+1;j=y+1
        while i<8 and j<8 :
            if cheak(i,j):
                break
            i+=1;j+=1
            
            
    def hogo(x,y):
        i=x-1;j=y
        while i>=0 :
            if cheak(i,j):
                break
            i-=1
            
        i=x;j=y+1
        while j<8 :
            if cheak(i,j):
                break
            j+=1
            
        i=x;j=y-1
        while j>=0 :
            if cheak(i,j):
                break
            j-=1
            
        i=x+1;j=y
        while i<8 :
            if cheak(i,j):
                break
            i+=1
            
    def hor(x,y) :
        for i in (-1,1) :
            for j in (-2,2):  
                cheak(x+i,y+j)
                cheak(x+j,y+i)
    
    def king(x,y) :
        i=x-1;j=y-1
        if i>=0 and j>=0 :
            cheak(i,j)
            
        i=x-1;j=y+1
        if i>=0 and j<8 :
            cheak(i,j)
            
        i=x+1;j=y-1
        if i<8 and j>=0 :
            cheak(i,j)
            
        i=x+1;j=y+1
        if i<8 and j<8 :
            cheak(i,j)
            
        i=x-1;j=y
        if i>=0 :
            cheak(i,j)
            
        i=x;j=y+1
        if j<8 :
            cheak(i,j)
            
        i=x;j=y-1
        if j>=0 :
            cheak(i,j)
            
        i=x+1;j=y
        if i<8 :
            cheak(i,j)

    v=t[x][y]
    print(v)
    
    if v==1 :
        if t[x+1][y]==0:
            out.append((x+1,y))
        if t[x+1][y+1]<0 :
            out.append((x+1,y+1))
        if t[x+1][y-1]<0 :
            out.append((x+1,y-1))
    elif v==-1 :
        if t[x-1][y]==0:
            out.append((x+1,y))
        if t[x-1][y+1]<0 :
            out.append((x+1,y+1))
        if t[x-1][y-1]<0 :
            out.append((x+1,y-1))
            
    elif abs(v)==20:
        king(x,y)
    elif abs(v)==9:
        digo(x,y)
        hogo(x,y)
    elif abs(v)==5:
        digo(x,y)
    elif abs(v)==4:
        digo(x,y)
    elif abs(v)==3:
        hor(x,y)
    return out
    
    
ta=[[ 5,  4,  3,  20,  9, -3,  4,  5],
    [ 1,  1,  1,  -1, -1, -1,  1,  1], 
    [-1,  0, -1,   0,  0,  0,  0,  0], 
    [ 0,  0,  0,   0,  0,  0,  0,  0], 
    [ 0,  0,  0,   0,  9,  0,  0,  0], 
    [ 0,  0,  0,   0,  0,  0,  0,  0], 
    [-1, -1, -1,  -1, -1, -1, -1, -1], 
    [-5, -4, -3, -20, -9, -3, -4, -5]]    


print(posible(4,4,ta))