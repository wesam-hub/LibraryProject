from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('books',views.books,name='books'),
    path('update/<int:book_id>',views.updatebook,name='updatebook'),
    path('delete/<int:book_id>',views.deletebook,name='deletebook'),
   

]