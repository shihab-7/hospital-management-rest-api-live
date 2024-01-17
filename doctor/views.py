from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, AvailableTime,Designation,Specialization,Review
from .serializers import DoctorSerializer, DesignationSerializer,SpecializationSerializer,AvailableTimeSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters, pagination
# Create your views here.

#  akhon doctor list tate ak ak page a koyekjon kore doctor rekhe multiple page banor jonno pagination use kore akta class banano hoise
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # ak page a koyta item thakbe oi number ta
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    search_fields = ['user__first_name', 'user__email','designation__name','specialization__name']

# akhon prottek doctor kon kon time available thake oita filter korar jonno class
class AvailableTimeForSpeceficDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get('doctor_id') # eita link theke data niye ashe jemon 'randomLink/?doctor_id=1'
        if doctor_id:
            return query_set.filter(doctor = doctor_id) # doctor er sathe availabletime er many to many relation thakay availabletime er vitor auto doctor nam er akta attribute toiri hoye thake jeta query_set diye access kora hoise

class AvailableTimeViewSet(viewsets.ModelViewSet):
    # authenticated user sara kew r ei api ta access korte parbe na
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all().order_by('id')
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpeceficDoctor]

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        doctor_id = self.request.query_params.get('doctor_id')

        if doctor_id:
            queryset = queryset.filter(doctor=doctor_id)
        return queryset
    


