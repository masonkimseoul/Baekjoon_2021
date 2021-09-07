import sys
num_0=0
num_1=1
N=int(sys.stdin.readline())
if N==1:
    print(num_1)
else:
    for i in range(N-1):
        tmp=num_1
        num_1+=num_0
        num_0=tmp
    print(num_1)