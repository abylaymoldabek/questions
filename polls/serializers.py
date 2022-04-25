from rest_framework import serializers

from .models import Question, UserAnswer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'
