s="I love Python"
s1="Python is awesome"
s=s.split()
s1=s1.split()
result=[]
for i in s:
   if i in s1:
     result.append(i)
print(result)


l=[1, 2, 3, 4, 6]; k = 6
for i in range(len(l)):
  for j in range(i+1,len(l)):
     if l[i]*l[j]==k:
         print((l[i],l[j]),end=" ")

s="aeiou"
vowel="aeiou"
str_vowel=[i for i in s if i in vowel]
result=""
for j in s:
  if j in vowel:
     result+=str_vowel[-1]
     str_vowel.pop() 
  else:
     result+=j
print(result)


l=[2, 5, 6, 7]; target = 4
m=float("inf")
for i in l:
  dif=abs(target-i)
  if m>dif:
    m=dif
    result=i
print(result)


l=["interview", "internet", "internal"]
l.sort()
result=""
for i in range(len(l[0])):
    if l[0][i]==l[-1][i]:
       result+=l[0][i]
    else:
      break
print(result)
       



      