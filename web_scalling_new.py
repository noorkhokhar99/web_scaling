from bs4 import BeautifulSoup
import requests

URL = "https://www.newegg.com/black-corsair-4000d-airflow-atx-mid-tower/p/N82E16811139156?Item=N82E16811139156" # Replace this with the website's URL
URL1 = "https://www.bhphotovideo.com/c/browse/Computers-Solutions/ci/9581" # Replace this with the website's URL
URL2 = "https://www.newegg.com/Computer-Systems/Store/ID-3" # Replace this with the website's URL
URL3 = "https://www.amazon.ae/s?i=computers&rh=n%3A11497745031%2Cn%3A11497746031%2Cn%3A12050245031&s=popularity-rank&pd_rd_r=5743a1f0-daa1-4a7f-8fbb-8d4d0850e29a&pd_rd_w=Ie4ke&pd_rd_wg=KJyhh&pf_rd_p=d374c4bf-a1d8-4455-b894-b69c47c4281a&pf_rd_r=AAD0ME31JF5ADW8GZRX2&ref=pd_gw_unk" # Replace this with the website's URL


getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
getURL1 = requests.get(URL1, headers={"User-Agent":"Mozilla/5.0"})
getURL2 = requests.get(URL2, headers={"User-Agent":"Mozilla/5.0"})
getURL3 = requests.get(URL3, headers={"User-Agent":"Mozilla/5.0"})



soup = BeautifulSoup(getURL.text, 'html.parser')
soup1 = BeautifulSoup(getURL1.text, 'html.parser')
soup2 = BeautifulSoup(getURL2.text, 'html.parser')
soup3 = BeautifulSoup(getURL3.text, 'html.parser')


 
images = soup.find_all('img')
images1 = soup1.find_all('img')
images2 = soup2.find_all('img')
images3 = soup3.find_all('img')


resolvedURLs = []
resolvedURLs1 = []
resolvedURLs2 = []
resolvedURLs3 = []


 
for image in images:
    src = image.get('src')
    resolvedURLs.append(requests.compat.urljoin(URL, src))
    print(image)
 
for image in resolvedURLs:
    webs = requests.get(image)
    open('images/' + image.split('/')[-1], 'wb').write(webs.content)
    print(image)

for image1 in images1:
    src = image1.get('src')
    resolvedURLs1.append(requests.compat.urljoin(URL1, src))
 
for image1 in resolvedURLs1:
    webs = requests.get(image1)
    open('images/' + image1.split('/')[-1], 'wb').write(webs.content)
    print(image1)






for image2 in images2:
    src = image2.get('src')
    resolvedURLs2.append(requests.compat.urljoin(URL2, src))
 
for image2 in resolvedURLs2:
    webs = requests.get(image2)
    open('images/' + image2.split('/')[-1], 'wb').write(webs.content)








for image3 in images3:
    src = image3.get('src')
    resolvedURLs3.append(requests.compat.urljoin(URL3, src))
 
for image3 in resolvedURLs3:
    webs = requests.get(image3)
    open('images/' + image3.split('/')[-1], 'wb').write(webs.content)
    print(image3)
