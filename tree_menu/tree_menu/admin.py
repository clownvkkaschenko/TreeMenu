from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name',]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'main_menu', 'url', 'id']
    list_filter = ['main_menu__name']
    search_fields = ['name',]
    prepopulated_fields = {'url': ('name',)}
