import sys
def operator(count):
    user = input("Please enter your password: ")
    if count > 5:
        print("You have entered forbidden entry more than 5 times")
        sys.exit()
    elif 5 <= len(user) <= 10 and user.isalnum():
        judge(user,count)
    else:
        print("Error")
        count+=1
        operator(count)

def judge(user,count):
    # list = []
    # list_isUpper = []
    # list_isLower = []
    # for i in range(0, len(user),1):
    #     if ord('a')<=ord(user[i])<ord('z'):
    #         list_isUpper.append(user[i])
    #     elif ord('A')<=ord(user[i])<ord('Z'):
    #         list_isLower.append(user[i])
    #     else:
    #         list.append(user[i])
    # if len(list)!=0 and len(list_isUpper)!=0 and len(list_isLower)!=0:
    #     print("GOOD PASSWORD")
    # else:
    #     print("The password needs to include capitalization and numbers, please re-enter")
    #     count+=1
    #     operator(count)
    if user.isupper()==False and user.islower()==False and user.isdecimal()==False:
        print("GOOD PASSWORD")
    else:
        print("The password needs to include capitalization and numbers, please re-enter")
        count+=1
        operator(count)
count = 2
operator(count)