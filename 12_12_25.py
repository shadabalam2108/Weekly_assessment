#1
s="hello"
reverse=""
def fun(s):
  global reverse
  for i in s:
     reverse=i+reverse
  return reverse
print(fun(s))

#2
n1=19
n2=91
sum_n1=0
sum_n2=0
while n1>0 or n2>0 :
    sum_n1+=n1%10
    sum_n2+=n2%10
    n1//=10
    n2//=10
print(sum_n1==sum_n2)

#3
num=1234
sum_num=0
while num>0:
   sum_num+=num%10
   num//=10
   if sum_num>9 and num==0:
     num=sum_num
     sum_num=0
print(sum_num)

#4
List_A= [1, 5, 3]
List_B= [0, 5, 2]
count=0
for i in range(len(List_A)):
  if List_A[i]>List_B[i]:
    count+=1
print(count)

#5
string="abcaad"
ch = 'a'
list1=[]
for i in range(len(string)):
  if string[i]==ch:
     list1.append(i)
list2=[]
for j in range(len(list1)-1):
  list2.append(list1[j+1]-list1[j])
print(min(list2))
  
       



   


    
   
