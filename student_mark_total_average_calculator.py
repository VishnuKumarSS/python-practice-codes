student_list=[]
def students(a):
    for i in range(a):
        name=input(f"Enter name{i+1}: ")
        student_list.append(name)

mark_list=[]
def marks(k):
    total=0
    print(f"Enter marks of {student_list[k]}")
    for i in range(5):
        mark=int(input(f"Enter mark{i+1}: "))
        mark_list.append(mark)
    for i in range(len(mark_list)):
        total+=mark_list[i]
    print(f"Total mark of {student_list[k]} is",total)
    average=total/len(mark_list)
    print(average)

def calculate():
    a=int(input("Enter how many students: "))
    students(a)
    print(len(student_list))
    for i in range(len(student_list)):
        marks(i)    
calculate()

