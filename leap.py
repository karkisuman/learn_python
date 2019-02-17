year=int(input("enter year to be checked\n"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("the year is leap year")
else:
    print("the year is not leap year")