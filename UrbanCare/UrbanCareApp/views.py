from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#Home_Page
@login_required
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

#Provider Dashboard
@login_required
def provider_dashboard(request):
    return render(request, "provider/dashboard.html")

#Register Page
def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == "provider":
                return redirect("provider_dashboard")

            return redirect("homepage")

        return render(
            request,
            "login.html",
            {"error": "Invalid email or password"}
        )

    return render(request, "login.html")