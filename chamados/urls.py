from django.urls import path
from .views import CategoriesApiView, ChamadoAPIView, ChamadosAPIView, ClosedIssueAPIView, QuestionApiView, QuestionsApiView, UsersAPIView

from . import views


urlpatterns = [
    path('chamados/', ChamadosAPIView.as_view(),name='chamado'),
    path('chamados/<int:pk>', ChamadoAPIView.as_view(), name="chamados"),
    path('closed/', ClosedIssueAPIView.as_view(), name="Chamados Fechados"),
    path('login/', views.login ),
    path('questions/',QuestionsApiView.as_view(),name="Questões"),
    path('questions/<int:pk>', QuestionApiView.as_view(), name='Questão'),
    path('categories/', CategoriesApiView.as_view(), name="Categorias"),
    path('users/', UsersAPIView.as_view(), name="Jogadores")


]
