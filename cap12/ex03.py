# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count:'))
position = int(input('Enter position:'))

for c in range(0,count+1):
  print("Retrieving:", url)
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  url = tags[position-1].get('href',None)