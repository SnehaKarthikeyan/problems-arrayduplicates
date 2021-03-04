Coding:
  
a=int(input())
b=list(map(int,input().split()))
t=[]
for i in b: 
    if i not in t: 
        t.append(i) 
c=len(t)
for i in range(0,c-1):
    print(t[i],end=" ")
print(t[c-1],end=" ")
