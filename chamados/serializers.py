from rest_framework import serializers

from .models import Chamado

class ChamadoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Chamado
        fields = [
            'created_at',
            'active',
            'eventType',
            'eventTitle',
            'eventSector',
            'eventArea',
            'eventCriticality',
            'eventPriority',
            'eventDescription'
        ]