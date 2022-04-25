from datetime import date
import typing
from decimal import Decimal

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, Answer, UserAnswer

from datetime import datetime
import xlwt
from django.http import HttpResponse


class GetQuestion(APIView):
    def post(self, request, format=None):  # noqa
        questions = Question.objects.all()
        result = self._get_questions(questions=questions)
        return Response(data={'result': result})

    def _get_questions(self, questions: typing.List[Question]):
        result = []
        for question in questions:
            question_data = {'id': question.id,
                             'question': question.text,
                             'answers': self._get_answers(question=question)}
            result.append(question_data)
        return result

    @staticmethod
    def _get_answers(question: Question):
        answers = Answer.objects.filter(question_id=question.id)
        return [{'name': f"question_{question.id}", 'value': not answer.negative} for answer in answers]


class CheckUser(APIView):

    def post(self, request, format=None):  # noqa
        if not request.data.get('phone'):
            return Response({'status': 'error', 'message': 'Phone required'}, status=400)
        try:
            _ = UserAnswer.objects.get(phone=request.data.get('phone'),
                                       created_date=date.today())
            return Response(data={'status': 'error', 'message': 'User also have a answer'})

        except UserAnswer.DoesNotExist:
            return Response(data={'status': 'success'})


class CreateUserAnswer(APIView):

    def post(self, request, format=None):  # noqa
        try:
            answers = request.data if request.data else {}
            full_name = answers.get('full_name')
            email = answers.get('email')
            phone = answers.get('phone')
            answers = answers.get('answers')
            negative_count = 0
            for answer in answers.values():
                if answer is False:
                    negative_count += 1
            negative_percentage = Decimal((negative_count * 100) / len(answers)).quantize(Decimal("1.00"))
            positive_percentage = Decimal(100 - negative_percentage).quantize(Decimal("1.00"))
            _ = UserAnswer.objects.create(fullName=full_name, mail=email, phone=phone,
                                          negative_percentage=negative_percentage - Decimal("0.01")
                                          if negative_percentage >= 100 else negative_percentage,
                                          positive_percentage=positive_percentage - Decimal("0.01")
                                          if positive_percentage >= 100 else positive_percentage)
            return Response({'status': 'success', 'message': 'Answers successfully created'}, status=201)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=500)


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Otchet' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Участники')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style = xlwt.easyxf('pattern: pattern solid, fore_colour green;'
                             'font: colour black, bold True;')
    columns = ['№', 'Толық аты жөні', 'Пошта', 'Ұялы телефоны', 'Негатив проценті', 'Позитив проценті',
               'Cұралған уакыт']
    for col in range(len(columns)):
        ws.write(row_num, col, columns[col], font_style)
    font_style = xlwt.XFStyle()
    rows = UserAnswer.objects.filter(negative_percentage__gte=50).values_list('id', 'fullName', 'mail', 'phone',
                                                                              'negative_percentage',
                                                                              'positive_percentage', 'created_date')
    for row in rows:
        row = list(row)
        row_num += 1
        for col in range(len(row)):
            ws.write(row_num, col, str(row[col]), font_style)
    wb.save(response)
    return response
