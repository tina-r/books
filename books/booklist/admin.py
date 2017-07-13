from django.contrib import admin
from .models import BookList
from django.contrib.auth.models import User

class BookListAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'pub_date')


admin.site.register(BookList, BookListAdmin)


