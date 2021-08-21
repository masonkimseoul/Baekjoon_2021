import math
N=int(input())
for i in range(N):
    x,y=map(int,input().split())
    d=y-x
    if d<4:
        print(d)
    else:
        sq=int(math.sqrt(d))
        if pow(sq,2)==d:
            print(sq*2-1)
        else:
            sq+=1
            if pow(sq,2)-sq>=d:
                print(sq*2-2)
            else:
                print(sq*2-1)