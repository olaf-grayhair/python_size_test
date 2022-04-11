import os, shutil

path = '/home/sasha/work/Oboi-raznoe-08.04.2022/'
new_path = '/home/sasha/work/images/'
mb = 1024 ** 2
size_img = []


for i in os.listdir(path):
    ls = os.path.getsize(path + i)
    result = round(ls / mb, 2)
    size_img.append(result)
    for file in range(0,17):
        if int(round(result)) == file:
            try:
                os.makedirs(f'{new_path}files_{file}_mb')
            except:
                pass
            try:
                shutil.copy(path + i, f'{new_path}files_{file}_mb/')
                print(path + i, f'{new_path}files_{file}_mb/')
            except:
                pass
size_img.sort()
print(size_img)