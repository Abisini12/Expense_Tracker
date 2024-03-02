from django.template import loader
from .models import Userinfo,reportinfo,productinfo
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm,DateRangeForm
from django.db.models import Sum


def ExpenseTracker(request):
    template=loader.get_template('basic.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method =='POST':
         username=request.POST['username']
         name=request.POST['name']
         email=request.POST['email']
         role=request.POST['role']
         phone=request.POST['phone']
         password=request.POST['password']
         cpassword=request.POST['cpassword']
         data=Userinfo(username=username,name=name,email=email,role=role,phone=phone,password=password,cpassword=cpassword)
         data.save()
         return redirect('login')
    return render(request,'signupfinal.html')


def landingpage(request):
    template=loader.get_template('landingpage.html')
    return HttpResponse(template.render())

def homepage(request):
    template=loader.get_template('homepage.html')
    return HttpResponse(template.render())

    
def logout_view(request):
    logout(request)

    return redirect('login')

        
def addexpense(request):
    if request.method == 'POST':
        budget = int(request.POST.get('budget'))
        category = request.POST.get('categorySelect')
        purchase_product = request.POST['product_name']
        purchase_date = request.POST.get('date')
        price = float(request.POST['product_price'])
        number_of_products = int(request.POST['numberofproduct'])
      
        # Now you can proceed with saving the data to the database
        data = productinfo(
            category=category,
            purchase_product=purchase_product,
            purchase_date=purchase_date,
            amount_spent=amount_spent,
            number_of_products=number_of_products,
            bill_receipt=bill_receipt,
        )
        data.save()
        
        product_details = productinfo.objects.all()
        expense = sum(x.amount_spent for x in product_details)

    

    return render(request, 'expense.html')

def saveexpense(request):
    product_details = productinfo.objects.all()
    for x in product_details:
        data = reportinfo(
            category=x.category,
            purchase_product=x.purchase_product,
            purchase_date=x.purchase_date,
            amount_spent=x.amount_spent,
            number_of_products=x.number_of_products,
            bill_receipt=x.bill_receipt,
        )
        data.save()

    product_details.delete()
    return render(request, 'homepage.html')



def filter_records(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        start_date = None
        end_date = None
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if end_date and start_date:
                # If the filter button is clicked, filter records based on the date range
                filtered_records = reportinfo.objects.filter(
                    purchase_date__range=[start_date, end_date]
                )
                return render(request, 'report.html', {'records': filtered_records, 'form': form})
    else:
        form = DateRangeForm() #calling the appropiate forms
    
    filtered_records = reportinfo.objects.all()
    return render(request, 'report.html', {'records': filtered_records,'form': form})


def expense_pie_chart(request):
    categories = reportinfo.objects.values('category').distinct()
    expense_data = {}

    for category in categories:
        category_name = category['category']
        total_expense = reportinfo.objects.filter(category=category_name).aggregate(total=Sum('amount_spent'))['total'] or 0
        expense_data[category_name] = total_expense
    print(expense_data)
    return Jsonesponse(expense_data)

