from django.contrib import admin
from .models import Card, UserScore

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'time_taken', 'timestamp')
    list_filter = ('timestamp',)
    ordering = ('-score',)
