from django.contrib import admin
from .models import MatchingStrings, Tickets, Channels

@admin.register(MatchingStrings)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('string',)
    search_fields = ('string',)
    list_filter = ('string',)
@admin.register(Tickets)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user_name',)
    search_fields = ('user_name',)
    list_filter = ('user_name',)
@admin.register(Channels)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
