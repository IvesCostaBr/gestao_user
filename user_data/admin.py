from django.contrib import admin
from .models import Endereco, UserData
# Register your models here.
admin.site.register(UserData)
admin.site.register(Endereco)
