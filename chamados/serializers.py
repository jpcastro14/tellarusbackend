from rest_framework import serializers

from .models import Category, Chamado, Question

class ChamadoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Chamado
        fields = [
            'active',
            'created_at',
            'eventTitle',
            'eventSector',
            'eventArea',
            'eventCriticality',
            'eventPriority',
            'eventDescription',
            'eventCloseDesc',
            'eventFinalStatus'
        ]

"""  python3 manage.py runserver 172.16.239.177:8000 """

class QuestionSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = [
            'body',
            'answer',
            'category'
        ]

class CategorySerializer(serializers.ModelField):

    class Meta:
        model = Category
        fields = "__all__"