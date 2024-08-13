from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import io

from calendar_app.models import Lesson, Subject


@login_required
def dashboard(request):
    user = request.user
    lessons = Lesson.objects.filter(teacher=user)
    subjects = Subject.objects.filter(lesson__teacher=user).distinct()
    return render(request, 'users/user_detail.html',
                  {'object': user, 'lessons': lessons, 'subjects': subjects})


@login_required
def download_schedule(request, format):
    user = request.user
    lessons = Lesson.objects.filter(teacher=user)

    if format == 'excel':
        return generate_excel_schedule(lessons)
    elif format == 'pdf':
        return generate_pdf_schedule(lessons)
    return redirect('dashboard')


def generate_excel_schedule(lessons):
    df = pd.DataFrame([
        {'Subject': lesson.subject.name, 'Lesson': lesson.name, 'Date': lesson.date}
        for lesson in lessons
    ])

    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="schedule.xlsx"'
    return response


def generate_pdf_schedule(lessons):
    df = pd.DataFrame([
        {'Subject': lesson.subject.name, 'Lesson': lesson.name, 'Date': lesson.date}
        for lesson in lessons
    ])

    buffer = io.BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    pdf = canvas.Canvas('schedule.pdf', pagesize=letter)
    pdf.setFont('Helvetica-Bold', 24)
    pdf.drawCentredString(300, 750, 'Schedule')

    pdf.setFont('Helvetica-Bold', 18)
    pdf.drawString(100, 700, 'Subject')
    pdf.drawString(200, 700, 'Lesson')
    pdf.drawString(500, 700, 'Date')

    pdf.setFont('Helvetica', 12)
    for i, row in enumerate(df.itertuples()):
        pdf.drawString(100, 650 - i * 20, row.Subject)
        pdf.drawString(200, 650 - i * 20, str(row.Lesson))
        pdf.drawString(500, 650 - i * 20, str(row.Date))

    pdf.save()
    buffer = open('schedule.pdf', 'rb')
    response = HttpResponse(buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="schedule.pdf"'
    return response

