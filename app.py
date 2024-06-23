import requests
from bs4 import BeautifulSoup

def fetch_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    data = []
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        data.append({'quote': text, 'author': author})
    
    return data

def display_quotes(data):
    for i, item in enumerate(data, start=1):
        print(f"Quote {i}:")
        print(f"\"{item['quote']}\"")
        print(f"- {item['author']}")
        print()

def main():
    print("Interactive Web Scraper")
    print("=======================")
    url = input("Enter the URL to scrape (e.g., http://quotes.toscrape.com/): ").strip()
    
    try:
        data = fetch_quotes(url)
        display_quotes(data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
