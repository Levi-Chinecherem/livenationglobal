# chat/urls.py
from django.urls import path
from .views import UserChatListView, UserChatCreateView, AdminChatCreateView, AdminChatListView, ChatDetailView

urlpatterns = [
    path('user-chats/', UserChatListView.as_view(), name='user-chat-list'),
    path('admin-chats/', AdminChatListView.as_view(), name='admin-chat-list'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),
    path('user-chats/create/', UserChatCreateView.as_view(), name='user-chat-create'),
    path('admin-chats/create/', AdminChatCreateView.as_view(), name='admin-chat-create'),
    
]
