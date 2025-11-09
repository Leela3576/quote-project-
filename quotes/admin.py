from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text_short', 'author', 'created_at')
    def text_short(self, obj):
        return obj.text[:60]
    text_short.short_description = 'Quote'