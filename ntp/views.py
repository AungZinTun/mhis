from django.shortcuts import render
from rest_framework import viewsets
from .serializer import NotifySerializer
from .models import Notify
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
# Create your views here.

class NotifyViewSet(viewsets.ModelViewSet):
    serializer_class=NotifySerializer
    queryset=Notify.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    renderer_classes = [JSONRenderer]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)