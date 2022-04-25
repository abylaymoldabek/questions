from django.contrib import admin
from .models import Answer, Question, UserAnswer

admin.site.register(Question)
admin.site.register(Answer)
# admin.site.register(UserAnswer)


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'get_excel']
    readonly_fields = ['get_excel']
