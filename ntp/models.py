from django.db import models
from django.contrib.auth.models import User
from facility.models import Township, Facility
# Create your models here.



class Notify(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    sex=models.CharField(max_length=200, choices=[ ('M','M'),('F', 'F') ])
    age=models.PositiveIntegerField()
    address=models.CharField(max_length=200)
    township=models.ForeignKey(Township, on_delete=models.CASCADE, related_name="notify")
    name_of_treatment_center=models.ForeignKey(Facility, on_delete=models.CASCADE, related_name="notify")
    registration_group=models.PositiveIntegerField()
    specimen_collected_date=models.DateField(blank=True, null=True)
    x_pert_result=models.CharField(max_length=5, choices=[ ('N','N'),('RR', 'RR'),('TI','TI')], null=True, blank=True)
    x_pert_result_date=models.DateField(blank=True, null=True)
    culture_result=models.CharField(max_length=10,blank=True)
    dst_result=models.CharField(max_length=10, blank=True)
    died_before_treatment=models.BooleanField(default=False,blank=True, null=True)
    died_before_treatment_date=models.DateField(blank=True, null=True)
    sld_treatment_at_private_date=models.DateField(blank=True, null=True)
    refused_date=models.DateField(blank=True, null=True)
    lfu_date=models.DateField(blank=True, null=True)
    mdr_treatment_start_date=models.DateField(blank=True, null=True)
    mdr_treatment_registration_no=models.CharField(max_length=10, blank=True, null=True)
    remark=models.CharField(max_length=200, blank=True, null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE, related_name="notify" )
    created_at=models.DateField(auto_now_add=True )
    updated_at=models.DateField(auto_now=True )
