from PIL import Image
import pathlib, requests

ROOT_FOLDER = pathlib.Path(__file__).parent
IMG_FOLDER = ROOT_FOLDER / 'Web_Server' / 'imagens' / 'proz_icon.png'


response = requests.get('https://is1-ssl.mzstatic.com/image/thumb/Purple126/v4/e0/39/a7/e039a74a-b3da-c12e-b761-f648ffe56932/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg')


if response.status_code in range(200, 300):
    bytes_img = response.content
    with open(IMG_FOLDER, 'wb') as img_file:
        img_file.write(bytes_img)
else:
    print(response.reason)


fd_image = Image.open(IMG_FOLDER)
width, height = fd_image.size

new_height = 200
new_width = round((width * new_height) / height)

fd_image.resize((new_width, new_height))

fd_image.save(IMG_FOLDER, optimize=True, quality=70)