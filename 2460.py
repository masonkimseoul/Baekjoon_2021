head=0
max=0
for _ in range(10):
    a,b=map(int, input().split( ))
    head-=a
    head+=b
    if head>max:
        max=head
print(max)