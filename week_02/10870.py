a=[0,1]
N=int(input())
for i in range(N-1):
    a.append(a[i]+a[i+1])
print(a[N])