def user():
    str = '$sd1#111$svda123!!!221&eSSDSyyyyyyDG^svda121^svda124^1111111111111'
    result = ''
    for i in range(0,len(str),1):
        if str[i].isalnum():
            result+=str[i]
            if i!=len(str)-1 and str[i+1].isalnum() != True:
                result = ''
            elif i==len(str)-1 and str[i].isalnum() != True:
                result += str[i]
    print(result)
user()