from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet
from .models import AdminTheme
from .serializers import AdminThemeSerializer
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework.permissions import IsAdminUser




class AdminThemeViewSet(ModelViewSet):
    queryset = AdminTheme.objects.all()
    serializer_class = AdminThemeSerializer
    permission_classes=[IsAdminUser]

























