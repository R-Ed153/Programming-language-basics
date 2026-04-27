import urllib.request
import os
from pathlib import Path
from dotenv import load_dotenv,find_dotenv 

load_dotenv(find_dotenv())

PEXEL_API_KEY = os.getenv("PEXEL_API_KEY")


def downloadImage(imagePath, fileName):
    print("Downloading Image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)

def main():
    for i in range(10):
        imageName = f"temp/image-{i}.jpg"
        downloadImage("https://pexels.com",imageName)

if __name__ == "__main__":
    #main() 
    print(PEXEL_API_KEY)
