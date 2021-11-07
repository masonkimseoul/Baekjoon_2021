import sys

N=int(sys.stdin.readline())
for i in range(N):
    a=int(sys.stdin.readline())

    length=[1,1,1]

    if(a>3):
        for j in range(3,a+1):
            length.append(length[j-2]+length[j-3])

    print(length[a-1])