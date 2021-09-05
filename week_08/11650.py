N=int(input())
array=[list(map(int,input().split()))for i in range(N)]
array.sort(key=lambda a:a[1])
array.sort(key=lambda a:a[0])
for i in range(N):
    print(str(array[i][0])+" "+str(array[i][1]))
#삽입정렬=O(n^2)
#파이썬 내장 sort=O(nlogn)