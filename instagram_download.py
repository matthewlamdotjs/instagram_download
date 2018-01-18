# Download an instagram image from its page's URL

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver

test_url = "https://www.instagram.com/p/BeD9Q3dBqxh/"
# Expected IMG URL: https://instagram.fhnl1-1.fna.fbcdn.net/vp/4fc78cfe764903511383fda746e7ab4c/5AD8568B/t51.2885-15/e35/26153078_978109285660175_3609259442022907904_n.jpg
# div class _4rbun

browser = webdriver.Chrome()
browser.get(test_url)
innerHTML = browser.execute_script("return document.body.innerHTML")
soup = BeautifulSoup(innerHTML, 'html.parser')
img = soup.find("div",{"class":"_4rbun"}).find("img")['src']

browser.close()

file = urllib2.urlopen(img).read()
fileName = img.split('/')[-1]
output = open(fileName,'wb')
output.write(file)
output.close()
