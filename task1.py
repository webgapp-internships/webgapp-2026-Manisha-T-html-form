marks=[100,57,85,80,88]
def check_result(mark):
    if mark>=90:
        return "Grade A"
    elif mark>=70:
        return "Grade B"
    else:
        return "Grade C"

for i in range(len(marks)):
    result = check_result(marks[i])
    print("Student", i + 1, ":", result)
