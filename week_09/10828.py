import sys

class stack:
    def __init__(self):
        self.top=[]

    def __len__(self):
        return len(self.top)

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            return -1

    def peek(self):
        if not self.isEmpty():
            print(self.top[-1])
        else:
            print(-1)

N=int(sys.stdin.readline())
a=stack()
for i in range(N):
    comd=list(map(str,sys.stdin.readline().split()))
    if comd[0]=="push":
        a.push(comd[1])
    elif comd[0]=="pop":
        print(a.pop())
    elif comd[0]=="size":
        print(len(a.top))
    elif comd[0]=="empty":
        if(a.isEmpty()==True):
            print(1)
        else:
            print(0)
    elif comd[0]=="top":
        a.peek()