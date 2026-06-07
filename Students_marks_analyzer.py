# Project: Student Marks Analyzer
# Author: Sri Sahana
# Concepts Used:
# - Lists
# - Loops
# - Conditional Statements
# - Built-in Functions (sum, max, min, len)
n=int(input("How many students marks you have= "))
marks=[]
for i in range(n):
    mark=int(input("Enter mark= "))
    marks.append(mark)
print(marks)


total=sum(marks)
print("total= ",total)
average=sum(marks)/len(marks)
print("Average= ",average)
print("Highest score= ",max(marks))
print("Lowest score= ",min(marks))


fail=[]
passed_students=[]
for mark in (marks):
    if mark<35:
        fail.append(mark)
    else:
        passed_students.append(mark)

        
print("Number of fails= ",len(fail))
print("Failed marks= ",fail)
print("Number of passed students= ",len(passed_students))
print("Passed student marks= ",passed_students)
