from django.urls import path
from .views import ChamadoAPIView, ChamadosAPIView


urlpatterns = [
    path('chamados/', ChamadosAPIView.as_view(),name='chamado'),
    path('chamados/<int:pk>', ChamadoAPIView.as_view(), name="chamados")
]
