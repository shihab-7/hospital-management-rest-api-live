from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    # first name r last name dekhanor jonno custom function banay data ber kore niye ashte hobe
    list_display = ['first_name','last_name','mobile_no', 'image']

    # first name last name auto ei model a chole ashse modeladmin k inherrit korar jonno r er vitor user er sathe relation thakay amra direct function banay oigula access korte pari
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(Patient, PatientAdmin)