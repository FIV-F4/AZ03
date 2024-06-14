import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.prettify()

url = 'https://jira.petrovich.tech/secure/CreateIssue!default.jspa'
html_content = get_html_content(url)
if html_content:
    with open('divan_ru_page.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    print("HTML content saved to 'divan_ru_page.html'")
else:
    print("Failed to retrieve the HTML content.")
