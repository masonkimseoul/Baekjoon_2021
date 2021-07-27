#1부터 1000까지 수열 생성한 코드 : 128ms
'''
a,b=map(int,input().split())
array=[]
for i in range(1000):
    for j in range(i):
        array.append(i)
print(sum(array[a-1:b]))
'''

#1부터 시작하며 원소가 b개인 수열 생성한 코드 : 68ms
#수열이 a번째 원소부터 시작하면 더 빨라질 것임

import math
a,b=map(int,input().split())
array=[]
for i in range(int(math.sqrt(b*2-0.25)-0.5)+2):
    for j in range(i):
        array.append(i)
        if len(array)>b-1:
            break
print(sum(array[a-1:b]))