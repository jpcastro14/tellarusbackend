from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Chamado(Base):
    eventTitle = models.CharField(max_length=255)
    eventType = models.CharField(max_length=255)
    eventSector = models.CharField(max_length=255)
    eventArea = models.CharField(max_length=255)
    eventCriticality = models.IntegerField()
    eventCriticalityColor = models.CharField(blank=True,max_length=50)
    eventPriority = models.IntegerField()
    eventDescription = models.CharField(max_length=2000)    
    eventCloseDesc = models.CharField(max_length = 2000, blank = True)
    eventFinalStatus = models.BooleanField(default=False, blank= True)
    class Meta: 
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"

    def __str__(self):
        return self.eventTitle

