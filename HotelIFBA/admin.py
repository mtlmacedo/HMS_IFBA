from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from HotelIFBA.models import *
from HotelIFBA.forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUser(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['username', 'cpf', 'telefone']
    add_fieldsets = (
        (None, {
            "classes": ("wide1",),
            "fields": ("username", "password1", "password2", "cpf", "telefone")
        })
    )

admin.site.register(Usuario, CustomUser)
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Reserva)
admin.site.register(Estadia)