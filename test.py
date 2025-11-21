
d={
"user": {
"firstname": "Alice",
"lastname": "Brown"
},
"age": 30
}
flat={}
def fun(d,path=""):
    for i in d:
          if isinstance(d[i],dict):
              fun(d[i],path+i+".")
          else:
            flat[path+i]=d[i]
    return flat
print(fun(d))


l=[3, 1, 3, 2, 2, 4]
uniq=[]
for i in l:
   if i not in uniq:
      uniq.append(i)
print(uniq)

l=[1, 5, 2, 5, 3]
for i in range(len(l)):
   if l[i] in l[i+1:]:
      print(l[i])
      break

st="Hello"
c=""
length=0
for i in st:
    if i!=" ":
      c+=i
    elif c:
      length+=1
      c=""
if c:
  length+=1
print(length)


d={'m': 22, 'n': 10, 'o': 35, 'p': 18}
d_items=list(d.items())
for i in range(len(d_items)):
   for j in range(i+1,len(d_items)):
     if d_items[i][1]>d_items[j][1]:
         d_items[i],d_items[j]=d_items[j],d_items[i]
print(dict(d_items))
      
       

            


   
 


