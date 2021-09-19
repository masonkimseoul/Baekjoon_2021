import sys

class queue:
    def __init__(self):
        self.a=[]
        self.b=[]

    def len_(self):
        return len(self.a)+len(self.b)

    def isEmpty(self):
        return len(self.a)+len(self.b)==0

    def push(self, item):
        self.a.append(item)

    def pop_(self):
        if self.isEmpty():
            return -1
        elif len(self.b)==0:
            while len(self.a)!=0:
                    self.b.append(self.a.pop())
        return self.b.pop()

    def front(self):
        if self.isEmpty():
            return -1
        elif len(self.b)==0:
            return self.a[0]
        else:
            return self.b[-1]

    def back(self):
        if self.isEmpty():
            return -1
        elif len(self.a)==0:
            return self.b[0]
        else:
            return self.a[-1]

N=int(sys.stdin.readline())
Q=queue()

for i in range(N):
    comd=list(map(str,sys.stdin.readline().split()))
    if comd[0]=='push':
        Q.push(comd[1])
    elif comd[0]=='pop':
        print(Q.pop_())
    elif comd[0]=='size':
        print(Q.len_())
    elif comd[0]=='empty':
        print(int(Q.isEmpty()))
    elif comd[0]=='front':
        print(Q.front())
    elif comd[0]=='back':
        print(Q.back())