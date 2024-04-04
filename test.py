import multiprocessing
from brains import move
from oldbr import oldmove
import time

ta1=[[ 5,  4,  3,  20,  9,  3,  4,  5],
     [ 1,  1,  1,   1,  1,  1,  1,  1], 
     [ 0,  0,  0,   0,  0,  0,  0,  0], 
     [ 0,  0,  0,   0,  0,  0,  0,  0], 
     [ 0,  0,  0,   0,  0,  0,  0,  0], 
     [ 0,  0,  0,   0,  0,  0,  0,  0], 
     [-1, -1, -1,   1, -1, -1, -1, -1], 
     [-5, -4, -3, -20, -9, -3, -4, -1]]    


ta2=[[ 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 0, 0, 0], 
     [ 0, 0, 0, 0, 0, 0, 0, 0], 
     [ 0, 0, 0, 0, 0, 0, 0, 0], 
     [ 0, 0, 0, 0, 0, 0, 0, 0], 
     [ 1, 0, 0, 0, 0, 0, 0, 0], 
     [ 0, 0, 0, 0, 0, 0, 0, 0], 
     [-1, 0, 0, 0, 0, 0, 0, 0]]    

TA=ta1
VAL=4
AR=(1,TA,VAL)
# if __name__ == "__main__":


#     p1 = multiprocessing.Process(target=move, args=AR) 
#     p2 = multiprocessing.Process(target=oldmove, args=AR)
#     p1.start() 
#     p2.start()
# at1=time.time()
# a=move(1,TA,VAL)
# at2=time.time()
# print(a)
# print('new\n\n\nold')
# bt1=time.time()
# b=oldmove(1,TA,VAL)
# bt2=time.time()
# print(b)

# print(a==b)
# print(f'\n\n{at2-at1}\n{bt2-bt1}')

t1=time.time()
ans=move(*AR)
t2=time.time()
print("TIME NEEDED IS :  ",t2-t1)