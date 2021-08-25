N=int(input())
num=666
cnt=0
while cnt<N:
    num_str=str(num)
    for j in range(len(num_str)-2):
        if num_str[j:j+3]=='666':
            cnt+=1
            break
    num+=1
print(num-1)