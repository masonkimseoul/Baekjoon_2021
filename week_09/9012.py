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
            return self.top[-1]
        else:
            return -1

N=int(sys.stdin.readline())
a=stack()
flag=0
for i in range(N):
    str=list(sys.stdin.readline())
    for j in str:
        if j=='(':
            a.push(j)
        elif j==')':
            if a.peek()=='(':
                a.pop()
            else:
                print("NO")
                flag=1
                break
    if flag==0:
        if a.isEmpty()==True:
            print("YES")
        else:
            print("NO")
            while(a.isEmpty()==False):
                a.pop()
    flag=0