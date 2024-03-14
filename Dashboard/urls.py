
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
    path('Report_Payment/',views.Report4,name="Report_Payment"),
    path('Report_Employee/',views.Report5,name="Report_Employee"),
    path('Report_Salary/',views.Report6,name="Report_Salary"),

    path('Record_Event/<int:pk>', views.Record_Event, name="Record_Event"),
    path('record/<int:pk>', views.Customer_Record, name="record"),
    path('Record_Venue/<int:pk>', views.Record_Venue, name="Record_Venue"),
    path('Record_Payment/<int:pk>', views.Record_Payment, name="Record_Payment"),
      path('Record_Employee/<int:pk>', views.Record_Employee, name="Record_Employee"),
       path('Record_Salary/<int:pk>', views.Record_Salary, name="Record_Salary"),

    path('Delete_Event/<int:pk>', views.Delete_Event, name="Delete_Event"),
    path('Delete_record/<int:pk>', views.Delete_record, name="Delete_record"),
    path('Delete_Venue/<int:pk>', views.Delete_Venue, name="Delete_Venue"),
    path('Delete_Payment/<int:pk>', views.Delete_Payment, name="Delete_Payment"),
     path('Delete_Employee/<int:pk>', views.Delete_Employee, name="Delete_Employee"),
      path('Delete_Salary/<int:pk>', views.Delete_Salary, name="Delete_Salary"),

    # path('Employee_register/',views.Employee,name="Employee_register")
]