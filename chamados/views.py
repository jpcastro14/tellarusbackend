from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import ChamadoSerializer, QuestionSerializer
from .models import Chamado, Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

class QuestionAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class FilteredQuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        category = self.kwargs.get('category__name')
        return Question.objects.filter(category__name = category)


@api_view(['POST'])
def login(request):
    return Response(request.data)

@api_view(['POST'])
def signup(request):
    return Response({})

@api_view(['POST'])
def test_token(request):
    return Response({})