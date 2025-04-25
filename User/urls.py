from django.urls import path, include
from User import views
app_name="User"

urlpatterns=[
    path('Homepage/',views.homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('Complaint/',views.Complaint,name='Complaint'),
    path('EmergencyPass/',views.EmergencyPass,name='EmergencyPass'),
    path('Feedback/',views.Feedback,name='Feedback'),
    path('PassRequest/',views.PassRequest,name='PassRequest'),
    path('RentVehicle/',views.RentVehicle,name='RentVehicle'),
    path('viewrentrequests/',views.viewrentrequests,name='viewrentrequests'),
    path('MyComplaint/',views.MyComplaint,name='MyComplaint'),
    path('MyCab/',views.MyCab,name='MyCab'),
    path('MyPassRequest/',views.MyPassRequest,name='MyPassRequest'),

    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path("passpayment/<int:id>",views.passpayment,name="passpayment"),
    path("cabpayment/<int:id>",views.cabpayment,name="cabpayment"),

    path('viewpass/<int:id>',views.viewpass, name='viewpass'),
    path('ppass/<int:id>',views.ppass, name='ppass'),

    path("rentpayment/<int:id>",views.rentpayment,name="rentpayment"),

    path("rating/<int:mid>",views.rating,name="rating"),
    path("ajaxstar/",views.ajaxstar,name="ajaxstar"),
    path("starrating/",views.starrating,name="starrating"),
]