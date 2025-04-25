from django.urls import path, include
from Driver import views
app_name="Driver"

urlpatterns=[
    path('Homepage/',views.Homepage,name='Homepage'),
    path('vehicle/',views.vehicle,name='vehicle'),
    path('delvehicle/<int:id>',views.delvehicle,name='delvehicle'),

    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),

    path('Feedback/',views.Feedback,name='Feedback'),
    path('viewassigning/<int:id>',views.viewassigning,name='viewassigning'),
    
]