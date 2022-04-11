import shutil
import os

path = '/home/sasha/.local/share/Trash/files/'
pathWork = '/home/sasha/work/Tatyana_Ystinova/'
big_files = []
path_this = []
result = ''
mb = 1024 ** 2
gb = 1024 ** 3

for i in os.listdir(path):
    try:
        ls = os.path.getsize(path + i)
        if len(str(ls)) > 6:
            ls = round(ls / mb, 2)
            result = str(ls) + 'M'
            try:
                big_files.append(result)
                path_this.append(path + i)
                # with open('result.txt', 'a') as f:
                #     f.write(f"{result} {path + i}\n")
            except:
                print('no')
        else:
            ls = ls // 1024
            result = str(ls) + 'K'
        print(result, i)
        with open('new.txt', 'a') as f:
            f.write(f"{result} {path + i}\n")
    except:
        pass
print(big_files)
print(path_this)

