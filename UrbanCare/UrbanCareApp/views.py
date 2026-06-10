from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, ProviderProfile
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

#signup page
def signup_view(request):

    if request.method == "POST":

        role = request.POST.get("account_type")

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        if password != confirm_password:
            return render(
                request,
                "signup.html",
                {"error": "Passwords do not match"}
            )

        if User.objects.filter(email=email).exists():
            return render(
                request,
                "signup.html",
                {"error": "Email already registered"}
            )

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            role=(
                User.PROVIDER
                if role == "provider"
                else User.CUSTOMER
            )
        )

        user.first_name = fullname
        user.save()

        # Provider-specific information
        if role == "provider":

            ProviderProfile.objects.create(
                user=user,
                province=request.POST.get("province"),
                district=request.POST.get("district"),
                municipality=request.POST.get("city"),

                citizenship_Num=request.POST.get(
                    "citizenship_number"
                ),

                czn_front=request.FILES.get("id_front"),
                czn_back=request.FILES.get("id_back"),

                service_type=", ".join(
                    request.POST.getlist("services")
                ),

                short_bio=request.POST.get("bio"),

                experience_years=(
                    request.POST.get("experience")
                    if request.POST.get("experience")
                    else None
                )
            )

        return redirect("login")

    return render(request, "signup.html")