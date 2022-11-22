from bs4 import BeautifulSoup
import requests

URL = "https://www.newegg.com/Components-Storage/Store/ID-1" # Replace this with the website's URL
getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(getURL.text, 'html.parser')
 
images = soup.find_all('img')
resolvedURLs = []
 
for image in images:
    src = image.get('src')
    resolvedURLs.append(requests.compat.urljoin(URL, src))
 
for image in resolvedURLs:
    webs = requests.get(image)
    open('images/' + image.split('/')[-1], 'wb').write(webs.content)