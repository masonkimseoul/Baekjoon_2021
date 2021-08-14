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
calc=Stack
answer=0
tmp=0
flag=0
for i in par_array:
    if s.isEmpty():
        if i==')' or i==']':
            print(0)
            break
        s.push(i)
    else:
        if i=='(' or i=='[':
            s.push(i)
        elif i==')':
            if s.peek()=='(':
                s.pop()


    '''
    if s.isEmpty():
        if i==')' or i==']':
            print(0)
            break
        s.push(i)
    else:
        if i=='(' or i=='[':
            s.push(i)
            if tmp!=0:
                answer+=tmp
                tmp=0
        elif i==')':
            if s.peek()=='(':
                s.pop()
                if flag==0:
                    if s.isEmpty():
                        if tmp==0:
                            tmp+=2
                            answer+=tmp
                        else:
                            answer+=tmp
                            answer*=2
                        tmp=0
                        flag=1
                    elif tmp==0:
                        tmp+=2
                    else:
                        tmp*=2
                else:
                    if s.isEmpty():
                        if tmp==0:
                            tmp+=2
                        else:
                            tmp*=2
                        answer+=tmp
                    elif tmp==0:
                        tmp+=2
                    else:
                        tmp*=2

            elif s.peek()=='[':
                print(0)
                break
        elif i==']':
            if s.peek()=='[':
                s.pop()
                if s.isEmpty():
                    if tmp == 0:
                        tmp += 3
                    answer += tmp
                    tmp = 0
                elif tmp==0:
                    tmp+=3
                else:
                    tmp*=3
            elif s.peek()=='(':
                print(0)
                break
    print(answer, tmp, flag)
print(answer)
    '''