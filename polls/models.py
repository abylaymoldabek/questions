from django.db import models
from django.utils.safestring import mark_safe


class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    negative = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    fullName = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    negative_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    positive_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullName

    class Meta:
        unique_together = ['phone', 'created_date']

    def get_excel(self):
        return mark_safe('<a href="%s">Скачать отчет</a>' % f'/polls/export_excel/')

    get_excel.short_description = 'Отчеты'
    get_excel.allow_tags = True
