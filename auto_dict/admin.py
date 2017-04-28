from django.contrib import admin
from .models import Word, Sentence, Translation
# Register your models here.

class WordAdmin(admin.ModelAdmin):
    list_display = ['word', 'definition']


class SentenceAdmin(admin.ModelAdmin):
    list_display = ['sentence']

class TranslationAdmin(admin.ModelAdmin):
    list_display = ['sentence' , 'translation']


admin.site.register(Translation, TranslationAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Sentence, SentenceAdmin)
