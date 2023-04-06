# 请编写一个程序，实现下列功能：程序带三个正整数作为命令行参数，
# 如果其中任意一个数大于或等于另两个数之和，则输出False，否则输出True
num1=input("Please enter the first parameter；")
num2=input("Please enter the second parameter：")
num3=input("Please enter the third parameter：")

if(num1 >= num2+num3 and num2 >= num1+num3 and num3 >= num1+num2):
    print("True")
else:
    print("False")