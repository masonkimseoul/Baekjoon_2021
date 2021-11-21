import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
B,C=map(int,sys.stdin.readline().split())

cntPrin=0
cntVice=0

for i in A:
    i-=B
    cntPrin+=1
    if(i>0):
        if(i>=C):
            cntVice+=(i//C)
        if(i%C!=0):
            cntVice+=1
print(cntPrin+cntVice)