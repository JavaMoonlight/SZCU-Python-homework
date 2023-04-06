# 请编写一个程序，实现下列功能，程序带两个整数命令行参数m和d，
# 如果m月份d日的日期位于3月20日和6月20日之间，则输出True，否则输出False。
# 注：假设m=1代表1月份，m=2代表2月份，以此类推

m = input("Please enter month：")
d = input("Please enter day：")

month = int(m)
day = int(d)

if 6 > month > 3:
    if month==4 and 0<day<30:
        print("True")
    elif month==5 and 0<day<31:
        print("True")
elif month == 6:
    if 0 < day <= 20:
       print("True")
    else:
        print("False")
elif month == 3:
    if day >= 20:
        print("True")
    else:
        print("False")
else:
    print("False")