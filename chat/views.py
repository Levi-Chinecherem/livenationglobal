# chat/views.py
from rest_framework import generics, permissions

from accounts.models import CustomUser
from .models import Chat
from .serializers import ChatSerializer

class UserChatListView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(user=user)

class AdminChatListView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAdminUser]

class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserChatCreateView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        # Automatically associate the chat with the first admin user (modify as needed)
        admin_user = CustomUser.objects.filter(is_staff=True).first()
        serializer.save(user=user, admin=admin_user)

class AdminChatCreateView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        admin_user = self.request.user
        serializer.save(admin=admin_user)

