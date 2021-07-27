N=int(input())
a=[]
cnt=0
flag=0
a=list(map(int, input().split()))
for i in range(N):
    for j in range(1, a[i]+1):
        if a[i]%j==0:
            flag+=1
        if flag>2:
            break
    if flag==2:
        cnt+=1
    flag=0
print(cnt)