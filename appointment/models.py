from django.db import models
from doctor.models import Doctor, AvailableTime
from patient.models import Patient

# Create your models here.

APPOINTMENT_STATUS =[
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]

APPOINTMENT_TYPE = [
    ('Offline','Offline'),
    ('Online','Online'),
]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(max_length=20, choices= APPOINTMENT_TYPE)
    appointment_status = models.CharField(max_length=20, choices= APPOINTMENT_STATUS, default= 'Pending')
    symptom = models.TextField()

    # time = models.OneToOneField(AvailableTime, on_delete=models.CASCADE) eita use korle ak time multiple user nite parbe na
    
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE) # foreign key one to many relation build korate ak time multiple user nite parbe
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f'Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}'