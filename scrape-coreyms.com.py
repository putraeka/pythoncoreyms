import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://coreyms.com/'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}
source = requests.get(URL, headers=headers)

soup = BeautifulSoup(source.content, 'lxml')

csv_file = open('coreyms-blog.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    # print(article.prettify())

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').text
    print(summary.strip())

    try:
        video_url = article.find('iframe', class_='youtube-player')['src']
        video_id = video_url.split('/')[4]
        video_id = video_id.split('?')[0]
        yt_link = f'https://www.youtube.com/watch?v={video_id}'
    except Exception as e:
        yt_link = None
    
    print(yt_link)
    
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()