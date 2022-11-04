subject1 = int(input("Enter subject1 mark:"))
subject2 = int(input("Enter subject2 mark:"))
subject3 = int(input("Enter subject3 mark:"))
subject4 = int(input("Enter subject4 mark:"))
subject5 = int(input("Enter subject5 mark:"))
total_subjects = [subject1,subject2,subject3,subject4,subject5]
length = len(total_subjects)
total_marks = 0
for i in range(length):
    total_marks += total_subjects[i]
print("Total marks :",total_marks)
    
for j in range(length):
    if total_subjects[j]>=35:
        print("pass")
    else:
        print("fail")
