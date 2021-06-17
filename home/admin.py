from django.contrib import admin
from . models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'household', 'redemmed', 'mountain', 'christ', 'apostolic', 'pub_date']




class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'choice_text', 'votes']
    readonly_fields = ['id', 'choice_text', 'votes']


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)