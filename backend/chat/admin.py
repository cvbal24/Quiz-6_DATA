from django.contrib import admin
from .models import ChatHistory


class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'message')
    search_fields = ('user__email', 'message')
    list_filter = ('created_at', 'user')
    readonly_fields = ('created_at',)


admin.site.register(ChatHistory, ChatHistoryAdmin)
