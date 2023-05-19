import re,shutil,os

p=r'D:\王一通\后端\Python\代码\homework\arrange_dir'
for folderName, subfolders, filenames in os.walk(p):
    for filename in filenames:
        if re.compile('.*.txt').search(filename):
            shutil.move(p+'\\'+filename, p+'\\txt\\'+filename)
        elif re.compile('.*.mp3').search(filename):
            shutil.move(p + '\\' + filename, p + '\\mp3\\' + filename)
        elif re.compile('.*.jpg').search(filename):
            shutil.move(p + '\\' + filename, p + '\\jpg\\' + filename)