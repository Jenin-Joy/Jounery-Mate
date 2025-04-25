from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail

from datetime import date

# Create your views here.
def add(request):
    if request.method=="POST" :
        a=int(request.POST.get("number1"))
        b=int(request.POST.get("number2"))
        c=a+b
        return render(request,"Admin/Add.html",{'result':c})
    else:
        return render(request,"Admin/Add.html")

def largest(request):
    if request.method=="POST" :
        a=int(request.POST.get("number1"))
        b=int(request.POST.get("number2"))
        if a>b :
            return render(request,"Admin/Add.html",{'result':a})    
        else:
            return render(request,"Admin/Largest.html",{'result':b})
    else:
        return render(request,"Admin/Largest.html")

def calculator(request):
    if request.method=="POST" :
        a=int(request.POST.get("number1"))
        b=int(request.POST.get("number2"))
        btn=request.POST.get("add")
        if btn=='+':
            c=a+b
            return render(request,"Admin/Calculator.html",{'result':c})

        elif btn=='-':
            c=a-b
            return render(request,"Admin/Calculator.html",{'result':c})
        elif btn=='*':
            c=a*b
            return render(request,"Admin/Calculator.html",{'result':c})
        elif btn=='/':
            c=a/b
            return render(request,"Admin/Calculator.html",{'result':c})
    else:
        return render(request,"Admin/Calculator.html")

