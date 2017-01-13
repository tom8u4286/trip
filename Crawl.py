from bs4 import BeautifulSoup
#import urllib, unicodedata
import re
import time
#import sqlite3
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait

def remove_ads():
    print "OK"

    try:
        driver.find_element_by_class_name("moreLink").click()
        print "click more 1"
    except:
        pass
    try:
        driver.find_element_by_class_name("ui_close_x").click()
        print "ad closed"
    except:
        pass
    try:
        driver.find_element_by_class_name("moreLink").click()
        print "click more 2"
    except:
        pass

def pause():
    time.sleep(7)


text = []
url = "https://www.tripadvisor.com/Attraction_Review-g293913-d321216-Reviews-or10-National_Palace_Museum-Taipei.html"
urls = []
for i in range(1,25):
    urls.append(re.sub(r"-or\d+0-", "-or"+str(i)+"0-",url))

#urls = urls[:2]
#print urls
driver = webdriver.Chrome()

for url in urls:
    print "crawling "+url
    driver.get(url)
    pause()
    remove_ads()
    pause()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for div in soup.findAll("div",{ "class" : "dyn_full_review" }):

        data = []
        #print type(div.find("div",{"class": "entry"}).find("p").getText().strip("\n"))
        #print type(str(div.find("div",{"class": "entry"}).find("p").getText().strip("\n")))
        #print str(div.find("div",{"class": "entry"}).find("p").getText().strip("\n"))
        text.append( div.find("div",{"class": "entry"}).find("p").getText().strip("\n"))
        #data.append( un( div.find("div",{"class": "rating"}).find("img")["alt"][0],"utf-8"))
        #text.append(data)


f = open("data.txt","w+")
f.write(u"\n".join(text).encode('utf8'))

#conn = sqlite3.connect('mydb.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE review
#            (review, ratings)''')
#conn.commit()
#for item in text:
#    c.execute('insert into tablename values (?,?)', item)
#
#conn.commit()
#conn.close()

