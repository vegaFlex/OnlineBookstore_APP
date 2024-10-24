

import random
from django.core.management.base import BaseCommand
from selenium.webdriver.common.by import By

from bookstore.models import Book, Category, Publisher
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

class Command(BaseCommand):
    help = 'Populate the database with books from Chapter.bg using Firefox and Selenium'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to populate books from Chapter.bg...'))

        # Настройка на Firefox WebDriver
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Работи в фонов режим
        # firefox_service = Service('./geckodriver.exe')  # Път към geckodriver
        firefox_service = Service('C:\\Users\\vega_\\Desktop\\library_management_app\\Online_Bookstore\\geckodriver.exe')# Път към geckodriver


        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
        url = 'https://www.chapter.bg/knigi.html'

        try:
            driver.get(url)
            time.sleep(5)  # Изчакваме съдържанието да се зареди

            # Намери книгите на страницата
            books = driver.find_elements(Bry.CLASS_NAME, 'book-item')  # Актуализиран селектор за Chapter.bg

            if not books:
                self.stdout.write(self.style.ERROR('No books found on the page. Check the structure of the site.'))
                return

            categories = Category.objects.all()
            publishers = Publisher.objects.all()

            for i, book in enumerate(books[:30]):
                title = book.find_element(By.CLASS_NAME, 'product-name').text.strip()
                author = book.find_element(By.CLASS_NAME, 'product-author').text.strip() if book.find_element(By.CLASS_NAME, 'product-author') else 'Unknown Author'
                description = book.find_element(By.CLASS_NAME, 'product-description').text.strip() if book.find_element(By.CLASS_NAME, 'product-description') else 'No description available.'
                price_text = book.find_element(By.CLASS_NAME, 'price').text.replace('лв.', '').strip()
                price = float(price_text.replace(',', '.')) if price_text else 0.0
                isbn = f"{random.randint(1000000000000, 9999999999999)}"
                cover_image = book.find_element(By.TAG_NAME, 'img').get_attribute('src') if book.find_element(By.TAG_NAME, 'img') else None
                category = random.choice(categories) if categories else None
                publication_year = random.randint(1990, 2023)
                publisher = random.choice(publishers) if publishers else None

                new_book = Book(
                    title=title,
                    author=author,
                    description=description,
                    price=price,
                    isbn=isbn,
                    cover_image=cover_image,
                    category=category,
                    publication_year=publication_year,
                    publisher=publisher
                )
                new_book.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {title}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
        finally:
            driver.quit()
