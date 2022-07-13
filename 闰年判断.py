#获得要检验的年份
year=int(input("year : "))
#1.能被400整除：为闰年
if year%400==0:
    print(str(year)+" is a闰年")
#2.能被4整除且不能被100整除：为闰年
elif (year%4==0) & (year%100!=0):
    print(str(year)+" is a 闰年")
#不能满足判断的年份均为非闰年
else:
    print(str(year)+" is not a 闰年")