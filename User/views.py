from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from Admin.models import *
from datetime import date
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse

def homepage(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    return render(request,'User/Homepage.html',{'homepage':homepage})

def Myprofile(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    user=tbl_employee.objects.get(id=request.session["eid"])
    return render(request,'User/Myprofile.html',{'user':user})

def Editprofile(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    b=tbl_employee.objects.get(id=request.session['eid'])
    if request.method=="POST":
        b.employee_name=request.POST.get("employee_name")
        b.employee_email=request.POST.get("employee_email")
        b.employee_contact=request.POST.get("employee_contact")
        b.employee_address=request.POST.get("employee_address")
        b.save()
        return redirect("User:Myprofile")
    else:
        return render(request,'User/Editprofile.html',{'b':b})

def Changepassword(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    b=tbl_employee.objects.get(id=request.session['eid'])
    olda=b.employee_password
    oldb= new=request.POST.get("user_old_pasword")
    new=request.POST.get("user_new_password")
    re=request.POST.get("re_type_password")
    if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.employee_password=request.POST.get("re_type_password")
                b.save()
                return render(request,"User/Myprofile.html",{'msg':"Profile Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg':"Your Confirm Password is error"})
        else:
            return render(request,"User/ChangePassword.html",{'msg':"Your Old Password is error"})
    else:
        return render(request,"User/ChangePassword.html")

def Complaint(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    if request.method == "POST":
        tbl_complaint.objects.create(
            complaint_title=request.POST.get("txt_subject"),
            complaint_content=request.POST.get("txt_content"),
            employee=tbl_employee.objects.get(id=request.session["eid"])
        )
        return redirect("User:MyComplaint")
    return render(request,'User/Complaint.html')

def EmergencyPass(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    district = tbl_district.objects.all()
    empass = tbl_emergencypass.objects.filter(employee=request.session["eid"])
    if request.method == "POST":
        tbl_emergencypass.objects.create(
            from_place = tbl_place.objects.get(id=request.POST.get("txt_fplace")),
            to_place = tbl_place.objects.get(id=request.POST.get("txt_tplace")),
            employee = tbl_employee.objects.get(id=request.session["eid"])
        )
        return render(request,'User/EmergencyPass.html',{"msg":"Emergency Pass Request Send Sucessfully..."})
    return render(request,'User/EmergencyPass.html',{"district":district,"empass":empass})

def Feedback(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    if request.method == "POST":
        tbl_feedback.objects.create(
            feedback_content=request.POST.get("txt_feedback"),
            employee=tbl_employee.objects.get(id=request.session["eid"])
        )
        return render(request,'User/Feedback.html',{"msg":"Feedback Send Sucessfully..."})
    return render(request,'User/Feedback.html')

def PassRequest(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    district = tbl_district.objects.all()
    passreq = tbl_passrequest.objects.filter(employee=request.session["eid"])
    if request.method == "POST":
        today = date.today()
        one_month_later = today + relativedelta(months=1)
        tbl_passrequest.objects.create(
            employee = tbl_employee.objects.get(id=request.session["eid"]),
            passrequest_startdate=today,
            passrequest_enddate=one_month_later,
            passrequest_fromplace=tbl_place.objects.get(id=request.POST.get("txt_fplace")),
            passrequest_toplace=tbl_place.objects.get(id=request.POST.get("txt_tplace"))
        )
        return render(request,'User/PassRequest.html',{"msg":"Pass Request Send Successfully"})
    return render(request,'User/PassRequest.html',{"district":district,"passreq":passreq})

def RentVehicle(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    vhc=tbl_rentvehicle.objects.all()
    userid=tbl_employee.objects.get(id=request.session['eid'])
    if request.method=="POST":
        fromdate=request.POST.get("txt_fromdate")
        todate=request.POST.get('txt_todate')
        proof=request.FILES.get('file_photo')
        tbl_rentvehicle.objects.create(rentvehicle_startdate=fromdate,
                                       rentvehicle_enddate=todate,
                                       rentvehicle_proof=proof,
                                       employee=userid)
        return render(request,'User/RentVehicle.html',{'msg':"Request Send"})
    else:
        return render(request,'User/RentVehicle.html')

def viewrentrequests(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    data=tbl_rentvehicle.objects.filter(employee=request.session['eid'])
    return render(request,'User/ViewRentRequests.html',{'data':data})

def MyComplaint(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    complaint = tbl_complaint.objects.filter(employee=request.session["eid"])    
    return render(request,'User/MyComplaint.html',{"complaint":complaint})

def MyCab(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    cab = tbl_cabassign.objects.filter(employee=request.session['eid'])
    if request.method == "POST":
        tbl_cabassign.objects.create(
            cabassign_startdate=request.POST.get("txt_startdate"),
            cabassign_enddate=request.POST.get("txt_enddate"),
            employee=tbl_employee.objects.get(id=request.session['eid'])
        )
        return redirect("User:MyCab")
    return render(request,'User/MyCab.html',{'cab':cab})

def cabpayment(request, id):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    cab = tbl_cabassign.objects.get(id=id)
    amount = cab.cabassign_amount
    if request.method == "POST":
        cab.cabassign_status = 3
        cab.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"amount":amount})

def MyPassRequest(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    return render(request,'User/MyPassRequest.html')

def payment(request, id):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    emp = tbl_emergencypass.objects.get(id=id)
    amount = emp.emergencypass_amount
    if request.method == "POST":
        emp.emergencypass_status = 3
        emp.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"amount":amount})
    
def passpayment(request, id):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    passreq = tbl_passrequest.objects.get(id=id)
    amount = passreq.passrequest_amount
    if request.method == "POST":
        passreq.passrequest_status = 3
        passreq.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"amount":amount})

def loader(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    return render(request,"User/Loader.html")

def paymentsuc(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    return render(request,"User/Paymentsuc.html")

def viewpass(request, id):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    emp = tbl_emergencypass.objects.get(id=id,emergencypass_status=3)
    return render(request,"User/ViewPass.html",{"data":emp})

def ppass(request, id):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    emp = tbl_passrequest.objects.get(id=id,passrequest_status=3)
    return render(request,"User/ViewPass.html",{"pdata":emp})

def rentpayment(request, id):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    rentrequest = tbl_rentvehicle.objects.get(id=id)
    amount = rentrequest.rentvehicle_amount
    if request.method == "POST":
        rentrequest.rentvehicle_status = 3
        rentrequest.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"amount":amount})

def rating(request,mid):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(driver=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(driver=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(employee=tbl_employee.objects.get(id=request.session['eid']),user_review=user_review,rating_data=rating_data,driver=tbl_driver.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(driver=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    if 'eid' not in request.session:
        return redirect("Guest:login")
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(driver=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(driver=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)