import shutil
import os

path = '/home/sasha/.local/share/Trash/files/'
pathWork = '/home/sasha/work/Tatyana_Ystinova/'
big_files = []
very_big_files = []
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
            except:
                print('no')
        # if len(str(ls)) > 7:
        #     ls = round(ls / gb, 2)
        #     result = str(ls) + 'GB'
        #     try:
        #         very_big_files.append(result)
        #     except:
        #         pass
        else:
            ls = ls // 1024
            result = str(ls) + 'K'
        print(result, i)
    except:
        pass
print(big_files)
print(very_big_files)