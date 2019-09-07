from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# print(html.html) # untuk menampilkan halaman html di standard ouput

# print (html.text) # Hanya menampilkan text saja (tapi juga menampilkan javascript)

match = html.find('title') # cari html dengan selector title
print(match[0].text) # print text dari index pertama dari variable match

match = html.find('title', first=True) # menampilkan hanya isi pertama dari id 'title'
print(match.text) # karena sudah didefinisikan dari awal tidak perlu lagi menggunakan [0]

article = html.find('div.article', first=True) # menampilkan semua element dari 'div.article'
print(article.text)

headline = article.find('h2', first=True).text
summary = article.find('p', first=True).text

print(headline)
print(summary)