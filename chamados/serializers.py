from rest_framework import serializers

from .models import Chamado

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
            'eventCloseDesc'
        ]

"""  python3 manage.py runserver 172.16.239.177:8000 """