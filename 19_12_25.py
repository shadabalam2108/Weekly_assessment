#1
String = "leetcode"
Dict = ["leet", "code", "leetcode"]
def fun(String):
    if String in Dict:
       return True
    return False
print(fun(String))

#2
coins = [2, 2, 5]
amount = 10
output=float("inf")
for i in coins:
    if amount%i==0:
      if output>amount//i:
         output=amount//i
print(output) if output!=float("inf") else print(-1)
    
         
       
       
      



#3
Input="abcabcdebb"
temp=""
stack=[]
for i in Input:
   if i not in temp:
     temp+=i
   else:
     stack.append(len(temp))
     temp=i
print(max(stack))

#4
string="4[x]1[y]"
stack=[]
curr=""
num=0
for i in string:
   if i.isdigit():
     num=num*10+int(i)
   elif i=="[":
      stack.append((curr,num))
      curr=""
      num=0
   elif i=="]":
     pr,n=stack.pop()
     curr=pr+n*curr
   else:
     curr+=i
print(curr)

#5
str1="python,,,,,java,,c++"
stack=[]
temp=""
for i in str1:
    if i!=",":
      temp+=i
    elif temp:
      stack.append(temp)
      temp=""
if temp:
 stack.append(temp)
print(",".join(stack))

