from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

#pegando a classe do models

# Só existe porque queremos que no admin apareça o campo filmes vistos personalizados
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filme_vistos',)})
)

UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)

