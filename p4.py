import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_prices_from_divanru(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for product in soup.find_all('div', class_='_Ud0k U4KZV'):
        name_tag = product.find('a', class_='ui-GPFV8')
        price_tag = product.find('span', class_='ui-LD-ZU KIkOH', attrs={'data-testid': 'price'})

        if name_tag and price_tag:
            name = name_tag.get('title').strip() if name_tag.has_attr('title') else name_tag.text.strip()
            price = price_tag.text.strip()
            products.append({'Name': name, 'Price': price})
        else:
            print(f"Skipping product due to missing name or price. Product HTML: {product}")

    if not products:
        print("No products found. Please check the website structure and class names.")

    return pd.DataFrame(products)


url = 'https://www.divan.ru/category/divany'
prices_df = get_prices_from_divanru(url)
if not prices_df.empty:
    prices_df.to_csv('prices_from_divanru.csv', index=False)
    print(prices_df)
else:
    print("No data extracted.")
