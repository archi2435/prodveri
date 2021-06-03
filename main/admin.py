from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import *


class AutoSlug(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class catalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('title', 'image_tag', 'category', 'sub_category', 'collection', 'price')
    readonly_fields = ('image_tag',)   

class OrdersList(admin.ModelAdmin):

    list_display = ('Date', 'first_name', 'Middle_name', 'Address', 'Phone', 'Cart')
    readonly_fields = ('Date', 'first_name', 'Middle_name', 'Phone', 'Address', 'Cart',)


admin.site.register(category, AutoSlug)
admin.site.register(catalog, catalogAdmin)
admin.site.register(sub_category, AutoSlug)
admin.site.register(collection, AutoSlug)
#admin.site.register(Sizes)
admin.site.register(Furnite_category, AutoSlug)
admin.site.register(Furnite_sub_category, AutoSlug)
admin.site.register(Furnite)
admin.site.register(News)
admin.site.register(Orders, OrdersList)