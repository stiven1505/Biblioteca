from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#formulario personalizado para registro de usuario con los form de django

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_superuser = forms.BooleanField(label='Usuario Admnisitrador', required=False)  # Campo para definir si es superusuario

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superuser']
        help_texts = {k: "" for k in fields}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        # Establecer is_superuser en True o False según el formulario
        if self.cleaned_data['is_superuser']:
            user.is_superuser = True
        else:
            user.is_superuser = False
        
        user.save()  # Guardar el usuario con el estado de is_superuser

        return user

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'stock']