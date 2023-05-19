import shutil,zipfile

shutil.move('D:\王一通\后端\Python\代码\homework\DRL.png','D:\王一通\后端\Python\代码\homework\WYT_5_19.png')
fileZip = zipfile.ZipFile('D:\王一通\后端\Python\代码\homework\WYT_5_19.zip','w')
fileZip.write('D:\王一通\后端\Python\代码\homework\WYT_5_19.png',compress_type=zipfile.ZIP_DEFLATED)
fileZip.close()
