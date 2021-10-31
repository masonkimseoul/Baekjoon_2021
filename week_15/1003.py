import sys

N=int(sys.stdin.readline())

callZero=[1,0,1]
callOne=[0,1,1]

def fib(n):
    if(n<len(callZero)):
        print("%d %d" % (callZero[n], callOne[n]))
    else:
        for i in range(len(callZero),n+1):
            callZero.append(callZero[i-1]+callZero[i-2])
            callOne.append(callOne[i-1]+callOne[i-2])
        print("%d %d"%(callZero[n],callOne[n]))

for i in range(N):
    num=int(sys.stdin.readline())
    fib(num)