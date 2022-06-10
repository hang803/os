import os,time

path = '/home//user/Documnets.11'
print(os.path.normpath(path))
print(os.path.basename(os.path.normpath(path)))

for parent,dirs,files in os.walk('D:/bbbbb'):
    print(parent,dirs,files)
