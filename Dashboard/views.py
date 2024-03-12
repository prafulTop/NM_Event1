from django.shortcuts import render,redirect
from .models import Event
from .models import Customer
from .models import Venue
from .models import Payment
from .models import Event
from .models import Employee
from .models import Salary




from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'homepage.html',)

def Event_register(request):
    
    if request.method == 'POST':
        name = request.POST.get('event_name')
        date = request.POST.get('event_date')
        time = request.POST.get('event_time')
        location = request.POST.get('event_location')
        requirement = request.POST.get('event_requirement')
        themes = request.POST.get('event_themes')

        # Perform validation if needed
        if Event.objects.filter(date=date, time=time, location=location).exists():
            messages.error(request, 'An event with the same time, date, and location already exists.')
            return render(request, 'Event_register.html', {})
        # Create and save the event
        event = Event(
            name=name,
            date=date,
            time=time,
            location=location,
            requirement=requirement,
            themes=themes
        )
        event.save()
        
        
        messages.success(request, 'Event registered successfully!')
        return redirect('Report_tabel1')  # Update 'event_register' to your actual URL name
    return render(request,'Event_register.html', {})

    
def Register_Customer(request):
    if request.method == 'POST':
        cust_name = request.POST.get('customer_name')
        cust_email = request.POST.get('customer_email')
        cust_phone_no = request.POST.get('customer_phone_no')
        cust_address = request.POST.get('customer_address')

        # Perform validation if needed
        if not cust_phone_no.isdigit() or len(cust_phone_no) != 10:
            messages.error(request, 'Customer phone number must be a 10-digit number.')
            return render(request, 'Register_Customer.html') 
        
        # Create and save the Customer
        customer = Customer(
            cust_name=cust_name,
            cust_email=cust_email,
            cust_phone_no=cust_phone_no,
            cust_address=cust_address
        )
        customer.save()

        messages.success(request, 'Customer registered successfully!  ')
        return redirect('Report_Customer')  # Update 'Register_Customer' to your actual URL name
    return render(request, 'Register_Customer.html')




# def Register_Customer(request):
#     if request.method == 'POST':
#         cust_name = request.POST.get('customer_name')
#         cust_email = request.POST.get('customer_email')
#         cust_phone_no = request.POST.get('customer_phone_no')
#         cust_address = request.POST.get('customer_address')

#         # Perform validation if needed
     
#         # Create and save the Customer
#         customer = Customer(
#           Cust_name=cust_name,
#           Cust_email=cust_email,
#           Cust_phone_no=cust_phone_no,
#           Cust_address=cust_address
#         )
#         customer.save()
       
#         messages.success(request, 'Customer registered successfully!')
#         return redirect('home')  # Update 'Register_Customer' to your actual URL name
#     return render(request,'Register_Customer.html')

def Venue_register(request):
    if request.method == 'POST':
        v_event_name = request.POST.get('Event_name')
        event_type = request.POST.get('Event_type')
        event_address = request.POST.get('Event_address')

        # Save the form data to the Venue model
        venue = Venue(
          venue_event_name=v_event_name,
          event_type=event_type, 
          event_address=event_address
        )
        venue.save()

        messages.success(request, 'Venue registered successfully!')

        return redirect('home')  # Redirect to the same page after form submission

    return render(request, 'venue_register.html')

def Payment_register(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('event_name')  # Assuming you have a form field named 'event_name'
        price = request.POST.get('Price')
        payment_type = request.POST.get('payment_type')
        payment_pending = request.POST.get('payment_pending')

        # Save data to the Payment model
        payment = Payment(
            name=name,
            price=price,
            payment_type=payment_type,
            status=payment_pending
        )
        payment.save()
        messages.success(request, 'Payment registered successfully!')


        return redirect('home')
    return render(request,'Payment_register.html')


def Employee_register(request):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')

        if not contact_number.isdigit() or len(contact_number) != 10:
            messages.error(request, 'Contact number must be a 10-digit number.')
            return render(request, 'Employee_register.html')

        
        if Employee.objects.filter(emp_name=emp_name).exists():
            messages.error(request, 'Employee with this name already exists. Choose a different name.')
            return render(request, 'Employee_register.html')

        # Create and save the Employee object to the database
        employee =Employee(
            emp_name=emp_name,
            emp_email=emp_email,
            contact_number=contact_number,
            address=address
        )
        employee.save()
       
        messages.success(request, 'Employee registered successfully!.')

       
        return redirect('home')  
    return render(request, 'Employee_register.html')

def Salary_register(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        date = request.POST.get('date')
        month = request.POST.get('month')
        salary_amount = request.POST.get('salary')

        # Create and save the Salary object to the database
        salary = Salary(
            employee_name=employee_name,
            date=date,
            month=month,
            salary=salary_amount
        )
        salary.save()
         
        messages.success(request, 'Employee Salary Create  successfully!.')

       
        return redirect('home')  
        
    return render(request, 'Salary_register.html')




def Report(request):
    records = Event.objects.all()
    return render(request,'Report_tabel1.html',{"records":records})

def Report2(request):
    records2 = Customer.objects.all()
    return render(request,'Report_Customer.html',{"records2":records2})


def Report3(request):
    records3 = Venue.objects.all()
    return render(request,'Report_Venue.html',{"records3":records3})
def Report5(request):
    records5 = Employee.objects.all()
    return render(request,'Report_Employee.html',{"records5":records5})
def Report6(request):
    records6 = Salary.objects.all()
    return render(request,'Report_Salary.html',{"records6":records6})

