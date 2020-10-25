from django.contrib import admin

from .models import Question, Choice, top10cat, inputcat

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(top10cat)
admin.site.register(inputcat)