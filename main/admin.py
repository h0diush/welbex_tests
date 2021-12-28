from django.contrib import admin

from .models import BaseModel


@admin.register(BaseModel)
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'qty', 'distance')
