#remove 2회 사용한 코드 실행시간 : 152ms
N=int(input())
a=[]
for i in range(N):
    a=list(map(int,input().split()))
    a.remove(max(a))
    a.remove(max(a))
    print(max(a))
    a.clear
#정렬 후 배열 요소 출력한 코드 : 184ms
'''
N=int(input())
a=[]
for i in range(N):
    a=list(map(int,input().split()))
    a.sort()
    print(a[7])
    a.clear()
'''

#remove 2회 사용한 게 더 빨랐음