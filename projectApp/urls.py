from django.urls import path
from . import views
 
urlpatterns = [
    # path('testapi', views.testapi, name='testapi'),
    path('add_book', views.add_book, name='add_book'),
    path('show_books', views.show_books, name='show_books'),
]