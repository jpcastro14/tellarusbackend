from dataclasses import field
from rest_framework import serializers

from .models import Category, Chamado
from .models import Question

class ChamadoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Chamado
        fields = [
            'id',
            'created_at',
            'active',
            'eventType',
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

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    field = [
        'category_id',
        'category_name'
    ]
class QuestionSerializer(serializers.ModelSerializer):

    question_category = serializers.StringRelatedField(read_only=True)

    class Meta: 
        model = Question
        fields = [ 
            'question_id',
            'question_body',
            'question_answer',
            'question_category'
        ]