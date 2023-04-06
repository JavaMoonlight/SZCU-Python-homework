# def transform(num):
#     result = "{:b}".format(num)
#     print(result)

def transform(num):
    if num == 0:
        return ""
    return transform(num//2) + str(num%2)

def main():
    print("请输入要转换的十进制数：")
    num1 = int(input())
    if num1 > 0:
        result = transform(num1)
        print("转换为二进制后为："+result)
    elif num1 == 0:
        print("0")

main()