def homepage(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    passrequest = tbl_passrequest.objects.filter(passrequest_status=3,passrequest_enddate=date.today(),email_status=0)
    rent = tbl_rentvehicle.objects.filter(rentvehicle_status=3,rentvehicle_enddate=date.today(),email_status=0)
    cab = tbl_cabassign.objects.filter(cabassign_status=3,cabassign_enddate=date.today(),email_status=0)

    data=tbl_adminreg.objects.get(id=request.session['aid'])
    empcount=tbl_employee.objects.all().count()
    drivercount=tbl_driver.objects.all().count()
    compcount=tbl_complaint.objects.all().count()
    rcount=tbl_complaint.objects.filter(complaint_status=1).count()
    return render(request,"Admin/HomePage.html",{'data4':rcount,'data3':compcount,'passrequest':passrequest,'rent':rent,'cab':cab,'data':data,'data1':empcount,'data2':drivercount})

def passrequestmail(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    expiring_passes = tbl_passrequest.objects.filter(passrequest_status=3,passrequest_enddate=date.today(),email_status=0)
    for req in expiring_passes:
        subject = "Your Pass Will Expire Today"
        message = (
            f"Dear {req.employee.employee_name},\n\n"
            f"Your travel pass from {req.passrequest_fromplace.place_name} to {req.passrequest_toplace.place_name} "
            f"is set to expire today ({req.passrequest_enddate}).\n\n"
            "Please renew it as soon as possible to avoid interruption.\n\n"
            "Regards,\n"
            "Your Travel Desk"
        )
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [req.employee.employee_email],
            fail_silently=False
        )
        req.email_status = 1
        req.save()
    return render(request,"Admin/HomePage.html",{'msg':'Mail Send'})

def rentvehicleemail(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    rents = tbl_rentvehicle.objects.filter(rentvehicle_status=3,rentvehicle_enddate=date.today(),email_status=0)
    for rent in rents:
        subject = "Your Vehicle Rent Period Ends Today"
        message = (
            f"Dear {rent.employee.employee_name},\n\n"
            f"Your rented vehicle ({rent.rentvehicle_number}) period ends today ({rent.rentvehicle_enddate}).\n"
            f"Total Amount: {rent.rentvehicle_amount}\n\n"
            "Please take the necessary steps for return or renewal.\n\n"
            "Regards,\n"
            "Your Travel Desk"
        )
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [rent.employee.employee_email],
            fail_silently=False
        )
        rent.email_status = 1
        rent.save()
    return render(request,"Admin/HomePage.html",{'msg':'Mail Send'})

def cabemail(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cabs = tbl_cabassign.objects.filter(cabassign_status=3,cabassign_enddate=date.today(),email_status=0)
    for cab in cabs:
        subject = "Cab Assignment Expiry Notification"
        message = (
            f"Dear {cab.employee.employee_name},\n\n"
            f"Your cab assignment (Vehicle: {cab.vehicle}) is expiring today ({cab.cabassign_enddate}).\n"
            f"Total Amount: {cab.cabassign_amount}\n\n"
            "Please take action if renewal is needed.\n\n"
            "Best regards,\n"
            "Transport Desk"
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [cab.employee.employee_email],
            fail_silently=False
        )
        cab.email_status = 1
        cab.save()
    return render(request,"Admin/HomePage.html",{'msg':'Mail Send'})

def district(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    dis=tbl_district.objects.all()
    if request.method=="POST":
       district=request.POST.get("district")
       tbl_district.objects.create(district_name=district)
       return render(request,'Admin/District.html',{'dis':dis})
    else:
        return render(request,'Admin/District.html',{'dis':dis})


def deldistrict(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")

def eddistrict(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    dist=tbl_district.objects.get(id=id)
    if request.method=="POST":
      dist.district_name=request.POST.get("district")
      dist.save()
      return redirect("Admin:district")
    else:
        return render(request,'Admin/District.html',{'distr':dist})
    
def category(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cat=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("category")
        tbl_category.objects.create(category_name=category)
        return render(request,'Admin/Category.html',{'cat':cat})
    else:
        return render(request,'Admin/Category.html')        


def adminreg(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    rege=tbl_adminreg.objects.all()
    if request.method=="POST":
       name=request.POST.get("name")
       email=request.POST.get("email")
       password=request.POST.get("password")
       
       tbl_adminreg.objects.create(admin_name=name,admin_email=email,admin_password=password)
       
       return render(request,'Admin/AdminReg.html',{'reg':rege})
    else:
        return render(request,'Admin/AdminReg.html',{'reg':rege})


def viewrentrequests(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    data=tbl_rentvehicle.objects.all()
    if request.method=="POST":
        vehiclerequest = tbl_rentvehicle.objects.get(id=request.POST.get("id"))
        vehiclerequest.rentvehicle_number=request.POST.get("vehicle_number")
        vehiclerequest.rentvehicle_amount=request.POST.get("amount")
        vehiclerequest.rentvehicle_status=1
        vehiclerequest.save()
        return redirect("Admin:viewrentrequests")
    return render(request,'Admin/ViewRentRequests.html',{'data':data})

def rejectrentrequest(request, id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    req = tbl_rentvehicle.objects.get(id=id)
    req.rentvehicle_status=2; req.save()
    return redirect("Admin:viewrentrequests")


def deladmin(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_adminreg.objects.get(id=id).delete()
    return redirect("Admin:adminreg")

def place(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    dis=tbl_district.objects.all()
    pl=tbl_place.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("sel_dist"))
        tbl_place.objects.create(place_name=request.POST.get("txt_dis"),district=dist)
        return redirect("Admin:place")
    else:
        return render(request,'Admin/place.html',{'result':dis,'r':pl}) 

def pdelete(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")

def brand(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    br=tbl_brand.objects.all()
    if request.method=="POST":
        brand=request.POST.get("brand")
        tbl_brand.objects.create(brand_name=brand)
        return render(request,'Admin/Brand.html',{'br':br})
    else:
        return render(request,'Admin/Brand.html',{'br':br})

def delbrand(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_brand.objects.get(id=id).delete()
    return redirect("Admin:brand")

def subcategory(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cat=tbl_category.objects.all()
    subcat=tbl_subcategory.objects.all()
    if request.method=="POST":
        cat=tbl_category.objects.get(id=request.POST.get("sel_cat"))
        tbl_subcategory.object.create(subcategory_name=request.POST.get("subcat"),category=cat)
        return redirect("Admin:subcategory")
    else:
        return render(request,'Admin/subcategory.html',{'subcat':subcat,'cat':cat})

def delsubcategory(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory")


def editsub(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cate=tbl_category.objects.all()
    kar=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
      kar.subcategory_name=request.POST.get("subcat")
      kar.save()
      return redirect("Admin:subcategory")
    else:
      return render(request,'Admin/subcategory.html',{'d':kar,'cat':cate})



def transportationtype(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    transportationtype=tbl_transportationtype.objects.all()
    if request.method=="POST":
       ttype=request.POST.get("transportationtype")
       tbl_transportationtype.objects.create(transportationtype_name=ttype)
       return render(request,'Admin/TransportationType.html',{'transportationtype':transportationtype})
    else:
        return render(request,'Admin/TransportationType.html',{'transportationtype':transportationtype})

def deletettype(request, id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tbl_transportationtype.objects.get(id=id).delete()
    return redirect("Admin:transportationtype")

def editttype(request, id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    tran = tbl_transportationtype.objects.get(id=id)
    if request.method == "POST":
        tran.transportationtype_name = request.POST.get("transportationtype")
        tran.save()
        return redirect("Admin:transportationtype")
    return render(request, "Admin/TransportationType.html",{"ttype":tran})

def district(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    dis=tbl_district.objects.all()
    if request.method=="POST":
       district=request.POST.get("district")
       tbl_district.objects.create(district_name=district)
       return render(request,'Admin/District.html',{'dis':dis})
    else:
        return render(request,'Admin/District.html',{'dis':dis})
    
def EmergencyPass(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    district = tbl_district.objects.all()
    empass = tbl_emergencypass.objects.filter(employee=request.session["eid"])
    if request.method == "POST":
        tbl_emergencypass.objects.create(
            from_place = tbl_place.objects.get(id=request.POST.get("txt_fplace")),
            to_place = tbl_place.objects.get(id=request.POST.get("txt_tplace")),
            employee = tbl_employee.objects.get(id=request.session["eid"])
        )
        return render(request,'Admin/ViewEmergencyPass.html',{"msg":"Emergency Pass Request Send Sucessfully..."})
    return render(request,'Admin/ViewEmergencyPass.html',{"district":district,"empass":empass})

def acceptemergencypage(request,id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    if request.method == "POST":
        empassdata=tbl_emergencypass.objects.get(id=id)
        empassdata.emergencypass_amount=request.POST.get('payment')
        empassdata.emergencypass_status=1
        empassdata.save()
        return render(request,'Admin/ViewEmergencyPass.html',{'msg':"Amount Added"})
    else:
        return render(request,'Admin/EmergencyPassPayment.html')
    
def rejectemergencypage(request, id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    empassdata=tbl_emergencypass.objects.get(id=id)
    empassdata.emergencypass_status=2
    empassdata.save()
    return redirect("Admin:EmergencyPass")

def passrequest(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    passreq = tbl_passrequest.objects.all()
    return render(request, "Admin/ViewPassRequest.html",{"passreq":passreq})

def passrequestaccept(request, id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    if request.method == "POST":
        passreq=tbl_passrequest.objects.get(id=id)
        passreq.passrequest_amount=request.POST.get('payment')
        passreq.passrequest_status=1
        passreq.save()
        return render(request,'Admin/ViewPassRequest.html',{'msg':"Amount Added"})
    else:
        return render(request,'Admin/EmergencyPassPayment.html')

def passrequestreject(request, id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    empassdata=tbl_passrequest.objects.get(id=id)
    empassdata.passrequest_status=2
    empassdata.save()
    return redirect("Admin:passrequest")

def cabrequest(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cabreq = tbl_cabassign.objects.all()
    cab = tbl_vehicle.objects.all()
    cabid = []    
    emp_dis = []
    for i in cab:
        cabcount = tbl_cabassign.objects.filter(vehicle=i.id).count()
        if int(i.vehicle_count) > cabcount:
            cabid.append(i.id)
    for c in cabreq:
        emp_dis.append(c.employee.place.district.id)
    cab = tbl_vehicle.objects.filter(id__in=cabid,driver__place__district__in=emp_dis,driver__driver_status=1)
    if request.method == "POST":
        cabreq = tbl_cabassign.objects.get(id=request.POST.get("id"))
        cabreq.vehicle = tbl_vehicle.objects.get(id=request.POST.get("vehicle"))
        cabreq.cabassign_amount = request.POST.get("amount")
        cabreq.cabassign_status = 1
        cabreq.save()
        return redirect("Admin:cabrequest")
    return render(request, "Admin/ViewCab_request.html",{"cabreq":cabreq,"cab":cab})

def cabreject(request, id):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    cabreq = tbl_cabassign.objects.get(id=id)
    cabreq.cabassign_status = 2
    cabreq.save()
    return redirect("Admin:cabrequest")

def viewcomplaint(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    complaint = tbl_complaint.objects.all()
    if request.method == "POST":
        com = tbl_complaint.objects.get(id=request.POST.get("id"))
        com.complaint_reply = request.POST.get("reply")
        com.complaint_status = 1
        com.save()
        return redirect("Admin:viewcomplaint")
    return render(request, "Admin/ViewComplaint.html",{"complaint":complaint})

def viewfeedback(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    employeefeedback = tbl_feedback.objects.filter(employee__isnull=False)
    driverfeedback = tbl_feedback.objects.filter(driver__isnull=False)
    return render(request, "Admin/ViewFeedback.html",{"employeefeedback":employeefeedback,"driverfeedback":driverfeedback})

def driver(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    newdriver = tbl_driver.objects.filter(driver_status=0)
    verifieddrive = tbl_driver.objects.filter(driver_status=1)
    rejecteddrive = tbl_driver.objects.filter(driver_status=2)
    return render(request, "Admin/Driver.html",{"newdriver":newdriver,"verifieddriver":verifieddrive,"rejecteddriver":rejecteddrive})
    
def verifydriver(request, id, status):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    driver = tbl_driver.objects.get(id=id)
    driver.driver_status = status
    driver.save()
    return redirect("Admin:driver")

def OurDrivers(request):
    if 'aid' not in request.session:
        return redirect("Guest:login")
    driver = tbl_driver.objects.filter(driver_status=1)
    return render(request, "Admin/OurDrivers.html",{"driver":driver})

def rating(request,mid):
    if 'aid' not in request.session:
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
        return render(request,"Admin/DriverRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"Admin/DriverRating.html",{'mid':mid})

def starrating(request):
    if 'aid' not in request.session:
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

def logout(request):
    del request.session["aid"]
    return redirect("Guest:login")