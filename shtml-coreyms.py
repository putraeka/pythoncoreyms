from requests_html import HTML,HTMLSession

session = HTMLSession()

r = session.get('https://coreyms.com')

article = r.html.find('article', first=True) # cari element dengan class article
headline = article.find('.entry-title-link', first=True).text
print(headline)
summary = article.find('.entry-content p', first=True).text # cari element dengan class entry-content yang ada p
print(summary)

vid_src = article.find('iframe', first=True).attrs['src']
# print(vid_src.attrs['src'])
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
vid_id = f'https://youtube.com/watch?={vid_id}'
print(vid_id)

# Untuk menampilkan semua class article
articles = r.html.find('article') # cari element dengan class article
for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print(headline)
    summary = article.find('.entry-content p', first=True).text # cari element dengan class entry-content yang ada p
    print(summary)
    
    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        # print(vid_src.attrs['src'])
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        ytlink = f'https://youtube.com/watch?={vid_id}'
    except:
        ytlink = None
    print(ytlink)
    print()

# Menampilkan link dari sebuah web
for link in r.html.links:
    print(link)