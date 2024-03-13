
from django.urls import path
from . import views
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('event_register/',views.Event_register,name="Event_register"),
    path('register_Customer/',views.Register_Customer,name="Register_Customer"),
    path('venue_register/',views.Venue_register,name="Venue_register"),
    path('Payment_register/',views.Payment_register, name="Payment_register"),
    path('Employee_register/',views.Employee_register,name="Employee_register"),
    path('Salary_register/',views.Salary_register,name="Salary_register"),
    path('Report_tabel1/',views.Report,name="Report_tabel1"),
    path('Report_Customer/',views.Report2,name="Report_Customer"),
    path('Report_Venue/',views.Report3,name="Report_Venue"),
    path('Report_Employee/',views.Report5,name="Report_Employee"),
    path('Report_Salary/',views.Report6,name="Report_Salary"),
    path('record/<int:pk>', views.Customer_Record, name="record"),
    path('Delete_record/<int:pk>', views.Delete_record, name="Delete_record")

    # path('Employee_register/',views.Employee,name="Employee_register")
]