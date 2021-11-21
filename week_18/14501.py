import sys
N=int(sys.stdin.readline())
TP=[]
for i in range(0,N):
    Day,Profit=map(int,sys.stdin.readline().split())
    TP.append((Day,Profit))
array=[]
for i in range(0,N):
    if (TP[i][0]+i-1<N):
        array.append(TP[i][1])
    else:
        array.append(0)

for i in range(0,N):
    if array[i]==0:
        continue
    for j in range(0,i):
        if (TP[j][0]+j-1<i):
            array[i]=max(array[j]+TP[i][1],array[i])

print(max(array))
