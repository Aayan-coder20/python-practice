# AIM: Write a Python program to create,
# update, and manipulate a dictionary of student records,
# including their grades and attendance.
# Coder: Aayan Khan
# Date:26-01-2026



print("--- Student Records Manager ---")

students = {
    "251P005": {"name": "Sameer", "grade": "A", "attendance": 68},
    "251P055": {"name": "Abdulla", "grade": "B+", "attendance": 88},
    "251P026": {"name": "Katrina", "grade": "A-", "attendance": 55}
}

print("Current Student Records:", students)

uin = input("Enter New Student UIN: ")
name = input("Enter New Student Name: ")
grade = input("Enter New Student Grade: ")
attendance = int(input("Enter New Student Attendance: "))

students[uin] = {
    "name": name,
    "grade": grade,
    "attendance": attendance
}

update_uin = input("Enter UIN to Update: ")
new_grade = input("Enter New Grade of Student: ")

students[update_uin]["grade"] = new_grade

delete_uin = input("Enter UIN of the Student to Delete: ")

students.pop(delete_uin)

print("Final Student Records:", students)
