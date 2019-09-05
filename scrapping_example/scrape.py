from bs4 import BeautifulSoup
import requests
import csv 


source = requests.get('http://coreyms.com').text
# with open('simple.html') as html_file:

# soup = BeautifulSoup(html_file, 'lxml')
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
	# print(article.prettify())

	headline = article.a.text
	summary = article.find('div', class_='entry-content').p.text
	# print(summary)

	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']
		# print(vid_src)

		vid_id = vid_src.split('/')[4].split('?')[0]
		# print(vid_id)

		yt_link = f'https://youtube.com/watch?v={vid_id}'
		
	except Exception as e:
		yt_link = None

	print(yt_link)
	print()

	csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

# print(soup.prettify())
# .find  will only find the first result

# for article in soup.find_all('div', class_='article'):
# # print(article)

# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.p.text
# 	print(summary)

# 	print()