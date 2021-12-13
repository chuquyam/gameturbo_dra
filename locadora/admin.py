from django.contrib import admin
from .models import Cliente, Jogo, Alugar


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Jogo)
admin.site.register(Alugar)