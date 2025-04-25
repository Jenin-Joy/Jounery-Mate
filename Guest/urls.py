from django.urls import path, include
from Guest import views
app_name="Guest"

urlpatterns=[
    path('login/',views.login,name='login'),
    path('Registration/',views.Registration,name='Registration'),
    path('Ajaxplace/',views.Ajaxplace,name='Ajaxplace'),
    path('Employee/',views.Employee,name='Employee'),
    path('Driver/',views.Driver,name='Driver'),

    path('',views.index,name='index'),

 ]