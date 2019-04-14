#Import urllib and BS
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Set inputs
url = input('Enter URL - ')

count = input('Enter count - ')
count = int(count)

position = input('Enter position - ')
position = int(position)

#print(range(count))
#counting loop
for num in range(count + 1) :
    print(num)
    print('Retrieving:', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        link = tag.get()
        print(link[position - 1])
