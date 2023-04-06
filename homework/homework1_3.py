# 星期判断(Day of the week)。请编写一个程序，完成下列功能:
# 接收一个日期作为输入，输出日期所对应的星期。程序接收三个命令行参数:m(月)、d(日)和y(年)。
# 月份m为1时表示一月份,m为2时表示二月份，以此类推。
# 输出0表示星期日，1表示星期一，2表示星期二,以此类推。
def FinalDay(y, m, d):
    y1 = y - (14 - m) / 12
    x = y1 + y1 / 4 - y1 / 100 + y1 / 400
    m1 = m + 12 * ((14 - m) / 12) - 2
    d1 = int((d + x + (31 * m1) / 12) % 7)
    if d1 == 0:
        print("The week corresponding to the date entered is : Sunday")
    elif d1 == 1:
        print("The week corresponding to the date entered is : Monday")
    elif d1 == 2:
        print("The week corresponding to the date entered is : Tuesday")
    elif d1 == 3:
        print("The week corresponding to the date entered is : Wednesday")
    elif d1 == 4:
        print("The week corresponding to the date entered is : Thursday")
    elif d1 == 5:
        print("The week corresponding to the date entered is : Friday")
    elif d1 == 6:
        print("The week corresponding to the date entered is : Saturday")

def IsLeapYear(day1):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 31 >= d >= 1:
            FinalDay(y, m, d)
    elif m == 2:
        if day1 >= d >= 1:
            FinalDay(y, m, d)
    else:
        FinalDay(y, m, d)

m = int(input("Please Enter month："))
d = int(input("Please Enter day："))
y = int(input("Please Enter year："))

if (y % 4) == 0 and (y % 100)== 0 and (y % 400) == 0:
    day1 = 29
    IsLeapYear(day1)
else:
    day1 = 28
    IsLeapYear(day1)
