def posible(x,y,t):
    out=[]
    
    print(*t,sep='\n')
    v=t[x][y]
    print(v)
    
    if v==1 :
        if t[x+1][y]==0:
            out.append((x+1,y))
        if t[x+1][y+1]<0 :
            out.append((x+1,y+1))
        if t[x+1][y-1]<0 :
            out.append((x+1,y-1))
        return out
    elif v==-1 :
        if t[x+1][y]==0:
            out.append((x+1,y))
        if t[x+1][y+1]<0 :
            out.append((x+1,y+1))
        if t[x+1][y-1]<0 :
            out.append((x+1,y-1))
        return out
    
    
ta=[[5, 4, 3, 20, 9, 3, 4, 5], [1, 1, 1, 1, 1, 1, 1, 1], [-1, 0, -1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1], [-5, -4, -3, -20, -9, -3, -4, -5]]    
print(posible(1,1,ta))