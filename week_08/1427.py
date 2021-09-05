#bubble sort
'''
N=list(str(input()))
for i in range(len(N)-1):
    for j in range(len(N)-1):
        if N[j+1]>N[j]:
            N[j+1],N[j]=N[j],N[j+1]
print("".join(N))
'''
#insertion sort
N=list(str(input()))
for i in range(len(N)):
    for j in range(i,0,-1):
        if N[j]>N[j-1]:
            N[j],N[j-1]=N[j-1],N[j]
print("".join(N))