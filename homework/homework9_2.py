from pathlib import Path

#（1）以r的模式打开源文件,利用for循环遍历文件句柄
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\t1.txt','r',encoding='utf-8')
for i in helloFile:
    print(i.strip())
helloFile.close()

#（2）以r的模式打开源文件,以readlines()方法读出来,并循环遍历readlines()
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\t1.txt','r',encoding='utf-8')
helloRead = helloFile.readlines()
for i in range(0,len(helloRead)):
    #将列表各项中的'\n'打印出来，使用了repr函数
    print(repr(helloRead[i]))
helloFile.close()

#（3）以r模式读取文件的前四个字符
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\t1.txt','r',encoding='utf-8')
helloRead = helloFile.read(4)
print(helloRead)
helloFile.close()

#（4）以r模式读取第一行内容,并除去此行前后的空格、制表符、换行符
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\t1.txt','r',encoding='utf-8')
helloRead = helloFile.readline().strip()
print(helloRead)
helloFile.close()

#（5）以a+模式打开文件，先追加一行:'老男孩教育'然后在从最开始将原内容全部读取出来
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\t1.txt','a+',encoding='utf-8')
# seek() 方法用于移动文件读取指针到指定位置
helloFile.seek(0)
helloRead = helloFile.read()
helloWrite = helloFile.write("\n老男孩教育")
print(helloRead)
helloFile.close()