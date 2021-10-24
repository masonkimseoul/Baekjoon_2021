import sys

N, K = map(int, sys.stdin.readline().split())
list = []
cnt = 0

for i in range(N):
    list.append(int(sys.stdin.readline()))

for i in range(N-1,-1,-1):
    if K-list[i]>=0:
        cnt+=K//list[i]
        K%=list[i]

print(cnt)