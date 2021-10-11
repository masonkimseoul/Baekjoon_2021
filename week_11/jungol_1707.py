import sys
import math

N=int(sys.stdin.readline())
cnt=1
array=[[0 for j in range(N)]for i in range(N)]

col=0
row=0

while cnt<=math.pow(N,2):
    while col<N and array[row][col]==0:
        array[row][col]=cnt
        cnt+=1
        col+=1

    row+=1
    col-=1

    while row<N and array[row][col]==0:
        array[row][col]=cnt
        cnt+=1
        row+=1

    row-=1
    col-=1

    while col>=0 and array[row][col]==0:
        array[row][col]=cnt
        cnt+=1
        col-=1

    row-=1
    col+=1

    while row>=0 and array[row][col]==0:
        array[row][col]=cnt
        cnt+=1
        row-=1

    row+=1
    col+=1

for i in array:
    for j in i:
        print(j, end=' ')
    print()