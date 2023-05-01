student_dic = {}
n = int(input("Enter no.of students:"))
for i in range(1, n + 1):
    l = []
    sno = int(input("Enter student roll number:"))
    sname = input("Enter student name:")
    group = input("Enter name of the group:")
    college = input("Enter name of the college:")
    branch = input("Enter name of the branch:")
    sphno = int(input("Enter student phone number:"))
    l.append(sname)
    l.append(group)
    l.append(college)
    l.append(branch)
    l.append(sphno)
    student_dic[sno] = l
print(student_dic)
