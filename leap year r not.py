year=int(input("Enter year:"))
if(year%4==0 and year%100!==0 or year%400==0):
    print("IT IS A LEAP YEAR")
else:
    print(NOT A LEAP YEAR")
