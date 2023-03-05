from bs4 import BeautifulSoup
import requests
from PIL import Image
import glob

URL = input("Give me a URL:") 
getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})

soup = BeautifulSoup(getURL.text, 'html.parser')

images = soup.find_all('img')

image_list = []
resized_images = []



resolvedURLs = []
 
for image in images:
    src = image.get('src')
    resolvedURLs.append(requests.compat.urljoin(URL, src))
    print(image)
 
for image in resolvedURLs:
    webs = requests.get(image)
    open('images/' + image.split('/')[-1], 'wb').write(webs.content)
    print(image)



for filename in glob.glob('images/*.jpg'):
    print(filename,"png")
    img = Image.open(filename)
    image_list.append(img)

for image in image_list:
    image = image.resize((600, 600))
    resized_images.append(image)

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format('resize/', i+1, '.jpg'))



for filename2 in glob.glob('images/*.png'):
    print(filename2,"png")
    img = Image.open(filename2)
    image_list.append(img)

for image in image_list:
    image = image.resize((600, 600))
    resized_images.append(image)

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format('resize/', i+1, '.png'))


for filename3 in glob.glob('images/*.gif'):
    print(filename3,"gif")
    img = Image.open(filename3)
    image_list.append(img)

for image in image_list:
    image = image.resize((600, 600))
    resized_images.append(image)

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format('resize/', i+1, '.gif'))

