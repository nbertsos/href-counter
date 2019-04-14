#Import urllib and BS
import urllib.request #import urlopen
from bs4 import BeautifulSoup
import ssl
import re
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Set inputs
url = input('Enter URL - ')

count = input('Enter count - ')
count = int(count)

position = input('Enter position - ')
position = int(position)
print("Retrieving:", url)
#print(range(count))
#counting loop
for num in range(count) :
    print(num)

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tags = tags.get('href', None)
    print(tags)
