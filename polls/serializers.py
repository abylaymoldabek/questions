from rest_framework import serializers
from .models import Question, Answer, UserAnswer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'


class AnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()

    def validate_answers(self, answers):
        if not answers:
            raise serializers.Validationerror("Answers must be not null.")
        return answers

    def save(self):
        answers = self.data['answers']
        for question_id in answers:
            question = Question.objects.get(name=question_id.get('name'))
            choices = question_id.get('value')
            for choice_id in choices:
                choice = UserAnswer.objects.get(pk=choice_id)
                Answer(user=user, question=question, choice=choice).save()
                user.is_answer = True
                user.save()
