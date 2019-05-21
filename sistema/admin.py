from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from django.contrib import admin
from .models import *


admin.site.register(Empreendimento)
admin.site.register(Bloco)
admin.site.register(Apartamento)
admin.site.register(Chamado)
admin.site.register(CategoriaDeProblema)
admin.site.register(EventosChamado)
admin.site.register(Usuarios)


