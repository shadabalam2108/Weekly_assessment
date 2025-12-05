l=[2, 4, 7, 8]
c=0
for i in l:
  if i%3==0 or i%5==0:
      c+=1
print(c)

s="hello world python"
c=""
result=""
for i in s:
   if i!=" ":
      c+=i
   else:
     result=c+" "+result
     c=""
result=c+" "+result
print(result)

str1="hello"
str2= "helllllllllo"
def fun(str1,str2):
     for i in str1:
       if i not in str2:
         return False
     for j in str2:
       if j not in str1:
         return False
     return True
print(fun(str1,str2))
     


r=4
for i in range(r):
   for j in range(r):
     if i==j:
       print("*",end="")
     else:
       print(" ",end="")
   print()

s="madam racecar apple"
s=s.split()
maximum=0
max_palindrome=""
for i in s:
   if len(i)>maximum:
      maximum=len(i)
      max_palindrome=i
print(max_palindrome)

