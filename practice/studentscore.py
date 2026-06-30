students=[("yash",40),("rahu",90),("rohit",70),("mayank",50),("rachit",75),("sun",99),("tanu",35),("harsh",88),("unu",66),("rish",87),]
student=[name for name,score in students if score>=60 ]
print(f"students who scored 60+ :{student}")
stu=[name for name,score in students if score>=80]
print(f"top performers who scored 80+{stu}")
gen=(sum(score for name,score in students ))/10
print(f"average class {gen}")
status = {name: ("Pass" if score >= 60 else "Fail") for name, score in students}
print(status)