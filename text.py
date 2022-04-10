import os

def new():
    input_name = input('enter name here: ')
    input_text = input('enter text here: ')
    with open(input_name + '.txt', 'w') as f:
        f.write(input_text)


def rem():
    catalog = os.listdir('/home/sasha/PycharmProjects/text_editor')
    file_name = input('enter file name: ')
    for num,item in enumerate(catalog):
        f = file_name + '.txt'
        try:
            if f == item:
                delete_file = input(f'delete file {f} ? print y for delete or n for cancel: ')
                if delete_file == 'y':
                    os.remove(f)
                    print(f'file {f} was deleted')
                    break
        except:
            print(f'file {f} does not exist')

def add_text():
    name = input('write name of file: ')
    try:
        with open(f'{name}.txt', 'a') as f:
            f.write(input('add text here: '))
    except:
        print('file not exist')

rem()