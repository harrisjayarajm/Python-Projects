n=int(input("how many students?"))
student={}
for i in range(n):
    name=input(f"enter the name of the student:{i+1}:")
    mark=int(input(f"enter mark of{name}:"))
    student[name]=mark
    print("\n dictionary:",student)
    topper=max(student,key=student.get)
    print("topper:",topper,"with",student[topper],"marks")