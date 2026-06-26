student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course_name = input("Enter Course Name: ")

subject1 = float(input("Enter Marks in Subject 1: "))
subject2 = float(input("Enter Marks in Subject 2: "))
subject3 = float(input("Enter Marks in Subject 3: "))


total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

print("\n----- Student Details -----")
print("Student Name :", student_name)
print("Age          :", age)
print("City         :", city)
print("Course Name  :", course_name)
print("Subject 1    :", subject1)
print("Subject 2    :", subject2)
print("Subject 3    :", subject3)
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")