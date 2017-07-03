from django.contrib import admin
from .models import BookList

class BookListAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')


admin.site.register(BookList, BookListAdmin)


