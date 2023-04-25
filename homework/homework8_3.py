import re
data = {
    '零'.encode('utf-8').decode('utf-8'):'0',
    '一'.encode('utf-8').decode('utf-8'):'1',
    '二'.encode('utf-8').decode('utf-8'):'2',
    '三'.encode('utf-8').decode('utf-8'):'3',
    '四'.encode('utf-8').decode('utf-8'):'4',
    '五'.encode('utf-8').decode('utf-8'):'5',
    '六'.encode('utf-8').decode('utf-8'):'6',
    '七'.encode('utf-8').decode('utf-8'):'7',
    '八'.encode('utf-8').decode('utf-8'):'8',
    '九'.encode('utf-8').decode('utf-8'):'9',
    '年'.encode('utf-8').decode('utf-8'):'年'
}
word = re.compile("[\u96f6|\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d]+\u5e74")
num = word.findall('一九四九年')
result = ''
for i in num:
    for j in i:
        result += data[j]
print(result)