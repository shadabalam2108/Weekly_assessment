#1
lst=[3,1,2,4,7,6]
odd=[]
even=[]
for i in lst:
  if i%2==0:
      even.append(i)
  else:
      odd.append(i)
odd.extend(even)
print(odd)

#2
l=[16,17,4,3,5,2]
result=[]
for i in range(len(l)):
   for j in range(i+1,len(l)):
       if l[i]>l[j]:
          pass
    





#3
l=[2,1,3,5]
def fun(l):
   for i in range(len(l)):
      if sum(l[:i])==sum(l[i:]):
        return True
   return False
print(fun(l))

#4
l=[1,2,3,4,-5,-6,-7,-8]
result=[0]*len(l)
pos=1
neg=0
for i in l:
  if i<0:
    result[neg]=i
    neg+=2
  else:
    result[pos]=i
    pos+=2
print(result)

#5
l1=[1,2,3]
length=len(l1)//2
result=[length] if sum(l1[:length])==sum(l1[length+1:]) else []
print(result)
    
