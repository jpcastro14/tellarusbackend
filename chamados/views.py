from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import ChamadoSerializer
from .models import Chamado
# Create your views here.

class ChamadosAPIView(generics.ListCreateAPIView):
    queryset = Chamado.objects.filter(active = True)
    serializer_class = ChamadoSerializer


class ChamadoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

class ClosedIssueAPIView(generics.ListCreateAPIView):
    queryset = Chamado.objects.filter(active = False)
    serializer_class = ChamadoSerializer
