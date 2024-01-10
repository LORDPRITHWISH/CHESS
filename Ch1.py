from operator import mod
import tkinter as tk
from movement import posible

MARK={20:'K',9:'Q',5:'r',4:'b',3:'h',1:'p'}
OUTW=[]
OUTB=[]

def setpi(x):
    for i in range(0,8):
        if i==0 :
            v=5
            for j in (0,1,2):
                x[i][j]=x[i][7-j]=v
                v-=1
        elif i==7 :
            v=5
            for j in (0,1,2):
                x[i][j]=x[i][7-j]=-v
                v-=1
        elif i==1 :
            for j in range(0,8):
                x[i][j]=1
        elif i==6 :
            for j in range(0,8):
                x[i][j]=-1
    x[0][3]=20
    x[0][4]=9
    x[7][3]=-20
    x[7][4]=-9
    


W = tk.Tk()
W.geometry("1150x1000+0+0")
W.title("LORDS CHESS PRO MAX")
s=11
W.resizable(False,False)
BL="#0d5d8f"
WH="#75cfff"
SC="#00ff2f"
SF="#ffcc00"
WW="#f0b1dd"
BB="#730024"
SELECTED=False
SLPO=(0,0)
POSLI=[]

f=tk.Frame(W,background="blue",border=5)
f.pack(side="top",pady=15,padx=15,fill="x")
b=[[tk.Button(f)]*8]
loc=[[0]*8]

for i in range(0,7):
    b.append([tk.Button(f)]*8)
    loc.append([0]*8)
    
 
 
    
setpi(loc)

def press(x,y):
    global SELECTED,SLPO,POSLI
    
    def move(s,f,v):
        s.config(text="")
        if v>0 :
            col=BB
        else :
            col=WW
        f.config(text=f"{MARK.get(abs(v))}",fg=col)
        print(v)
    print(x,y)
    if SELECTED :        
        opx=SLPO[0];opy=SLPO[1]
        if opx==((opx//2)*2):
            if opy==((opy//2)*2):
                clo=WH
            else:
                clo=BL
        else:
            if opy==((opy//2)*2):
                clo=BL
            else:
                clo=WH
        b[opx][opy].config(bg=clo)
        if ((loc[opx][opy]<0 and loc[x][y]<0) or (loc[opx][opy]>0 and loc[x][y]>0)) :  #-----------------------------------------------
            def mark(li,v):
                for i in li :
                    if loc[i[0]][i[1]]==0:
                        b[i[0]][i[1]].config(text=v)
                    elif v=="":
                        opx=SLPO[0];opy=SLPO[1]
                        if opx==((opx//2)*2):
                            if opy==((opy//2)*2):
                                clo=WH
                            else:
                                clo=BL
                        else:
                            if opy==((opy//2)*2):
                                clo=BL
                            else:
                                clo=WH
                        b[i[0]][i[1]].config(bg=clo)
                    elif v=="." :
                        b[i[0]][i[1]].config(bg="red")
                        
                        
            b[x][y].config(bg=SC)
            SLPO=(x,y)
            print(445879)
            mark(POSLI,"")
            POSLI=posible(opx,opy,loc)
            mark(POSLI,".")
        else :
            # if loc[x][y]!=0 :
            #     OUTW.append(loc[x][y])
            # loc[x][y]=loc[opx][opy]
            # loc[opx][opy]=0
            
            posible(opx,opy,loc)
            move(b[opx][opy],b[x][y],loc[x][y])
            print(999)
    else:
        b[x][y].config(bg=SC)
        SLPO=(x,y)
        SELECTED=True
    
bc=WH
ff="black"
for i in range(8):
    for j in range(8):
        if i==((i//2)*2):
            if j==((j//2)*2):
                bc=WH
                ac=BL
            else:
                bc=BL
                ac=WH
        else:
            if j==((j//2)*2):
                bc=BL
                ac=WH
            else:
                ac=BL
                bc=WH
        if loc[i][j] == 0 :
            txt=''
        else :
            txt=MARK.get(abs(loc[i][j]))
            if loc[i][j] > 0 :
                ff=BB
            else :
                ff=WW
        
        b[i][j] = tk.Button(f, text=f"{txt}",font=('Arial Black',35,'bold'), width=4, height=1,relief="raised",activebackground=ac,bg=bc,fg=ff,command= lambda r=i, c=j: press(r,c))
        b[i][j].grid(row=i,column=j)



qwe = tk.Button(f, text="kkl",font=('Arial Black',35,'bold'), width=4, height=1,relief="raised",)
qwe.config(text="")

tk.mainloop()