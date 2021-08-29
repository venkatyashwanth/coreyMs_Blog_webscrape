from bs4 import BeautifulSoup 
import requests
import csv 


source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source,'lxml')


csv_file = open('cms_scrape.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])




# article = soup.find('article')
for article in soup.find_all('article'): 
	headline = article.h2.a.text 
	summary_cont = article.find('div',class_="entry-content")
	summary = summary_cont.p.text
	
	try: 
		vid_src = article.find('iframe',class_="youtube-player")['src']
		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]
		yt_link = ("https://youtube.com/watch?v={}".format(vid_id))
	except Exception as e: 
		yt_link= None 


	print(headline)
	print(summary)
	print(yt_link)
	print('')
	csv_writer.writerow([headline,summary,yt_link])


csv_file.close()


#VideoDescription: https://www.youtube.com/watch?v=ng2o98k983k&t=1678s

