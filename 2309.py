list=[]
flag=0
for _ in range(9):
    list.append(int(input()))
all_hobbit_length=sum(list)
for i in range(8):
    for j in range(i+1,9):
        if all_hobbit_length-100==list[i]+list[j]:
            list.pop(j)
            list.pop(i)
            flag=1
            break
    if flag==1:
        break
list.sort()
for i in list:
    print(i)