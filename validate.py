name=input("enter the name here\n")
num=input("enter the number\n")
age=input("enter your age\n")
if name.isalpha(name):
    print("valid name")
if num.isdigit(num):
    print("valid number")
if age.isdigit(age):
    print("age is valid ")
if name.isnull(name):
    print("enter the name ")
if age.isnull(age):
    print("field should not  be empty")
if num.isnull(num):
    print("field is empty")



