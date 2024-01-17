from rest_framework import serializers
from .models import Doctor, Specialization,Designation,AvailableTime,Review

class DoctorSerializer(serializers.ModelSerializer):

    # string related fields use korle visualize korte easy hoileo rest framework a data edit korte raw format use korte hoy tai html format a edit korte chaile string related field use korar jabe na

    user = serializers.StringRelatedField(many=False) 
    designation = serializers.StringRelatedField(many= True)
    specialization = serializers.StringRelatedField(many= True)
    available_time = serializers.StringRelatedField(many= True)

    class Meta:
        model = Doctor
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = '__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'