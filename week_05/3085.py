def max_line_check(array,n):
    max_cnt=tmp=1

    #check by row direction
    for i in range(n):
        tmp=1
        for j in range(n-1):
            if array[i][j]==array[i][j+1]:
                tmp+=1
                max_cnt=max(tmp,max_cnt)
            else:
                tmp=1

    #check by column direction
    for i in range(n):
        tmp=1
        for j in range(n-1):
            if array[j][i]==array[j+1][i]:
                tmp+=1
                max_cnt=max(tmp,max_cnt)
            else:
                tmp=1

    return max_cnt

N=int(input())
candy_array=[[j for j in input()]for i in range(N)]

max_count=max_line_check(candy_array,N)

#check by row direction
for i in range(N):
    for j in range(N-1):
        if candy_array[i][j]==candy_array[i][j+1]:
            continue
        temp=candy_array[i][j]
        candy_array[i][j]=candy_array[i][j+1]
        candy_array[i][j+1]=temp

        max_count=max(max_count,max_line_check(candy_array,N))

        temp=candy_array[i][j]
        candy_array[i][j]=candy_array[i][j+1]
        candy_array[i][j+1]=temp

#check by column direction
for i in range(N):
    for j in range(N-1):
        if candy_array[j][i]==candy_array[j+1][i]:
            continue
        temp=candy_array[j][i]
        candy_array[j][i]=candy_array[j+1][i]
        candy_array[j+1][i]=temp

        max_count=max(max_count,max_line_check(candy_array,N))

        temp=candy_array[j][i]
        candy_array[j][i]=candy_array[j+1][i]
        candy_array[j+1][i]=temp

print(max_count)