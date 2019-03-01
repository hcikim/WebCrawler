from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv

def music_info(div):
	
	title_tag = div.find('div', {'class':'tracklist-name ellipsis-one-line'}).get_text()
	artist_tag = div.find('a', {'class':'tracklist-row__artist-name-link'}).get_text()
	
	return {
		"title": title_tag,
		"artist": artist_tag
	}

url = ['https://open.spotify.com/playlist/37i9dQZF1DX4pAtJteyweQ','https://open.spotify.com/playlist/37i9dQZF1DX3Z99viCDp7Q',
		'https://open.spotify.com/playlist/37i9dQZF1DWX3387IZmjNa','https://open.spotify.com/playlist/37i9dQZF1DX09mi3a4Zmox',
		'https://open.spotify.com/playlist/37i9dQZF1DX8WMG8VPSOJC','https://open.spotify.com/playlist/37i9dQZF1DX6mvEU1S6INL',
		'https://open.spotify.com/playlist/37i9dQZF1DWSlwBojgQEcN','https://open.spotify.com/playlist/37i9dQZF1DWWCKk94npRDB','https://open.spotify.com/playlist/37i9dQZF1DWUoGbRYcteyC',
		'https://open.spotify.com/playlist/37i9dQZF1DWVGy1YP1ojM5','https://open.spotify.com/playlist/37i9dQZF1DWSRc3WJklgBs',
		'https://open.spotify.com/playlist/37i9dQZF1DX4adj7PFEBwf','https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn',
		'https://open.spotify.com/playlist/37i9dQZF1DX0QKpU3cGsyb','https://open.spotify.com/playlist/37i9dQZF1DX7rOY2tZUw1k',
		'https://open.spotify.com/playlist/37i9dQZF1DX2Ma8k80RiMN','https://open.spotify.com/playlist/4QuJ2DbcTe7R8lzqfNXz7v',
		'https://open.spotify.com/playlist/3wI0prya1veVHKQOtLbmxB']

driver = webdriver.Chrome('/Users/tommy/chromedriver') #direct your chromedriver path here
driver.implicitly_wait(3)

result = []

for page in url:
	print("souping page: ", page, ",", len(result), "data have been crawled.")
	
	driver.get(page)
	sleep(3)

	html = driver.page_source.encode('utf-8')
	soup = BeautifulSoup(html, 'html.parser')
	blocks = soup.find_all('div', {'class': 'tracklist-col name'})
	
	for block in blocks:
		result.append(music_info(block))

keys = result[0].keys()

driver.quit()

with open('Most_Loved.csv', 'w', encoding="utf-8") as f: #store the data as a txt file.
    dict_writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(result)