# bookstore/admin.py

from django.contrib import admin
from .models import Book, Category, Publisher, Review, Favorite

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category', 'publisher')
    list_filter = ('category', 'publisher')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'date_created')
    list_filter = ('book', 'rating')
    search_fields = ('book__title', 'user')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'date_added')
    list_filter = ('user', 'book')
    search_fields = ('user__username', 'book__title')
