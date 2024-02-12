# # chat/admin.py
# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
# from .models import Chat

# @admin.register(Chat)
# class ChatAdmin(admin.ModelAdmin):
#     list_display = ('user', 'admin', 'message', 'timestamp', 'is_admin_message')
#     search_fields = ('user__email', 'admin__email', 'message')
#     list_filter = ('is_admin_message',)
#     date_hierarchy = 'timestamp'
#     readonly_fields = ('timestamp',)
#     fieldsets = (
#         (None, {
#             'fields': ('user', 'admin', 'message', 'timestamp', 'is_admin_message')
#         }),
#     )
#     ordering = ('-timestamp',)
    
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         # Filter admin chats for non-admin users
#         if not request.user.is_staff:
#             qs = qs.filter(user=request.user)
#         return qs
