from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from appointment_app.views import AppointmentApi


urlpatterns = [
    path('appointment/', AppointmentApi.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)