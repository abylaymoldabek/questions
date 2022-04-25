from django.urls import path

from polls.views import CheckUser, GetQuestion, CreateUserAnswer, export_excel

urlpatterns = [
    path('questions/', GetQuestion.as_view()),
    path('check_user/', CheckUser.as_view()),
    path('user_answer/', CreateUserAnswer.as_view()),
    path('export_excel/', export_excel, name='excel'),
]
