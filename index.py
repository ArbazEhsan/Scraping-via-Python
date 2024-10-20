import requests
import pandas as pd

product_list = []
file_name = '';

for i in range(1,20):
    cookies = {
        '^cookie: AnonymousCustomerNumber': 'yE5JnprN1fV0ptH0t06pgZcupvAwuj8Wh/KFqQ3SDavyYwU0z8apb0feq9SHI7STWbQNlXCJaaqZOT5D6qVNJRInZMc=',
        'CustomerNumber': '',
        'CFIPCountry': '',
        '_gid': 'GA1.2.1413835535.1728775503',
        'ai_user': 'v3Kv1^|2024-10-12T23:25:04.577Z',
        'favListViewCookie': 'false',
        'ASP.NET_SessionId': 'nvtryxpxnpf2f1n1ysxszok4',
        'ActiveCartPriceLevel': '+oyjTmfjiH1sMKasK0uyvOPnj8/25RUlyCTSl9wrSHmuax+ZTbIokGe0hWFSFBUeQmZvMA==',
        'CurrencyCode': 'e1qKusVXy+P40Bz+ZabiBTEmVXNAlt1szrUR8hvUfO/Z2CnuwDwrNRssS0c+6Y2r4cQrng==',
        '_gat': '1',
        'ai_session': 'cssDh^|1728813257687^|1728813296789.4',
        '_ga_EFKXNT814CG-EFKXNT814C': 'GS1.1.1728813258.3.1.1728813296.0.0.0',
        '_ga': 'GA1.1.1355915805.1728775503^',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5NjUyMjciLCJhcCI6IjExMjAxMjA3MzEiLCJpZCI6IjkwMzRkOTE1NTg3MTY0ZWMiLCJ0ciI6IjJkMGMzODQ3Y2NlNDQ1ZTkyYTUwNDNhYjBmODAxZjE3IiwidGkiOjE3Mjg4MTMzMDg1MDZ9fQ==',
        'priority': 'u=1, i',
        'referer': 'https://universalwholesaleonline.com/categories/828380/just-arrived/products',
        '^request-id': '^|R56sz.sAYQR^',
        '^sec-ch-ua': '^\\^Microsoft',
        'sec-ch-ua-mobile': '?1',
        '^sec-ch-ua-platform': '^\\^Android^\\^^',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-2d0c3847cce445e92a5043ab0f801f17-9034d915587164ec-01',
        '^tracestate': '2965227^@nr=0-1-2965227-1120120731-9034d915587164ec----1728813308506^',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36 Edg/129.0.0.0',
        'x-newrelic-id': 'Vg8BVFRRDxAJUVFVBggDV1A=',
    }

    params = (
        ('page', str(i)),
        ('sortOn', 'ItemID'),
        ('direction', 'Ascending'),
        ('filters', 'UDF16:,UDF17:,UDF18:,UDF19:,UDF20:'),
    )

    url1 = 'https://universalwholesaleonline.com/categories/828380/just-arrived/products'
    # url2 = 'https://universalwholesaleonline.com/categories/1011421/specials/products'
    # url3 = 'https://universalwholesaleonline.com/categories/1011421/specials/products'
    response = requests.get(url1, headers=headers, params=params, cookies=cookies)

    result = response.json()

    file_name = result['RootCategoryName']

    if len(result['Products'])==0:
      pass
      break

    for item in result['Products']:
      ItemID = item['ItemID']
      ItemName = item['ItemName']
      CatalogCode = item['CatalogCode']
      Price = item['Price']
      SpecialPrice = item['SpecialPrice']
      ProductURL = item['ProductURL']
      UPC = item['UPC']
      OrderMinimumQuantity = item['OrderMinimumQuantity']
      OnHandQuantity = item['OnHandQuantity']
      BasePrice = item['AllPrices']['BasePrice']
      Level1 = item['AllPrices']['Level1']
      Level2 = item['AllPrices']['Level2']
      Level3 = item['AllPrices']['Level3']
      Level4 = item['AllPrices']['Level4']
      Level5 = item['AllPrices']['Level5']
      Level6 = item['AllPrices']['Level6']
      Level7 = item['AllPrices']['Level7']
      Level8 = item['AllPrices']['Level8']
      Level9 = item['AllPrices']['Level9']
      Level10 = item['AllPrices']['Level10']
      Level11 = item['AllPrices']['Level11']
      Level12 = item['AllPrices']['Level12']
      Level13 = item['AllPrices']['Level13']
      Level14 = item['AllPrices']['Level14']
      Level15 = item['AllPrices']['Level15']
      Level16 = item['AllPrices']['Level16']
      Level17 = item['AllPrices']['Level17']
      Level18 = item['AllPrices']['Level18']
      Level19 = item['AllPrices']['Level19']
      Level20 = item['AllPrices']['Level20']
      SpecialPrice = item['AllPrices']['SpecialPrice']

      product = {
        'ItemID': ItemID,
        'ItemName': ItemName,
        'CatalogCode': CatalogCode,
        'Price': Price,
        'SpecialPrice': SpecialPrice,
        'ProductURL': ProductURL,
        'UPC': UPC,
        'OrderMinimumQuantity': OrderMinimumQuantity,
        'OnHandQuantity': OnHandQuantity,
        'BasePrice': BasePrice,
        'Level1Price': Level1,
        'Level2Price': Level2,
        'Level3Price': Level3,
        'Level4Price': Level4,
        'Level5Price': Level5,
        'Level6Price': Level6,
        'Level7Price': Level7,
        'Level8Price': Level8,
        'Level9Price': Level9,
        'Level10Price': Level10,
        'Level11Price': Level11,
        'Level12Price': Level12,
        'Level13Price': Level13,
        'Level14Price': Level14,
        'Level15Price': Level15,
        'Level16Price': Level16,
        'Level17Price': Level17,
        'Level18Price': Level18,
        'Level19Price': Level19,
        'Level20Price': Level20,
        'SpecialPrice': SpecialPrice,
      }

      product_list.append(product)

df = pd.DataFrame(product_list)
df.to_csv('ProductSheets/'+file_name+'-universalwholesaleonline-price-list.csv')
print('saved to file.')