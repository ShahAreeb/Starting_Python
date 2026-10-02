name1=input("Enter student's name : ")
age1=int(input("Enter student's age : "))
marks1=int(input("Enter student's marks : "))
student={
    "Name":name1,
    "Age":age1,
    "Marks":marks1
}
print("Student details\n")
print("NAME:",student["Name"])
print("AGE:",student["Age"])
print("MARKS:",student["Marks"])
