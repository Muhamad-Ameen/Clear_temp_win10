import os

path1 = "C:\\Windows\\Temp\\"
path2 = "C:\\Users\\mhama\\AppData\\Local\\Temp\\"
path3 = "C:\\Windows\\prefetch\\"

print("#"*50)
for i in os.listdir(path1):
    try:
        os.remove(path1+i)
        print(i + " \033[32;1m:- File removed\033[0m")
    except:
        print(i + " \033[31;1m:- Permission Denied\033[0m")
print("#"*50)
for i in os.listdir(path2):
    try:
        os.remove(path2+i)
        print(i + " \033[32;1m:- File removed\033[0m")
    except:
        print(i + " \033[31;1m:- Permission Denied\033[0m")
print("#"*50)
for i in os.listdir(path3):
    try:
        os.remove(path3+i)
        print(i + " \033[32;1m:- File removed\033[0m")
    except:
        print(i + " \033[31;1m:- Permission Denied\033[0m")

input("")
