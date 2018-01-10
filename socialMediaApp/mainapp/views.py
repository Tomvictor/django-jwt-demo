from django.shortcuts import render
# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mainapp.serializer import CollegeSerializer
from mainapp.models import College


from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

class CollegeViewSet(ListAPIView):
    # permission_classes =
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = College.objects.all()
    serializer_class = CollegeSerializer