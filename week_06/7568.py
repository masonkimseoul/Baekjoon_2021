N=int(input())
weight=[]
height=[]
rank=[]
for i in range(N):
    wt,ht=map(int,input().split())
    weight.append(wt)
    height.append(ht)
    rank.append(1)
for i in range(N):
    for j in range(i+1,N):
        if weight[i]>weight[j] and height[i]>height[j]:
            rank[j]+=1
        elif weight[i]<weight[j] and height[i]<height[j]:
            rank[i]+=1
    rank[i]=str(rank[i])
print(" ".join(rank))

'''
#클래스 연습용
class student:
    def setdata(self, weight, height):
        self.weight=weight
        self.height=height
        self.rank=1

N=int(input())
stu_list=[]
answer=[]
for i in range(N):
    stu_list.append(student())
    w,h=map(int,input().split())
    stu_list[i].setdata(w,h)

for i in range(N):
    for j in range(i+1,N):
        if stu_list[i].weight>stu_list[j].weight and stu_list[i].height>stu_list[j].height:
            stu_list[j].rank+=1
        elif stu_list[i].weight<stu_list[j].weight and stu_list[i].height<stu_list[j].height:
            stu_list[i].rank+=1
for i in range(N):
    answer.append(str(stu_list[i].rank))
print(" ".join(answer))
'''