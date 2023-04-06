import math

def evaluate(x, a):
    sum = 0.0
    for i in range(0, len(a), 1):
        numbers = float(a[i])*math.pow(x,i)
        sum += numbers
    print("计算结果为：",sum)
    number = math.exp(x)
    print("e的x次方的值为：",number)
    if sum > number :
        print("sum的值较大")
    elif sum == number :
        print("sum的值和math.exp所求结果相等")
    elif sum < number :
        print("sum的值较小")

def exp(x):
    arr = [None] * (x+1)
    arr[0] = "1.0"
    number = 1
    for i in range(1, x+1, 1):
        number *= 1/i
        arr[i] = str(number)
    print("列表的值为：",arr)
    evaluate(x,arr)

def main():
    print("please enter a number:")
    number = int(input())
    if number < 0:
        print("please enter again")
    else:
        exp(number)

main()