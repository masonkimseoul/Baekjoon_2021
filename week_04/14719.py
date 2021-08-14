N,M=map(int,input().split())
height_list=list(map(int,input().split()))
cnt=0
for i in range(1,M-1):
    left_max=max(height_list[:i])
    right_max=max(height_list[i+1:])
    if height_list[i]>=left_max or height_list[i]>=right_max:
        continue
    cnt+=(min(left_max,right_max)-height_list[i])
print(cnt)
