import os
import shutil

path1, path2, path3 = "C:\\Windows\\Temp\\", "C:\\Users\\mhama\\AppData\\Local\\Temp\\", "C:\\Windows\\prefetch\\"
successes, fail = " \033[32;1m:- File removed\033[0m", "\033[31;1m:- Permission Denied\033[0m"


def cls(paths):
    if len(os.listdir(paths)) == 0:
        print("empty folder")
    for i in os.listdir(paths):
        try:
            shutil.rmtree(paths + i)
            print(i + successes)
        except:
            print(i + fail)


print("#" * 50 + "TEMP")
cls(path1)
print("#" * 50 + "%TEMP%")
cls(path2)
print("#" * 50 + "PREFETCH")
cls(path3)
