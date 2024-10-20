import requests
import json
import pandas as pd
from datetime import datetime

base_url = "https://www.leeswholesalebeauty.com"
website_name = 'leeswholesalebeauty';
product_list = []
y = 3

if y==1:
	for i in range(1,101):
		url = base_url + "/products.json?limit=250&page="+str(i)

		r = requests.get(url)
		data = r.json()

		if len(data['products'])<=0:
			print("Page End:"+ str(i))
			break

if y==2:
	for i in range(1,101):
		url = base_url + "/products.json?limit=250&page="+str(i)

		now = datetime.now()
		print("Scraping Started: "+str(url)+" | Timestamp: "+str(now))

		r = requests.get(url)
		data = r.json()

		if len(data['products'])<=0:
			print("Page End:"+ str(i))
			break
		else:
			# print(len(data['products']))
			# print(data['products'][0]['title'])

			for item in data['products']:
				title = item['title']
				handle = item['handle']
				created = item['created_at']
				product_type = item['product_type']
				vendor = item['vendor']

				for image in item['images']:
					try:
						image_src = image['src']
					except:
						image_src = 'None'

				url2 = base_url + "/products/"+ handle +".json"
				r2 = requests.get(url2)
				data2 = r2.json()

				for variant in data2['product']['variants']:
					price = variant['price']
					sku = variant['sku']
					barcode = variant['barcode']

					product = {
						'title': title,
						'created_at': created,
						'product_type': product_type,
						'image': image_src,
						'price': price,
						'sku': sku,
						'barcode': barcode,
					}
					product_list.append(product)
					print("Product ID: "+str(sku)+" | Timestamp: "+str(datetime.now()))


if y==3:
	for i in range(1,101):
		url = base_url + "/products.json?limit=250&page="+str(i)

		now = datetime.now()
		print("Scraping Started: "+str(url)+" | Timestamp: "+str(now))

		r = requests.get(url)
		data = r.json()

		if len(data['products'])<=0:
			print("Page End:"+ str(i))
			break
		else:
			for item in data['products']:
				title = item['title']
				handle = item['handle']
				created = item['created_at']
				product_type = item['product_type']
				vendor = item['vendor']

				for image in item['images']:
					try:
						image_src = image['src']
					except:
						image_src = 'None'

				for variant in item['variants']:
					price = variant['price']
					sku = variant['sku']

					product = {
						'title': title,
						'created_at': created,
						'product_type': product_type,
						'image': image_src,
						'price': price,
						'sku': sku,
					}
					product_list.append(product)
					print("Product ID: "+str(sku)+" | Timestamp: "+str(datetime.now()))		


df = pd.DataFrame(product_list)
df.to_csv('ProductSheets/Product-Sheet'+'-'+website_name+'.csv')
print('saved to file.')