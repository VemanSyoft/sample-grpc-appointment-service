from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appointment_app.models import Appointment
from appointment_app.serializer import AppointmentSerializer
from grpc_settings.client import get_user


class AppointmentApi(APIView):
    def get(self, request, format=None):
        snippets = Appointment.objects.all()
        serializer = AppointmentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # user_info = get_user("vinuraveman@gmail.com")
        user_info = get_user(request.data["email"])
        print("user_info --->",user_info)
        request.data["end_user"] = user_info
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
