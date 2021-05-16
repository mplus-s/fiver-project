from rest_framework import generics
from .models import Message
from .serializers import InitializeMessageSerializer, MessageSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class StartMessaging(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = InitializeMessageSerializer
    permission_classes = [IsAuthenticated]


class Conversation(generics.RetrieveAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ["product_uid",]
    
        
    def get_object(self):
        user = self.request.user
        return user.get_messages_for_product(product_uid=self.kwargs["product_uid"])


class AllMessages(generics.ListAPIView):
    pass