
"""
Це основний файл де викликаються функції які описані у файлі get_mars_photo.py
і потім це фото завантажується на сервер
"""
from get_mars_photo import get_img_url, download_img
from git.hillel_python.homework_19.api_ctrl import PhotoCtrl

api_ctrl = PhotoCtrl()

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'piUbc4uHYSc04vy6XbEwPhW4dKCg7GAvIK5ToRRn'}


file_path = download_img(get_img_url(url, params))

files = {'image': open(file_path, 'rb')}

def upld_photo(files):
    if not files:
        return 'No file for sending'
    else:
        response = api_ctrl.upload_photo(files)
        return response

def show_photo(file_path):
    response = api_ctrl.get_photo(file_path)
    return response

def del_photo(file_path):
    response = api_ctrl.delete_photo(file_path)
    return response

print(del_photo(file_path))

