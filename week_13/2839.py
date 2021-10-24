import sys
N=int(sys.stdin.readline())
cnt=0
while(N>=0):
    if(N%5==0):
        print(N//5+cnt)
        exit()
    else:
        N-=3
        cnt+=1

print(-1)