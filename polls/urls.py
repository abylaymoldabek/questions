from django.urls import path

from polls.views import QuestionAnswer, GetQuestion

urlpatterns = [
    path('', GetQuestion.as_view()),
    path('answer/', QuestionAnswer.as_view()),
]
