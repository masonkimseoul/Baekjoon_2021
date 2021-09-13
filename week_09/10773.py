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

N=int(sys.stdin.readline())
a=stack()
sum=0
for i in range(N):
    tmp=int(sys.stdin.readline())
    if tmp!=0:
        a.push(tmp)
        sum+=tmp
    else:
        sum-=a.pop()
print(sum)