import zipfile,os

def backupToZip(folder):
    # 将“文件夹”的全部内容备份为ZIP文件
    # 确保文件夹是绝对的
    folder = os.path.abspath(folder)    # 获取文件绝对路径

    # 找出该代码应该基于的文件名
    # 哪些文件已经存在
    number = 1
    while True:
        # os.path.basename()返回path最后的文件名
        zipFilename = os.path.basename(folder)+'_'+str(number)+".zip"
        # 检查文件是否存在
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create the zip file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # 遍历整个文件夹树并压缩每个文件夹中的文件
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # 将当前文件夹添加到ZIP文件中
        backupZip.write(foldername)
        # 将此文件夹中的所有文件添加到ZIP文件中
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            # startswith()用于检查字符串是否是以指定子字符串开头
            # endswith()用于检查字符串是否是以指定子字符串结尾
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('D:\王一通\后端\Python\代码\homework')