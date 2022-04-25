from django.conf import settings
from django.db import models


class AuthWithNumber(models.Model):
    fullName = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Question(models.Model):
    name = models.CharField(max_length=4096)

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class UserAnswer(models.Model):
    user = models.ForeignKey(AuthWithNumber, on_delete=models.DO_NOTHING, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return self.question
