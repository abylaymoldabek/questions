from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import  ListAPIView, CreateAPIView
from .models import Question


class GetQuestion(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionAnswer(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer
