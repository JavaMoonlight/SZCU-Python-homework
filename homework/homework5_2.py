def panel(homework):
    oper = {"entering" : 1, "checking" : 2, "exiting" : 3}
    print("================================")
    print("What you can do is:")
    print("1-----entering")
    print("2-----checking")
    print("3-----exiting")
    print("================================")
    number = int(input("Please confirm your action："))
    if number == oper["entering"]:
        num = 0;
        add(homework, num)
    elif number == oper["checking"]:
        check(homework)
    elif number == oper["exiting"]:
        exit()

def add(homework, num):
    if num == 4:
        print("Error,too many failures")
        panel(homework)
    else:
        name = input("Please enter the name of the student：")
        data = input("Please enter the submission time：")
        state = input("Please enter the submission status：")
        num += 1;
        reconfirm = input("Are you sure about your input?true or false")
        if reconfirm == "false":
            add(homework, num)
        elif reconfirm == "true" and (name == "" or data == "" or state == ""):
            print("There was a problem with the input. Please reenter it")
            add(homework,num)
        elif reconfirm == "true":
            message = {"name":name, "data":data, "state":state}
            homework.append(message)
            flag = input("Need to continue?true or false")
            if flag == "true":
                add(homework, num=0)
            elif flag == "false":
                panel(homework)

def check(homework):
    print(homework)
    panel(homework)

def user():
    homework1 = {"name": "John", "data": "2023.3.31", "state": "true"}
    homework2 = {"name": "tom", "data": "2023.3.31", "state": "true"}
    homework3 = {"name": "jack", "data": "2023.3.31", "state": "true"}
    homework = [homework1, homework2, homework3]
    panel(homework)

user()