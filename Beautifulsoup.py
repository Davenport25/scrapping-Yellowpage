import requests
from bs4 import BeautifulSoup
import pandas as pd

my_list = []

def extract(url):
   # url = 'https://www.yellowpages.com/houston-tx/restaurants'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    r = requests.get(url, headers=headers)
    bee = BeautifulSoup(r.content, 'html.parser')
    # print(bee.title.get_text())

    return bee.find_all('div', class_ = 'info')

def transform(beeHtml):
    x = 1
    beeHtml = extract(f'https://www.yellowpages.com/houston-tx/restaurants?page={x}')
    for item in beeHtml:
        name = item.find('a', class_ = 'business-name').text
    #  print(name)
        
        try:
            address = item.find('div', class_ = 'adr').text
        except:
            address = ''
    #  print(address)

        try:
            telephone = item.find('div', class_ = 'phones phone primary').text
        except:
            telephone = ''
    #   print(telephone)




        information = {
            'name': name,
            'address': address,
            'telephone': telephone
        }
    #  print(information)
        my_list.append(information)
    return
 
def load():
        df = pd.DataFrame(my_list)
        df.to_csv('yellow.csv', index= False)

for x in range(1,9):
        print('Download page {x}')
        beeHtml = extract(f'https://www.yellowpages.com/houston-tx/restaurants?page={x}')
        transform(beeHtml)
print(len(my_list))


load()
print('save to csv')





