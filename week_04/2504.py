class Stack:
    def __init__(self):
        self.top=[]
    def isEmpty(self):
        return len(self.top)==0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            exit()
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

par_array=list(input())
s=Stack()
answer=0
tmp=1
flag=0
for i in par_array:
    if i=='(':
        s.push(i)
        tmp*=2
    elif i=='[':
        s.push(i)
        tmp*=3
    elif i==')':
        if len(s.top)==0 or s.peek()=='[':
            answer=0
            break
        if flag=='(':
            answer+=tmp
        tmp//=2
        s.pop()
    elif i==']':
        if len(s.top)==0 or s.peek()=='(':
            answer=0
            break
        if flag=='[':
            answer+=tmp
        tmp//=3
        s.pop()
    flag=i
if not s.isEmpty():
    answer=0
print(answer)