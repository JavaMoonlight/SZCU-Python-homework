from pathlib import Path

#（1）将源文件全部读出来并打印
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\a1.txt',encoding='utf-8')
helloRead = helloFile.read()
print(helloRead)
helloFile.close()

#（2）在源文件后面追加一行内容:信不信由你,反正我信了.
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\a1.txt','a',encoding='utf-8')
helloWrite = helloFile.write("\n信不信由你,反正我信了.")
helloFile.close()

#（3）将源文件全部读出来,并在后面添加一行内容:信不信由你,反正我信了.
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\a1.txt','r+',encoding='utf-8')
helloRead = helloFile.read()
print(helloRead)
helloWrite = helloFile.write("\n信不信由你,反正我信了.")
helloFile.close()

# （4）将源文件全部清空,换成下面内容:
helloFile = open('D:\\王一通\\后端\\Python\\代码\\homework\\a1.txt','w',encoding='utf-8')
helloWrite = helloFile.write("每天坚持一点,\n每天努力一点,\n每天多思考一点,\n慢慢你会发现\n你的进步越来越大.")
helloFile.close()