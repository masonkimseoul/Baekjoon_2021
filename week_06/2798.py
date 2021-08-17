from itertools import combinations
N,M=map(int,input().split())
card_val=list(map(int,input().split()))

available_set=set(combinations(card_val,3))
answer=0
for i in available_set:
    if sum(i)>M:
        continue
    else:
        answer=max(answer,sum(i))
print(answer)