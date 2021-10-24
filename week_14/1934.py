N=int(input())
for i in range(N):
    x,y=map(int,input().split())
    X,Y=x,y
    while x%y!=0:
        tmp=x%y
        x=y
        y=tmp
    print(X*Y//y)
'''
유클리드 호제법
x=yq+r일 때
x와 y의 최대공약수는 y와 r의 최대공약수와 같다
위 코드는 x, y 입력 후 r값 구하고 y와 r 최대공약수 구할 때까지 while 돌림

최소공배수 = x*y // 최대공약수
'''