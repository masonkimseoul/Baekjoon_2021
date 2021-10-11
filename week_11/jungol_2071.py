import sys

def m1(p):

    for i in p:

        for j in i:
            print(j, end=' ')
        print()

def m2(p):
    for i in range(len(p)-1, -1, -1):

        for j in range(len(p)-len(p[i])):
            print(' ', end='')

        for k in range(len(p[i])):
            print(p[i][k], end=' ')
        print()

def m3(p):
    for i in range(len(p)-1, -1, -1):

        for j in range(len(p)-1, i-1, -1):
            print(p[j][i], end=' ')
        print()

N, M=map(int,sys.stdin.readline().split())

pascalTriangle=[]
pascalTriangle.append([1])
cnt=0

for p in pascalTriangle:
    if cnt==N-1:
        break

    array=[]
    array.append(1)

    for i in range(len(p)-1):
        array.append(p[i]+p[i+1])

    array.append(1)

    pascalTriangle.append(array)
    cnt+=1


if M==1:
    m1(pascalTriangle)

elif M==2:
    m2(pascalTriangle)

elif M==3:
    m3(pascalTriangle)