from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add-to-favorites/<int:book_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('add-review/<int:book_id>/', views.add_review, name='add_review'),
    path('checkout/<int:book_id>/', views.checkout, name='checkout'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_books, name='category_books'),
    path('search/', views.search, name='search'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
