N=int(input())
for i in range(N):
    num=int(input())
    a=[]
    b=[]
    while num>0:
        a.append(num%2)
        num//=2
    for j,a in enumerate(a):
        if a==1:
            b.append(j)
    for j in b:
        print(j,end=' ')
''' 이진수 더 짧은 코드
for _ in range(int(input())):
    n=int(input())
    i=0
    while n>0:
        if n%2==1:
            print(i,end=' ')
        n=n//2
        i+=1
'''