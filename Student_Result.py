'''Enter Student Name: Ravi

Enter Python Marks: 80
Enter SQL Marks: 70
Enter DBMS Marks: 90

----- STUDENT RESULT -----

Student Name: Ravi
Total Marks: 240
Average: 80
Percentage: 80%
Result: Pass'''
student_name = input("Enter Student Name : ")
python_marks = input("Enter Python Marks : ")
sql_marks = input("Enter Sql MArks : ")
dbms_marks = input("Enter DBMS Marks : ")
total_marks = int(python_marks)+int(sql_marks)+int(dbms_marks)
avg_marks = total_marks/3
percentage = int((total_marks/300)*100)

print(" --------- STUDENT RESULT -------- ")
print("Student Name: " , student_name)
print("Total Marks: ", total_marks)
print("Average: ", avg_marks)
print("Percentage: ", str(percentage) + "%")

if python_marks >= 35 and sql_marks >= 35 and dbms_marks >= 35:
    print("Result : Pass")
else:
    print("Result : Fail")



