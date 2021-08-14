M=int(input())
N=int(input())
array=[]
flag=0
for i in range(M,N+1):
    for j in range(1,i+1):
        if i%j==0:
            flag+=1
        if flag>2:
            break
    if flag==2:
        array.append(i)
    flag=0
if len(array)!=0:
    print(sum(array))
    print(min(array))
else:
    print(-1)
