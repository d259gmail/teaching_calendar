from django.urls import path

from teaching_calendar.calendar_app import views

app_name = "calendar_app"

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('download_schedule/<str:format>/', views.download_schedule, name='download_schedule'),
]
