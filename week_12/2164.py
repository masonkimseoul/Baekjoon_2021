import sys
from collections import deque
#queue.Queue는 멀티쓰레드 사용할 때 써서 느림
#속도를 위해선 collections deque을 사용할 것
deque=deque()

N=int(sys.stdin.readline())
for i in range(1,N+1):
    deque.append(i)
cnt=N

while cnt>1:
    deque.popleft()
    cnt-=1
    deque.append(deque.popleft())
print(deque.popleft())