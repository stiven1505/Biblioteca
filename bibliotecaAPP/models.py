from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
#tabla para llevar registro de los libros prestados con libros y usuarios
class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    delivery_status = models.BooleanField(default=False)  # False indica que no se ha entregado, True indica que se ha entregado
    loan_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Préstamo de "{self.book.title}" a {self.user.username}'