from django.urls import path,include
from Admin import views

app_name="Admin"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('add/',views.add,name="add"),
    path('largest/',views.largest,name="largest"),
    path('calculator',views.calculator,name="calculator"),
    path('district/',views.district,name="district"),
    path('deldistrict/<int:id>',views.deldistrict,name='deldistrict'),
    path('eddistrict/<int:id>',views.eddistrict,name='eddistrict'),
    path('category/',views.category,name="category"),
    path('adminreg/',views.adminreg,name="adminreg"),
    path('deladmin/<int:id>',views.deladmin,name='deladmin'),
    path('place/',views.place,name="place"),
    path('pdelete/<int:id>',views.pdelete,name='pdelete'),
    path('brand/',views.brand,name="brand"),
    path('delbrand/<int:id>',views.delbrand,name='delbrand'),

    path('transportationtype/',views.transportationtype,name="transportationtype"),
    path('deletettype/<int:id>',views.deletettype,name="deletettype"),
    path('editttype/<int:id>',views.editttype,name="editttype"),
    path('subcategory/',views.subcategory,name='subcategory'),
    path('delsubcategory/<int:id>',views.delsubcategory,name='delsubcategory'),
    path('editsub/<int:id>',views.editsub,name='editsub'),
    path('EmergencyPass/',views.EmergencyPass,name='EmergencyPass'),
    path('acceptemergencypage/<int:id>',views.acceptemergencypage,name="acceptemergencypage"),
    path('rejectemergencypage/<int:id>',views.rejectemergencypage,name="rejectemergencypage"),

    path('viewrentrequests/',views.viewrentrequests,name='viewrentrequests'),
    path('passrequest/',views.passrequest,name='passrequest'),
    path('passrequestaccept/<int:id>',views.passrequestaccept,name="passrequestaccept"),
    path('passrequestreject/<int:id>',views.passrequestreject,name="passrequestreject"),

    path('rejectrentrequest/<int:id>',views.rejectrentrequest,name="rejectrentrequest"),
    
    path('cabrequest/',views.cabrequest,name='cabrequest'),
    path('cabreject/<int:id>',views.cabreject,name='cabreject'),
    path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('driver/',views.driver,name='driver'),
    path('verifydriver/<int:id>/<int:status>',views.verifydriver,name='verifydriver'),
    
    path('OurDrivers/',views.OurDrivers,name='OurDrivers'),

    path("rating/<int:mid>",views.rating,name="rating"),
    path("starrating/",views.starrating,name="starrating"),

    path('passrequestmail/',views.passrequestmail,name='passrequestmail'),
    path('rentvehicleemail/',views.rentvehicleemail,name='rentvehicleemail'),
    path('cabemail/',views.cabemail,name='cabemail'),
    
    path('logout/',views.logout,name='logout'),
]
