def judge(object):
    if len(object) % 2 == 0:
        index = int(len(object)/2);
    elif len(object) % 2 != 0:
        index = int(len(object)/2+1)
    num = object[index:len(object)]
    num = num[::-1]
    if len(object) % 2 == 0 and num in object[:index]:
        print(object+" is palindromic number");
    elif num in object[:index-1]:
        print(object+" is palindromic number");
    else:
        print(object+" is not palindromic number")
def operator():
    object = input("Please enter a string：")
    judge(object)

operator()