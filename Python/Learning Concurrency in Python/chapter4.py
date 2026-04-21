from urllib.request import Request, urlopen, urljoin, URLError
from urllib.parse import urlparse
import ssl
from bs4 import BeautifulSoup

import threading
import queue

class Crawler:
    base_url = ""
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    errorLinks = set()

    def __init__(self, base_url):
        Crawler.base_url = base_url

    @staticmethod
    def crawl(thread_name, url, linksToCrawl):
        try:
            link = urljoin(Crawler.base_url, url)
            if (urlparse(link).netloc == "tutorialedge.net") and (
                link not in Crawler.crawledLinks
            ):
                request = Request(link, headers={"User-Agent": "Mozilla/5.0"})
                response = urlopen(request, context=Crawler.myssl)
                Crawler.crawledLinks.add(link)
                print(
                    f"Url {response.geturl()} crawled with status: {response.getcode()}: {len(Crawler.crawledLinks)} crawled with total."
                )
                soup = BeautifulSoup(response.read(), "html.parser")
                Crawler.enqueueLinks(soup.find_all("a", linksToCrawl))
        except URLError as e:
            print(f"URL {link} threw this error when trying to parse: {e.reason} ")
            Crawler.errorLinks.add(link)

    @staticmethod
    def enqueueLinks(links, linksToCrawl):
        for link in links:
            if (urljoin(Crawler.base_url, link.get("href")) not in Crawler.crawledLinks):
                if (urljoin(Crawler.base_url, link.get("href")) not in linksToCrawl):
                    linksToCrawl.put(link.get("href"))

class CheckableQueue(queue.Queue):
    def __contains__(self, item):
        with self.mutex:
            return item in self.queue
        
    def __len__(self):
        return len(self.queue)



THREAD_COUNT = 20
linksToCrawl = CheckableQueue()   

def createCrawlers():
    for i in range(THREAD_COUNT):
        t= threading.Thread(target=run)
        t.daemon = True
        t.start()

def run():
    while True:
        url = linksToCrawl.get()
        try:
            if url is None:
                break
            Crawler.crawl(threading.current_thread(),url,linksToCrawl)
        except:
            print("Exception")
        linksToCrawl.task_done()

def main():
    url = input("Website > ")
    Crawler(url)
    linksToCrawl.put(url)
    createCrawlers()
    linksToCrawl.join()
    print(f"Total Links Crawled: {len(Crawler.crawledLinks)}")
    print(f"Total Errors: {len(Crawler.errorLinks)}")


if "__main__":
    main()
