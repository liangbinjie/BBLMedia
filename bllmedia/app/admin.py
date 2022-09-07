from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contacto


class ContactFiltering(admin.ModelAdmin):
    list_display = ['email', 'description']


admin.site.register(Contacto, ContactFiltering)
admin.site.unregister(Group)