import os
path = "./" #文件夹目录
def readDir(dirPath):
    
    allFiles = []
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            f = dirPath+'/'+f
            if os.path.isdir(f):
                subFiles = readDir(f)
                allFiles = subFiles + allFiles #合并当前目录与子目录的所有文件路径
            else:
                if f.split('.')[-1]=="md":
                    allFiles.append(f)
        return allFiles
    else:
        return 'Error,not a dir'
files=readDir(path)
print(files)
weight=0
for fi in files:
    weight+=1
    print(fi.split('/')[-1][:-3])
    with open(fi,'r',encoding='utf-8') as f:
        lines = f.readlines()
    with open(fi,'w',encoding='utf-8') as file:
        file.write("---\n")
        file.write('title: "'+fi.split('/')[-1][:-3]+'"\n')
        file.write("date: 2021-04-14T02:23:00+08:00\n")
        file.write("draft: false\n")
        file.write("weight: "+ str(weight)+"\n")
        file.write("---\n")
        file.writelines(lines)
        file.close()
