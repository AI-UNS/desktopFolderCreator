import os
import shutil

current_directory = os.getcwd()
folder_order = current_directory.split('\\')

print(current_directory)
print(folder_order)
print(len(folder_order))

desktop_path = ''

for path in folder_order:
    desktop_path += path + '/'
    if path == 'Desktop':
        break

path_doc = 'DOC_container'
path_img = 'IMG_container'
path_music = 'MP4_container'

folder_container = [path_doc, path_img, path_music]
folder_place = []

for folder_path in folder_container:
    new_way = desktop_path + folder_path
    folder_place.append(new_way)


try:
    for direct in folder_place:
        os.mkdir(direct)
except FileExistsError:
    print('this folder already exists')

while True:
    dir_list = os.listdir(desktop_path)
    for key in dir_list:
        if 'jpg' in key or 'png' in key:
            shutil.move(desktop_path + key, folder_place[1])
        elif 'doc' in key or 'docx' in key:
            shutil.move(desktop_path + key, folder_place[0])
        elif 'mp4' in key:
            shutil.move(desktop_path + key, folder_place[2])
