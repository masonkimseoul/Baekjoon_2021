N=int(input())
cnt=0
flag=0
for i in range(1,N+1):
    if i<100:
        cnt+=1
    else:
        array=list(str(i))
        step=int(array[1])-int(array[0])
        for j in range(len(array)-1):
            if int(array[j+1])-int(array[j])!=step:
                flag+=1
                break
        if flag==0:
            cnt+=1
        else:
            flag=0
print(cnt)