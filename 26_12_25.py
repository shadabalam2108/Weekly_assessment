#1
from functools import reduce
lst=[2, 3, 4, 5]
result=[]
for i in range(len(lst)):
    result+=[reduce(lambda x,y:x*y,lst[:i]+lst[i+1:])]
print(result)

#2
employees = {
"John": 40000,
"Jane": 50000,
"Mike": 30000,
"Sara": 70000,
"Tom": 60000
}
lst1=sorted(employees.items(),key=lambda x:x[1],reverse=True)
print(lst1[:3])

#3
attendance = {
"Monday": ["Ahmed", "Fatima", "Hassan"],
"Tuesday": ["Fatima", "Ali", "Zainab"],
"Wednesday": ["Ahmed", "Hassan", "Ayesha"],
"Thursday": ["Fatima", "Ali", "Hassan"],
"Friday": ["Ahmed", "Fatima", "Zainab", "Ayesha"]
}
num_day={}
day=0
for i in attendance:
     for j in attendance[i]:
          num_day[j]=num_day.get(j,0)+1
for k in num_day:
    if num_day[k]>day:
        day=num_day[k]
        student=k
print(f"student name-{student},number of days-{day}")
       






#4
students = [
{"name": "Ahmed", "marks": [85, 90, 78]},
{"name": "Fatima", "marks": [92, 88, 95]},
{"name": "Hassan", "marks": [65, 70, 68]},
{"name": "Ayesha", "marks": [88, 85, 90]}
]
def calculate_average(marks_list):
     marks_list["average"]=sum(marks_list["marks"])/len(marks_list["marks"])
     return marks_list

average=list(map(calculate_average,students))
result=filter(lambda x:x["average"]>=80,average)
print(list(result))

#5
lst=[7, 8, 9, 11, 12]
def positive_integer(lst):
   for i in range(1,len(lst)+1):
      if i not in lst:
        return i
   return len(lst)+1
print(positive_integer(lst))
     
