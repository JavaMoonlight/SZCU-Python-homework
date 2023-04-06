import random
def birthday(num):
    x = 1
    for i in range(365-num+1, 365+1):
        x *= i
    return 1 - (x / 365 ** num)

def main():
    number = int(input('Please enter the number of people in the room：'))
    if number >= 0:
        result = birthday(number)
        print("The probability is {:.2f}%".format(result*100))
    else:
        print('input error')

main()