import requests
from bs4 import BeautifulSoup
import csv
import os


URL ='https://auto.ria.com/newauto/marka-bmw/'
FILE = 'cars.csv'
HEADERS={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36', 'accept':'*/*'}

HOST ='https://auto.ria.com'
def get_html(url, params =None):
	r=requests.get(url,headers=HEADERS, params=params)
	return r

def get_pages_count(html):
	soup=BeautifulSoup(html, 'html.parser')
	pagination = soup.find_all('span', class_="mhide")
	if pagination:
		return int(pagination[-1].get_text())
	else:
		return 1
def save_file(items, path):
	with open(path, 'w', newline='') as file:
		writer = csv.writer(file, delimiter=';')
		writer.writerow(['Марка', 'Ссылка','Цена USD','Цена UAH','Город'])
		for item in items:
			writer.writerow([item['title'], item['link'], item['usd_price'], item['uah_price'],item['place']])
def get_contetnt(html):
	soup=BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div' , class_="proposition_area")

	cars=[]
	for item in items:
		uah_price =item.find('span', class_="grey size13")
		if uah_price:
			uah_price=uah_price.get_text(strip=True)
		else:
			uah_price="Цену уточняйте"
		cars.append({
			'title': item.find('h3', class_="proposition_name").get_text(strip=True),
			'link': HOST+item.find('a').get('href'),
			'usd_price': item.find('span', class_="green").get_text(strip=True),
			'uah_price': uah_price,
			'place': item.find('svg', class_="svg-i16_pin").find_next('strong').get_text(strip=True),

		})
	return(cars)

def parse():
	URL = input("Введите URL: ")
	URL=URL.strip()
	html = get_html(URL)
	if html.status_code ==200:
		cars=[]
		pages_count = get_pages_count(html.text)

		for page in range(1,pages_count+1):
			print(f'Парсинг страницы {page} из {pages_count}...')
			html=get_html(URL, params={'page': page})
			cars.extend(get_contetnt(html.text))
		save_file(cars, FILE)
		print(f'Получено {len(cars)} автомобилей')
		os.startfile(FILE)
	else:
		print("Error")
parse()
