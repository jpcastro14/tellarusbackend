from django.urls import path
from .views import ChamadoAPIView, ChamadosAPIView, ClosedIssueAPIView, arts_question_list

from . import views


urlpatterns = [
    path('chamados/', ChamadosAPIView.as_view(),name='chamado'),
    path('chamados/<int:pk>', ChamadoAPIView.as_view(), name="chamados"),
    path('closed/', ClosedIssueAPIView.as_view(), name="Chamados Fechados"),
    path('login/', views.login ),
    path('question/', views.question_list, name='Todas as questões'),
    path('question/<str:param>/', views.arts_question_list, name='Questões de História')


]
