N=int(input())
M=int(N-len(str(N))*9)
flag=0
while M<N:
    result=M
    tmp=result
    while M>0:
        tmp+=(M%10)
        M//=10
    if N==tmp:
        print(result)
        flag=1
        break
    M=result+1
if flag==0:
    print(0)