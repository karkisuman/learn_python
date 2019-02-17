list=[]
num=int(input("enter how many numbers?"))
for i in range(num):
    numbers=int(input("enter the number"))
    list.append(numbers)
print("maximum element in the list:",max(list),"\nminimum element in the list:",min(list))

