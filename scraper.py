from bs4 import BeautifulSoup
import requests
# import csv 

def scrape(keyword):
	result = []
	source = requests.get(f'https://www.youtube.com/results?search_query={keyword}').text
	# with open('simple.html') as html_file:

	# soup = BeautifulSoup(html_file, 'lxml')
	soup = BeautifulSoup(source, 'lxml')


	# csv_file = open('cms_scrape.csv', 'w')
	# csv_writer = csv.writer(csv_file)
	# csv_writer.writerow(['headline', 'summary', 'video_link'])

	for yt_video in soup.find_all('a', class_ = 'yt-uix-tile-link'):
		# print(article.prettify())

		try:
			vid_src = yt_video['href']
			# print(vid_src)

			# yt_link = f'https://youtube.com{vid_src}'
			yt_video_id = vid_src.split('=')[1]
			
		except Exception as e:
			yt_link = None

		result.append(yt_video_id)
		if len(result) == 4:
			break

	return result


	# print(yt_link)

# 	csv_writer.writerow([headline, summary, yt_link])

# csv_file.close()

# print(soup.prettify())
# .find  will only find the first result

# for article in soup.find_all('div', class_='article'):
# # print(article)

# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.p.text
# 	print(summary)

# 	print()