from bs4 import BeautifulSoup
import urllib.request
import database
import notification
import time

url = 'http://slickdeals.net/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")

main_content = soup.find('div', id='mainColumn')\
    .find('div', id="fpMainContent")\
    .find('div', attrs={"class": "gridCategory removeHidden", "data-blockname": "best"})



products = main_content.find_all('div', 'fpGridBox grid  frontpage firedeal')

for product in products:
    print(product.find('img')['title'])



print(len(products))

existed_items = []

while 1:
    # if the program is runned the first time, add all deals to database without any notification
    if database.check_empty():
        for product in products:
            database.insert(product.find('img')['title'])
    else:
        for product in products:
            firedeal = product.find('img')['title']
            if not database.find(firedeal):
                notification.balloon_tip("Slickdeal Firedeal", firedeal)
                database.insert(firedeal)

    time.sleep(300)
