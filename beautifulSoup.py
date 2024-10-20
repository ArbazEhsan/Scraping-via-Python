import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.poundwholesale.co.uk'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0; Microsoft Outlook 16.0.5450; ms-office; MSOffice 16)'
}


r = requests.get(baseurl+'/wholesale-cleaning', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find_all('div', class_='products wrapper grid products-grid')

# print(r.content)
if r.status_code == 200:
    # print("Request was successful")
    print(productlist)

else:
    print(f"Failed to retrieve content: {r.status_code}")

