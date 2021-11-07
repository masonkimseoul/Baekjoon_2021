import sys

N=int(sys.stdin.readline())

cnt=[1,2,3]

if(N>3):
    for i in range(3,N+1):
        cnt.append((cnt[i-1]+cnt[i-2])%15746)

print(cnt[N-1])
