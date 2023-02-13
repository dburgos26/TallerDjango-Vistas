from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.measurementss_view, name='measurementss_view'),
    path('<int:pk>', views.measurements_view, name='measurements_view'),
]
