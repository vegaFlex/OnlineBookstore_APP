from django.core.management.base import BaseCommand
from bookstore.models import Book
import json

class Command(BaseCommand):
    help = 'Import books from JSON file'

    def handle(self, *args, **kwargs):
        with open('books.json', 'r', encoding='utf-8') as file:
            books = json.load(file)

            for book_data in books:
                book, created = Book.objects.get_or_create(
                    title=book_data['title'],
                    author=book_data['author'],
                    isbn=book_data['isbn'],
                    defaults={
                        'price': book_data['price'],
                        'description': book_data['description'],
                        'cover_image': book_data['image_url'],
                        'category': book_data['category'],
                        'publication_year': book_data['publication_year'],
                        'publisher': book_data['publisher'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added book: {book.title}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Book already exists: {book.title}'))
