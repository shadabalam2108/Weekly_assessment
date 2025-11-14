#que 1::

l=["race", "care", "note", "tone", "state", "taste", "abc", "bca"]
d={}
for i in l:
  d["".join(sorted(i))]=d.get("".join(sorted(i)),())+(i,)
print(list(d.values()))

#que 2::

d1 = {'x': 10, 'y': 20, 'z': 30}
d2 = {'y': 15, 'z': 45, 'w': 50}
for i in d2:
  d1[i]=d1.get(i,0)+d2[i]
print(d1)

#que 3::
d={'p': 3, 'q': 1, 'r': 3, 's': 2}
d1={}
for i in d:
   d1[d[i]]=d1.get(d[i],[])+[i]	
print(d1)

#que 4::

d={'k': 90, 'l': 40, 'm': 70, 'n': 20, 'o': 60}
s=sorted(d.values())
if len(s)>=3:
   for i in d:
     if d[i]==s[-3]:
         print(i)
else:
   print("Not enough values")
         
#que 5::

d={'u': 12, 'v': 5, 'w': 25, 'x': 7}
s=list(d.items())
for i in range(len(s)):
   for j in range(i+1,len(s)):
       if s[i][1]>s[j][1]:
          s[i],s[j]=s[j],s[i]
print(dict(s))

   
 


