from django.shortcuts import render
from rest_framework import permissions, viewsets

from ropes.models import ClimbingRopes, ColorSchemes, OtherRopes, Ropes
from ropes.serializers import (ClimbingRopesSerializer, ColorSchemesSerializer,
                               OtherRopesSerializer, RopesSerializer)


class RopesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ropes to be viewed or edited.
    """
    queryset = Ropes.objects.all()
    serializer_class = RopesSerializer


class ColorSchemesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all color schemes to be viewed or edited.
    """
    queryset = ColorSchemes.objects.all()
    serializer_class = ColorSchemesSerializer


class ClimbingRopesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all climbing ropes to be viewed or edited.
    """
    queryset = ClimbingRopes.objects.all()
    serializer_class = ClimbingRopesSerializer


class OtherRopesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all other ropes to be viewed or edited.
    """
    queryset = OtherRopes.objects.all()
    serializer_class = OtherRopesSerializer
