def decide():
    message = {"admin" : 12345, "root" : 123456, "timi" : 123}
    name = input("please enter a name：")
    if name in message.keys():
        password = int(input("please enter a password："))
        number = message.get(name, -1)
        if password == number:
            print("Welcome "+name+" login！")
        else:
            print("User name or password error, please log in again!")
    else:
        print("User name or password error, please log in again!")

decide()