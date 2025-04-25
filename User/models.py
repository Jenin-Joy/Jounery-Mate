from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_rentvehicle(models.Model):
    rentvehicle_number=models.CharField(max_length=50)
    employee=models.ForeignKey(tbl_employee,on_delete=models.CASCADE)
    rentvehicle_amount=models.CharField(max_length=50)
    rentvehicle_status=models.IntegerField(default=0)
    rentvehicle_startdate=models.CharField(max_length=50)
    rentvehicle_enddate=models.CharField(max_length=50)
    rentvehicle_proof=models.FileField(upload_to="Assets/Rentvehicle/Proof")
    email_status = models.IntegerField(default=0)

class tbl_passrequest(models.Model):
    passrequest_date=models.DateField(auto_now_add=True)
    employee=models.ForeignKey(tbl_employee,on_delete=models.CASCADE)
    passrequest_amount=models.CharField(max_length=50)
    passrequest_startdate=models.DateField()
    passrequest_enddate=models.DateField()
    passrequest_status=models.IntegerField(default=0)
    passrequest_fromplace=models.ForeignKey(tbl_place, on_delete=models.CASCADE, related_name="passrequest_fromplace")
    passrequest_toplace=models.ForeignKey(tbl_place, on_delete=models.CASCADE, related_name="passrequest_toplace")
    email_status = models.IntegerField(default=0)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50)
    complaint_status=models.IntegerField(default=0)
    employee=models.ForeignKey(tbl_employee,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    employee=models.ForeignKey(tbl_employee,on_delete=models.CASCADE, null=True)
    driver=models.ForeignKey(tbl_driver,on_delete=models.CASCADE, null=True)

class tbl_emergencypass(models.Model):
    employee=models.ForeignKey(tbl_employee,on_delete=models.CASCADE)
    emergencypass_amount=models.CharField(max_length=50)
    from_place=models.ForeignKey(tbl_place, on_delete=models.CASCADE, related_name="from_place")
    to_place=models.ForeignKey(tbl_place, on_delete=models.CASCADE, related_name="to_place")
    emergencypass_validity=models.DateField(auto_now_add=True)
    emergencypass_status=models.IntegerField(default=0)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_review=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)
    employee=models.ForeignKey(tbl_employee,on_delete=models.CASCADE)
    driver=models.ForeignKey(tbl_driver,on_delete=models.CASCADE)

