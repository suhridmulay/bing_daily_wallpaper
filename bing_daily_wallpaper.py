import bs4
import requests
import datetime

#src_url is the url of the bing homepage
src_url = 'https://www.bing.com'
r = requests.get(src_url)

soup = bs4.BeautifulSoup(r.text, 'html.parser')

#image url is extracted from the bing webpage.
#the url is in a link element
img_url = soup.link['href']

#final url of the image
final_url = src_url + img_url
image = requests.get(final_url)

date_str = str(datetime.date.today())
filename = 'wallpaper_' + date_str + '.jpg'

wallpaper = open(filename, 'wb')
wallpaper.write(image.content)
wallpaper.close()


