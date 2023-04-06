def explain(i, egg, bag, book,shoping):
    print("================================")
    print("What you can do is:")
    print("1-----buy")
    print("2-----check")
    print("3-----exit")
    print("================================")
    num = int(input("Enter what you want to do："))
    commodity(i, egg, bag, book, num,shoping)

def commodity(i, egg, bag, book, num, shoping):
    sum = 0
    # 购买系统
    if num == 1:
        ID = int(input("Please enter the ID of the item you want to purchase："))
        if ID == 1:
            if i >= egg[2]:
                sum += egg[2]
                shoping.append(egg[1])
            else:
                print("Insufficient balance, please re-operate")
                explain(i, egg, bag, book, shoping)
        elif ID == 2:
            if i >= bag[2]:
                sum += bag[2]
                shoping.append(bag[1])
            else:
                print("Insufficient balance, please re-operate")
                explain(i, egg, bag, book, shoping)
        elif ID == 3:
            if i >= book[2]:
                sum += book[2]
                shoping.append(book[1])
            else:
                print("Insufficient balance, please re-operate")
                explain(i, egg, bag, book, shoping)
        i -= sum
        flag = input("Do you need to keep buying： true or false?")
        if flag == "true":
            commodity(i, egg, bag, book, num, shoping)
        elif flag == "false":
            explain(i, egg, bag, book, shoping)

    # 查看系统
    elif num == 2:
        print("The items you purchased are:", shoping)
        print("Your balance is:",i)
        explain(i, egg, bag, book, shoping)

    # 退出系统
    elif num == 3:
        print("The items you purchased are:", shoping)
        print("Your balance is:", i)
        exit()

def user():
    shoping = []
    salary = int(input('please enter your salary: '))
    egg = (1, '鸡蛋', 20)
    bag = (2, '包', 200)
    book = (3, '书籍', 50)
    print("The items available for purchase are as follows:")
    print(egg, bag, book)
    explain(salary, egg, bag, book, shoping)

user()