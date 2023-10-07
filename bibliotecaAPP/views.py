from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import View
from .forms import BookForm
from django.views.generic import ListView





def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request , f'Usuario {username} creado')
			return redirect ('listarLibros')
	else:
		form= UserRegisterForm()
	context = {'form': form}
	return render(request, 'register.html', context)

def listarLibros(request):
    return render(request, 'listar_libros.html')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AddBookView(View):
    template_name = 'book_form.html'

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarLibros')  # Redirige a la página de listar libros
        return render(request, self.template_name, {'form': form})
			


class ListBooksView(ListView):
    model = Book
    template_name = 'listar_libros.html'
    context_object_name = 'books'
    



@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    existing_loan = Loan.objects.filter(user=request.user, book=book, delivery_status=False).first()

    if not existing_loan:
        loan = Loan(user=request.user, book=book)
        loan.save()
        book.stock -= 1
        book.save()
    else:
        # Tratar el caso en el que el libro ya esté prestado por el usuario
        pass

    return redirect('listarLibros')

@login_required
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)

    if not loan.delivery_status:
        loan.delivery_status = True
        loan.save()
        book = loan.book
        book.stock += 1
        book.save()

    return redirect('listarLibros')

class BookListView(ListView):
    model = Book
    template_name = 'listar_libros.html'
    context_object_name = 'books'
    

@login_required
def libros_prestados(request):
    user = request.user
    loans = Loan.objects.filter(user=user, delivery_status=False)
    return render(request, 'libros_prestados.html', {'loans': loans})


@login_required
def historial_libros(request):
    user = request.user
    prestamos_actuales = Loan.objects.filter(user=user, delivery_status=False)
    prestamos_devueltos = Loan.objects.filter(user=user, delivery_status=True)
    return render(request, 'user_books.html', {'prestamos_actuales': prestamos_actuales, 'prestamos_devueltos': prestamos_devueltos})


#---------------- REST ----------------

from rest_framework import generics
from .models import Profile, Post, Book, Loan
from .serializers import ProfileSerializer, PostSerializer, BookSerializer, LoanSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Vista para listar todos los perfiles de usuario
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

# Vista para ver, actualizar y eliminar un perfil de usuario específico
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

# Vista para listar todos los posts
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Vista para ver, actualizar y eliminar un post específico
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Vista para listar todos los libros
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# Vista para ver, actualizar y eliminar un libro específico
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# Vista para listar todos los préstamos de libros
class LoanList(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

# Vista para ver, actualizar y eliminar un préstamo de libro específico
class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

# Vista para tomar prestado un libro
class BorrowBook(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        book = Book.objects.get(pk=book_id)

        existing_loan = Loan.objects.filter(user=request.user, book=book, delivery_status=False).first()

        if not existing_loan:
            loan = Loan(user=request.user, book=book)
            loan.save()
            book.stock -= 1
            book.save()
        else:
            # Tratar el caso en el que el libro ya esté prestado por el usuario
            pass

        return Response({'message': 'Libro prestado con éxito'}, status=status.HTTP_201_CREATED)

# Vista para devolver un libro prestado
class ReturnBook(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, loan_id):
        loan = Loan.objects.get(pk=loan_id)

        if not loan.delivery_status:
            loan.delivery_status = True
            loan.save()
            book = loan.book
            book.stock += 1
            book.save()

        return Response({'message': 'Libro devuelto con éxito'}, status=status.HTTP_200_OK)
