array=[]
num=0
for i in range(1,10001):
    num+=i
    while i>0:
        num+=(i%10)
        i//=10
    array.append(num)
    num=0
for i in range(1,10001):
    if i in array:
        continue
    print(i)