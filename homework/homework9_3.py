from pathlib import Path

helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\a.txt','r',encoding='utf-8')
list = []
sum = 0
for i in helloFile.readlines():
    i = i.strip('\n').split(' ')
    dict = {'name':i[0],'price':i[1],'amount':i[2]}
    list.append(dict)
print(list)
for i in list:
    sum += int(i['price'])*int(i['amount'])
print(sum)
helloFile.close()