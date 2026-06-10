from django.shortcuts import render,redirect, HttpResponse

# Create your views here.

#Home_Page
def home_page(request):
    return render(request, 'homepage.html')

#About Page
def about_page(request):
    return render(request,'about.html')

#service page
def service_page(request):
    pass

#Electricity page
def electrcity_page(request):
    pass

#Register Page
def sign_in(request):
    if request.method == 'POST':
    return render(request,'login.html')