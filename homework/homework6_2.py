def operation(id):
    num = []
    sum = 0
    for i in id:
        num.append(int(i))

    for i in range(0,len(num)+1):
        if i == 0 or i == 10:
            sum += (num[i] * 7)
        elif i == 1 or i == 11:
            sum += (num[i] * 9)
        elif i == 2 or i == 12:
            sum += (num[i] * 10)
        elif i == 3 or i == 13:
            sum += (num[i] * 5)
        elif i == 4 or i == 14:
            sum += (num[i] * 8)
        elif i == 5 or i == 15:
            sum += (num[i] * 4)
        elif i == 6 or i == 16:
            sum += (num[i] * 2)
        elif i == 7:
            sum += (num[i] * 1)
        elif i == 8:
            sum += (num[i] * 6)
        elif i == 9:
            sum += (num[i] * 3)
    if sum % 11 == 0:
        print("ID is :" + (id + "1"))
    elif sum % 11 == 1:
        print("ID is :" + (id + "0"))
    elif sum % 11 == 2:
        print("ID is :" + (id + "x"))
    elif sum % 11 == 3:
        print("ID is :" + (id + "9"))
    elif sum % 11 == 4:
        print("ID is :" + (id + "8"))
    elif sum % 11 == 5:
        print("ID is :" + (id + "7"))
    elif sum % 11 == 6:
        print("ID is :" + (id + "6"))
    elif sum % 11 == 7:
        print("ID is :" + (id + "5"))
    elif sum % 11 == 8:
        print("ID is :" + (id + "4"))
    elif sum % 11 == 9:
        print("ID is :" + (id + "3"))
    elif sum % 11 == 10:
        print("ID is :" + (id + "2"))

def enter():
    card = input("Please enter a 17-digit ID number：")
    if len(card) == 17:
        operation(card)
    else:
        print("Please re-enter more than 17 digits")
        enter()

enter()