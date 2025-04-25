from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*

# Create your views here.
def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        admincount=tbl_adminreg.objects.filter(admin_email=email,admin_password=password).count()
        drivercount=tbl_driver.objects.filter(driver_email=email,driver_password=password).count()
        employeecount=tbl_employee.objects.filter(employee_email=email,employee_password=password).count()
        if admincount>0:
            admin=tbl_adminreg.objects.get(admin_email=email,admin_password=password)
            request.session["aid"]=admin.id
            return redirect("Admin:homepage")
        elif drivercount>0:
            driver=tbl_driver.objects.get(driver_email=email,driver_password=password)
            if driver.driver_status==0:
                return render(request,'Guest/Login.html',{"msg":"Wait for Admin Approval"})
            elif driver.driver_status==2:
                return render(request,'Guest/Login.html',{"msg":"Rejected by Admin"})
            else:
                request.session["did"]=driver.id
                return redirect("Driver:Homepage")
        elif employeecount>0:
            employee=tbl_employee.objects.get(employee_email=email,employee_password=password)
            request.session["eid"]=employee.id
            return redirect("User:Homepage")
        else:
            return render(request,'Guest/Login.html')

    else:
        return render(request,'Guest/Login.html')

def Registration(request):
    dis=tbl_district.objects.all()
    a=tbl_reg.objects.all()
    if request.method=="POST":
        pl=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_reg.objects.create(user_name=request.POST.get("txt_name"),
        user_email=request.POST.get("txt_email"),
        user_contact=request.POST.get("txt_contact"),
        user_password=request.POST.get("txt_password"),
        user_address=request.POST.get("txt_address"),
        user_photo=request.FILES.get("file_photo"),place=pl)
        return redirect("Guest:login")
    else:
        return render(request,'Guest/Registration.html',{'result':dis,'r':a})

def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})

def Employee(request):
    dis=tbl_district.objects.all()
    t=tbl_transportationtype.objects.all()
    if request.method=="POST":
        pl=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tr=tbl_transportationtype.objects.get(id=request.POST.get("sel_transportation"))
        tbl_employee.objects.create(employee_name=request.POST.get("txt_name"),
        employee_email=request.POST.get("txt_email"),
        employee_contact=request.POST.get("txt_contact"),
        employee_address=request.POST.get("txt_address"),
        employee_photo=request.FILES.get("file_photo"),
        employee_proof=request.FILES.get("file_proof"),
        employee_password=request.POST.get("txt_password"),
        place=pl,
        transportationtype=tr,)
        return redirect("Guest:login")
    else:
        return render(request,'Guest/Employee.html',{'result':dis,'t':t})
    
def Driver(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        pl=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_driver.objects.create(driver_name=request.POST.get("txt_name"),
        driver_email=request.POST.get("txt_email"),
        driver_contact=request.POST.get("txt_contact"),
        driver_password=request.POST.get("password"),
        driver_address=request.POST.get("txt_address"),
        driver_photo=request.FILES.get("file_photo"),
        driver_proof=request.FILES.get("file_proof"),
        driver_license=request.FILES.get("file_license"),
        place=pl)
        return redirect("Guest:login")
    else:
        return render(request,'Guest/Driver.html',{'result':dis,})

def index(request):
    return render(request,"Guest/index.html")