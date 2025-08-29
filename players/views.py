from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


# ✅ API لعرض الهدافين
class TopScorersView(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.order_by('-goals')[:10]  # أعلى 10 هدافين
