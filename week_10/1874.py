'''
#무지성으로 쓴 코드, 정답은 맞는데 지저분하다
import sys

N=int(sys.stdin.readline())
stack_num=[]
answer_num=[]
answer_str=[]
num=0
for i in range(N):
    tmp=int(sys.stdin.readline())
    if tmp>num:
        while num!=tmp:
            num+=1
            stack_num.append(num)
            answer_str.append('+')
        answer_num.append(stack_num.pop())
        answer_str.append('-')
    else:
        if num==N and tmp<stack_num[-1]:
            print("NO")
            exit()
        if tmp==answer_num[-1]:
            answer_num.append(stack_num.pop())
            answer_str.append('-')
        else:
            while tmp!=answer_num[-1]:
                answer_num.append(stack_num.pop())
                answer_str.append('-')
for i in answer_str:
    print(i)
'''

#종이에 스택 그리면서 푼 코드, 훨씬 깔끔함
import sys

N=int(sys.stdin.readline())
stack=[]
answer=[]
max=1
for i in range(N):
    val=int(sys.stdin.readline())
    if len(stack)!=0 and stack[-1]>val:
        print("NO")
        exit()
    else:
        while val>=max:
            stack.append(max)
            max+=1
            answer.append('+')
        if stack[-1]==val:
            stack.pop()
            answer.append('-')
for i in answer:
    print(i)
