import requests
from bs4 import BeautifulSoup
import json

def scrape_books():
    url = 'https://hermesbooks.bg/novi-knigi'  # Можете да промените URL-а според категорията
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []

    for item in soup.find_all('div', class_='book-item'):
        title = item.find('h3', class_='book-title').text.strip()
        author = item.find('p', class_='author').text.strip()
        price = item.find('span', class_='price').text.strip()
        image_url = item.find('img', class_='book-cover')['src']
        description = item.find('p', class_='description').text.strip()

        category = item.find('span', class_='category').text.strip()
        publication_year = item.find('span', class_='year').text.strip()
        publisher = item.find('span', class_='publisher').text.strip()

        publication_year = int(publication_year) if publication_year.isdigit() else None

        book = {
            'title': title,
            'author': author,
            'price': price,
            'image_url': image_url,
            'description': description,
            'category': category,
            'publication_year': publication_year,
            'publisher': publisher
        }

        books.append(book)

    # Запазваме данните във файл
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

    print('Скрайпингът завърши успешно. Данните са записани в books.json')

if __name__ == "__main__":
    scrape_books()
