from django.contrib import admin

from .models import Question, Choice, Cat

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Cat)