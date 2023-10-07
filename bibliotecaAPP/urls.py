from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import AddBookView ,ListBooksView


urlpatterns = [
	path('', ListBooksView.as_view(), name='listarLibros'),
    path('listar-libros/', ListBooksView.as_view(), name='listarLibros'),
	path('register/', views.register, name='register'),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('agregar-libro/', AddBookView.as_view(), name='add_book'),
    path('borrow_book/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return_book/<int:loan_id>/', views.return_book, name='return_book'),
    path('libros_prestados/', views.libros_prestados, name='libros_prestados'),
    path('historial_libros/', views.historial_libros, name='historial_libros'),

    #-----------REST 
   # Rutas para las vistas basadas en clases relacionadas con la API de libros
 # Rutas para perfiles de usuario
    path('api/profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('api/profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),

    # Rutas para publicaciones (posts)
    path('api/posts/', views.PostList.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),

    # Rutas para libros
    path('api/books/', views.BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),

    # Rutas para préstamos de libros
    path('api/loans/', views.LoanList.as_view(), name='loan-list'),
    path('api/loans/<int:pk>/', views.LoanDetail.as_view(), name='loan-detail'),

    # Rutas para tomar prestado y devolver libros
    path('api/borrow/<int:book_id>/', views.BorrowBook.as_view(), name='borrow-book'),
    path('api/return/<int:loan_id>/', views.ReturnBook.as_view(), name='return-book')

	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)