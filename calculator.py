num1=int(input("enter first number\n"))
num2=int(input("enter second number\n"))

op=input("enter operator\n")
result=0

if op=="+":
    result=num1+num2
elif op=="-":
     result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    result=num1/num2
elif op=="%":
    result=num1%num2
else:
    result="invalid inputs"
print("Result",result)