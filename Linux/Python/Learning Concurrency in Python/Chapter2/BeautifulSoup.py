import urllib.request
import time
from bs4 import BeautifulSoup

t0 = time.time()
req= urllib.request.urlopen("https://www.example.com")
t1 = time.time()
print(f"Total Time To Fetch Page: {t1 - t0} Seconds")
soup = BeautifulSoup(req.read(),"html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
t2 = time.time()
print(f"Total Execution Time: {t2-t0} Seconds")