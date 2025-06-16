from django.contrib import admin
from .models import Chamado, Question, Category

# Register your models here.

@admin.register(Chamado)

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('eventTitle', 'eventSector','eventArea','eventCriticality','eventPriority','eventDescription', 'active')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('body', 'answer', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']