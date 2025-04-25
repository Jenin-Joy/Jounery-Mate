from django.shortcuts import render,redirect
from Driver.models import *
from User.models import *
# Create your views here.
def vehicle(request):
    if 'did' not in request.session:
        return redirect("Guest:login")
    vehicle=tbl_vehicle.objects.filter(driver=request.session['did'])
    if request.method == "POST":
        tbl_vehicle.objects.create(
            vehicle_number=request.POST.get("txt_number"),
            vehicle_count=request.POST.get("txt_count"),
            vehicle_photo=request.FILES.get("file_photo"),
            driver=tbl_driver.objects.get(id=request.session['did'])
        )
        return redirect("Driver:vehicle")
    else:
        return render(request,"Driver/Vehicle.html",{'vehicle':vehicle})

def delvehicle(request,id):
    if 'did' not in request.session:
        return redirect("Guest:login")
    tbl_vehicle.objects.get(id=id).delete()
    return redirect("Driver:vehicle")
    
def Homepage(request):
    if 'did' not in request.session:
        return redirect("Guest:login")
    return render(request,'Driver/Homepage.html')

def Myprofile(request):
    if 'did' not in request.session:
        return redirect("Guest:login")
    user=tbl_driver.objects.get(id=request.session["did"])
    return render(request,'Driver/Myprofile.html',{'user':user})

def Editprofile(request):
    if 'did' not in request.session:
        return redirect("Guest:login")
    b=tbl_driver.objects.get(id=request.session['did'])
    if request.method=="POST":
        b.driver_name=request.POST.get("driver_name")
        b.driver_email=request.POST.get("driver_email")
        b.driver_contact=request.POST.get("driver_contact")
        b.driver_address=request.POST.get("driver_address")
        b.save()
        return redirect("Driver:Myprofile")
    else:
        return render(request,'Driver/Editprofile.html',{'b':b})

def Changepassword(request):
    if 'did' not in request.session:
        return redirect("Guest:login")
    b=tbl_driver.objects.get(id=request.session['did'])
    olda=b.driver_password
    oldb= new=request.POST.get("user_old_pasword")
    new=request.POST.get("user_new_password")
    re=request.POST.get("re_type_password")
    if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.driver_password=request.POST.get("re_type_password")
                b.save()
                return render(request,"Driver/Myprofile.html",{'msg':"Profile Updated"})
            else:
                return render(request,"Driver/ChangePassword.html",{'msg':"Your Confirm Password is error"})
        else:
            return render(request,"Driver/ChangePassword.html",{'msg':"Your Old Password is error"})
    else:
        return render(request,"Driver/ChangePassword.html")

def viewassigning(request, id):
    if 'did' not in request.session:
        return redirect("Guest:login")
    cab = tbl_cabassign.objects.filter(vehicle=id)
    return render(request,"Driver/ViewAssign.html",{"cab":cab})

def Feedback(request):
    if 'did' not in request.session:
        return redirect("Guest:login")
    if request.method == "POST":
        tbl_feedback.objects.create(
            feedback_content=request.POST.get("txt_feedback"),
            driver=tbl_driver.objects.get(id=request.session["did"])
        )
        return render(request,'Driver/Feedback.html',{"msg":"Feedback Send Sucessfully..."})
    return render(request,'Driver/Feedback.html')