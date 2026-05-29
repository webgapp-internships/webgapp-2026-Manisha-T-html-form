students=["Manisha","Nisha","Yudhu"]
department=("CSE","MECH","ECE")
def Student_details(name,dept):
    print("Student name:",name)
    print("Department:",dept)
    print("--------------------")
for i in range(len(students)):
    Student_details(students[i],department[i])