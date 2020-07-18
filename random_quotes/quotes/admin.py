from django.contrib import admin
from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ("quote_text","quote_by")


# Register your models here.
admin.site.register(Quote, QuoteAdmin)
