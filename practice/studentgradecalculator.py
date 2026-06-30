def get_grades(marks):
    if marks >89 and marks<101:
        return "A+"
    elif marks>79 and marks <90:
        return "A"
    elif marks>69 and marks<80:
        return "B"
    elif marks>59 and marks<70:
        return "C"
    elif marks<60:
        return "fail"
stu=[]
n=int(input("enter total noum of student"))
for i in range(n):
    name=input("enter name of student")
    marks=int(input("enter marks of student"))
    stu.append((name,marks))

for names,mark in stu:
    grade=get_grades(mark)
    print(f"{names} and the {mark}scored report is {grade}")