from rest_framework import generics
from .models import Card
from .serializers import CardSerializer

class CardList(generics.ListCreateAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = Card.objects.all()
        return queryset

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


