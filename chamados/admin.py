from django.contrib import admin
from .models import Chamado, Question, Category, Users

# Register your models here.

@admin.register(Chamado)

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('eventTitle', 'eventSector','eventArea','eventCriticality','eventPriority','eventDescription', 'active')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display =('question_id','question_body','question_answer', 'question_category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('category_name','category_id')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_alias')