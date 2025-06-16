from django.urls import path
from .views import ChamadoAPIView, ChamadosAPIView, ClosedIssueAPIView, FilteredQuestionAPIView, QuestionAPIView

from . import views


urlpatterns = [
    path('chamados/', ChamadosAPIView.as_view(),name='chamado'),
    path('chamados/<int:pk>', ChamadoAPIView.as_view(), name="chamados"),
    path('closed/', ClosedIssueAPIView.as_view(), name="Chamados Fechados"),
    path('login/', views.login ),
    path('question/', QuestionAPIView.as_view(), name='Todas as questões'),
    path('question/<str:category__name>/', FilteredQuestionAPIView.as_view(), name='Questões de História')


]
