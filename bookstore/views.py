from .models import Book, Category, Favorite
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ReviewForm
import stripe
from django.conf import settings
from django.db.models import Q

# Страница за началната страница
def index(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'bookstore/index.html', {'books': books, 'categories': categories})

# Детайлна страница за книгата
# def book_detail(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     return render(request, 'bookstore/book_detail.html', {'book': book})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    categories = Category.objects.all()  # Вземa всички категории
    return render(request, 'bookstore/book_detail.html', {'book': book, 'categories': categories})

# Добавяне на книга към любимите
@login_required
def add_to_favorites(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    Favorite.objects.get_or_create(user=request.user, book=book)
    return redirect('book_detail', book_id=book.id)

# Добавяне на отзив за книга
@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user.username
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'bookstore/add_review.html', {'form': form, 'book': book})

# Конфигурация на Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Чекаут функционалност с Stripe
@login_required
def checkout(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': book.title,
                },
                'unit_amount': int(book.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/bookstore/success/',
        cancel_url='http://localhost:8000/bookstore/cancel/',
    )
    return redirect(session.url, code=303)

# Изглед за категориите - всички книги в дадена категория
def category_books(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = Book.objects.filter(category=category)
    categories = Category.objects.all()  # За да покажa всички категории в aside
    return render(request, 'bookstore/category_books.html', {'category': category, 'books': books, 'categories': categories})

# Функция за показване на всички категории
def categories(request):
    categories = Category.objects.all()
    return render(request, 'bookstore/categories.html', {'categories': categories})



def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__icontains=query)
        )
    return render(request, 'bookstore/search_results.html', {'results': results, 'query': query})
