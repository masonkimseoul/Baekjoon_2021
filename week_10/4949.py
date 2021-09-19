import sys

str=sys.stdin.readline().replace('\n','')
parentheses=[]
while str!=".":
    flag=0
    parentheses.clear()
    for i in range(len(str)):
        if str[i]=='(' or str[i]=='[':
            parentheses.append(str[i])
        elif str[i]==')':
            if len(parentheses)==0:
                print("no")
                flag+=1
                break
            elif parentheses[-1]=='[':
                print("no")
                flag+=1
                break
            parentheses.pop()
        elif str[i]==']':
            if len(parentheses) == 0:
                print("no")
                flag+=1
                break
            elif parentheses[-1] == '(':
                print("no")
                flag+=1
                break
            parentheses.pop()
    if flag==0:
        if len(parentheses)==0:
            print("yes")
        else:
            print("no")
    str=sys.stdin.readline().replace('\n','')