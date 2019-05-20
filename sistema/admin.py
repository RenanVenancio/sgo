from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from django.contrib import admin
from .models import *



class UsuarioInline(admin.StackedInline):
    model = Usuarios
    can_delete = False
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)




admin.site.register(Empreendimento)
admin.site.register(Bloco)
admin.site.register(Apartamento)
admin.site.register(Chamado)
admin.site.register(CategoriaDeProblema)
admin.site.register(EventosChamado)
admin.site.register(Usuarios)


