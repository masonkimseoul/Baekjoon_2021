N=int(input())
sum=1
cnt=1
while sum<N:
    cnt+=1
    sum+=cnt
if sum>N:
    sum=sum-(sum-N)
    cnt-=1
print(cnt)