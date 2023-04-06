import numpy as np

def sigmoid(x):
    num = 1/(1+np.exp(-x))
    print(num)

def main():
    print("请输入一个数字并进行计算")
    x = float(input())
    sigmoid(x)

main()