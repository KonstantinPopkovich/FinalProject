from django.contrib import admin
from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'writer', 'category', 'rating', 'price', 'amount')
    search_fields = ('name', 'writer__name_authors', 'category__name_category')

class EBooksAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'country', 'article_number', 'amount', 'rating', 'price')
    search_fields = ('manufacturer__manufacturer_name', 'model__model_name')

class EBooks_other_shopsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('ebooks',)

class OfficeSuppliesAdmin(admin.ModelAdmin):
    list_display = ("brand", "country_manufacturer", 'article_number', 'manufactured_date', 'amount')

admin.site.register(Books, BooksAdmin)
admin.site.register(EBooks, EBooksAdmin)
admin.site.register(EBooks_other_shops, EBooks_other_shopsAdmin)
admin.site.register(OfficeSupplies, OfficeSuppliesAdmin)
admin.site.register(Authors)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Pen)
admin.site.register(Pencil)
admin.site.register(Paper)
admin.site.register(Notebook)
admin.site.register(Clip)
admin.site.register(Envelope)
admin.site.register(Paint)
admin.site.register(Marker)




