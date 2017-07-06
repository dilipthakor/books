# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Author, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldset = [
        ("Book Details",{"fields": ["title","author"]}),
        ("Review",{"fields": ["is_favourite","review","date_reviewed"]})
    ]
    
    readonly_fields = ("date_reviewed")
    
    def book_authors(self,obj):
        return obj.list_authors()
    
    book_authors.short_description = "Author(s)"
    
    list_display = ("title","date_reviewed","is_favourite",)
    list_editable = ("is_favorite",)
    list_display_links = ("title","date_reviewed",)
    list_filter = ("is_favourite",)
    search_fields = ("title","authors_name",)

# Register your models here.
admin.site.register(Book)


