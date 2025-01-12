import requests

"В цьому файлі я написав функції які отримують та завантажують фотографію з марса"

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'piUbc4uHYSc04vy6XbEwPhW4dKCg7GAvIK5ToRRn'}


def get_img_url(url, params):

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Request failed with status code {response.status_code}"

    photos = response.json().get('photos', [])
    if not photos:
        return "No photos found for these parameters"

    return photos[0]['img_src']

def download_img(url):

    response = requests.get(url)
    img_name = 'image_from_response.jpg'

    if response.status_code != 200:
        return f"Failed to download image. Status code: {response.status_code}"

    with open(img_name, 'wb') as file:
        file.write(response.content)

    return img_name
