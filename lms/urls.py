from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.UserView.as_view(),name='users'),
    path('users/<int:id>/',views.UserIdView.as_view(), name='user-detail'),
    path('books/',views.BookView.as_view(),name='books'),
    path('books/<int:id>/',views.BookDetailsView.as_view(),name='book_detail'),
    path('borrow/',views.BorrowedBooksView.as_view(),name='borrowed_book'),
    # path('return/',views.ReturnBookView.as_view(),name='return')
]

