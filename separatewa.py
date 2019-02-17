list=[23,2.40,'suman',11,'aarju',63.33]
int_list=[]
float_list=[]
string_list=[]
for i in list:
    if(type(i)==int):
        int_list.append(i)
    elif(type(i)==float):
        float_list.append(i)
    elif(type(i)==str):
        string_list.append(i)
print(int_list)
print(float_list)
print(string_list)
