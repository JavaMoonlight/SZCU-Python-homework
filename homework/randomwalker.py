import random
import numpy as np

# 初始化地图
def Init(num, map):
    h = z = int((2*num)/2)
    map[z][h] = 1       # 初始化位置为1，最后count的值为地图中1的数量-1
    count = 0
    walk(h,z,map,count,num)

# 移动
def walk(h,z,map,count,num):
    i = random.random()
    if h == 2*num-1 or h == 0 or z == 0 or z == 2*num-1:
        print(map)
        print("一共耗费的步数为：")
        print(count)
    elif 0.25 > i >= 0:  # 向东移动一格
        if map[z][h+1] != 1 :
            map[z][h+1] += 1
            h = h+1
            count += 1
        walk(h,z,map,count,num)
    elif 0.25 <= i <= 0.5:  # 向南移动一格
        if map[z+1][h] != 1 :
            map[z+1][h] += 1
            z = z+1
            count += 1
        walk(h,z,map,count,num)
    elif 0.5 <= i <= 0.75:  # 向西移动一格
        if map[z][h-1] != 1:
            map[z][h-1] += 1
            h = h - 1
            count += 1
        walk(h,z,map,count,num)
    elif 0.75 <= i < 1:  # 向北移动一格
        if map[z-1][h] != 1:
            map[z-1][h] += 1
            z = z - 1
            count += 1
        walk(h,z,map,count,num)
def main():
    print("请输入一个整数n，将生成2n*2n的正方形")
    n = int(input())
    map = np.zeros((2*n, 2*n))
    print(map)
    print()
    Init(n,map)

main()