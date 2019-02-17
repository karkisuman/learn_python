list=[]
new_list=[]
n=int(input("enter how many numbers\n"))
for i in range(n):
    num=int(input("enter the number\n"))
    list.append(num)
    if(num%2==0):
        new_list.append(num)
        print("result",new_list)

        
