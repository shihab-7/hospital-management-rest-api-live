from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer
# Create your views here.

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # akhon url theke patient id diye akta patient koyta apointment niyesilo oita query korar jonno custom function banay niye value pass korar jay api a

    def get_queryset(self):
        queryset = super().get_queryset() #eita builtin thake get_queryset methode just edit kore nite hoy

        # query_params.get() link theke ana data object banay diye dey
        # print(self.request.query_params)

        patient_id = self.request.query_params.get('patient_id') # url theke deowa id self.request diye dhore store kora hoilo

        if patient_id:
            queryset = queryset.filter(patient_id = patient_id) # upore super() diye sob data niye eshe queryset a thaka data theke id diye filter kore niye queryset k override kore oi id er data return kore dibe r null hoile nicher return exicute hoye sob data return korbe 
        return queryset