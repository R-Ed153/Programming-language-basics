import os
from dotenv import load_dotenv,find_dotenv
import requests
import time
import threading

load_dotenv(find_dotenv())

PEXEL_API_KEY = os.getenv("PEXEL_API_KEY")
image_url = "https://api.pexels.com/v1/"
image_folder = "Chapter1/temp/concurrent"
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",}


def saveImagesConcurrent(query, per_page=15):
    headers = {"Authorization": PEXEL_API_KEY}
    params = {"query": query, "per_page": per_page}
    response = requests.get(f"{image_url}search",headers=headers, params = params )
    if response.status_code == 200:
        data = response.json()
        threads = []
        for i,photo in enumerate(data['photos']):
            thread = threading.Thread(target=downloadImage,args=[photo,i])
            threads.append(thread)
            thread.start()
        for i in threads:
            i.join()        
    else:
        print('Error:',response.status_code)

def downloadImage(photo,index):
    url = photo['src']['original']
    print(url)        
    response = requests.get(url)
    if response.status_code == 200:
        filepath = f"{image_folder}/image-{index+1}.jpg"
        with open(filepath,"wb") as f:
            f.write(response.content)
            print(f"Saved: {filepath}")
    else:
        print(F"Error downloading image {index + 1}",response.stat)


def main():
    t0 = time.time()
    saveImagesConcurrent("Nature",10)
    t1 = time.time()
    totalTime = t1- t0
    print(f"Total Execution Time: {totalTime}")

if __name__ == "__main__":
    main()