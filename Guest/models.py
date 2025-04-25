from django.db import models
from Admin.models import *

class tbl_reg(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to='Assets/user/photo/')
    
class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_email=models.CharField(max_length=50)
    employee_contact=models.CharField(max_length=50)
    employee_address=models.CharField(max_length=100)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    employee_photo=models.FileField(upload_to='Assets/user/photo/')
    employee_proof=models.FileField(upload_to='Assets/user/photo/')
    employee_password=models.CharField(max_length=50)
    employee_status=models.IntegerField(default=0)
    transportationtype=models.ForeignKey(tbl_transportationtype,on_delete=models.CASCADE)

class tbl_driver(models.Model):
    driver_name=models.CharField(max_length=50)
    driver_email=models.CharField(max_length=50)
    driver_contact=models.CharField(max_length=50)
    driver_address=models.CharField(max_length=100)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    driver_photo=models.FileField(upload_to='Assets/user/photo/')
    driver_proof=models.FileField(upload_to='Assets/user/photo/')
    driver_license=models.FileField(upload_to='Assets/user/photo/')
    driver_password=models.CharField(max_length=50)
    driver_status=models.IntegerField(default=0)

class tbl_vehicle(models.Model):
    vehicle_number=models.CharField(max_length=50)
    vehicle_count=models.CharField(max_length=50)
    vehicle_photo=models.FileField(upload_to="Assets/user/photo/")
    driver=models.ForeignKey(tbl_driver,on_delete=models.CASCADE)

class tbl_cabassign(models.Model):
    cabassign_date=models.DateField(auto_now_add=True)
    employee=models.ForeignKey(tbl_employee,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE, null=True)
    cabassign_amount=models.CharField(max_length=50)
    cabassign_status=models.IntegerField(default=0)
    cabassign_startdate=models.CharField(max_length=50)
    cabassign_enddate=models.CharField(max_length=50)
    email_status = models.IntegerField(default=0)