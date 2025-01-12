import requests


class PhotoCtrl:
    def __init__(self, url='http://127.0.0.1:8080/'):
        self.url = url

    def upload_photo(self, files):
        return requests.post(url=f'{self.url}upload',files=files).json()


    def get_photo(self, file_path):
        headers = {'Content-Type': 'text'}
        return requests.get(url=f'{self.url}/image/{file_path}',headers=headers).json()


    def delete_photo(self, file_path):
        return requests.delete(url=f'{self.url}/delete/{file_path}').status_code