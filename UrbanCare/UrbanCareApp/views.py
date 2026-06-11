from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, ProviderProfile,Booking,Notification,ContactMessage
from django.shortcuts import get_object_or_404
# Create your views here.

#Home_Page
def home_page(request):
    return render(request, 'homepage.html')

#About Page
def about_page(request):
    return render(request,'about.html')

#service page
def service_page(request):
    return render(request, 'services.html')

#Electricity page
def electrcity_page(request):
    return render(request, 'electrician.html')

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
            "registration/login.html",
            {"error": "Invalid email or password"}
        )

    return render(request, "registration/login.html")

#signup page
def signup_view(request):

    if request.method == "POST":

        role = request.POST.get("account_type")

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        if password != confirm_password:
            return render(
                request,
                "registration/signup.html",
                {"error": "Passwords do not match"}
            )

        if User.objects.filter(email=email).exists():
            return render(
                request,
                "registration/signup.html",
                {"error": "Email already exists"}
            )

        try:

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

            if role == "provider":

                ProviderProfile.objects.create(
                    user=user,

                    province=request.POST.get("province"),
                    district=request.POST.get("district"),
                    municipality=request.POST.get("city"),

                    citizenship_Num=request.POST.get(
                        "citizenship_number"
                    ),

                    czn_front=request.FILES.get(
                        "id_front"
                    ),

                    czn_back=request.FILES.get(
                        "id_back"
                    ),

                    service_type=", ".join(
                        request.POST.getlist("services")
                    ),

                    experience_years=request.POST.get(
                        "experience"
                    ),

                    short_bio=request.POST.get("bio")
                )

            return redirect("login")

        except Exception as e:

            return render(
                request,
                "registration/signup.html",
                {"error": str(e)}
            )

    return render(
        request,
        "registration/signup.html"
    )

@login_required
@login_required
def book_service(request, service_code):

    if request.method == "POST":
        Booking.objects.create(
            customer=request.user,
            service=service_code,
            status="Pending"
        )
        return redirect("booking")

    return render(request, "booking_servuce.html", {
        "service": service_code
    })

#Provider Dashboard
@login_required
def provider_dashboard(request):

    notifications = Notification.objects.filter(
        provider=request.user
    ).order_by("-created_at")

    return render(
        request,
        "provider/dashboard.html",
        {
            "notifications": notifications
        }
    )

@login_required
def accept_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        provider=request.user
    )

    booking.status = "Accepted"
    booking.save()

    return redirect("provider/provider_bookings")

@login_required
def reject_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        provider=request.user
    )

    booking.status = "Rejected"
    booking.save()

    return redirect("provider/provider_bookings")

@login_required
def customer_bookings(request):

    bookings = Booking.objects.filter(
        customer=request.user
    ).order_by("-booking_date")

    return render(
        request,
        "booking.html",
        {"bookings": bookings}
    )
@login_required
def provider_notifications(request):

    notifications = Notification.objects.filter(
        provider=request.user
    ).order_by("-created_at")

    return render(
        request,
        "provider/provider_notifications.html",
        {
            "notifications": notifications
        }
    )

@login_required
def provider_profile(request):

    profile = ProviderProfile.objects.get(
        user=request.user
    )

    return render(
        request,
        "provider/profile.html",
        {
            "profile": profile
        }
    )

def provider_bookings(request):

    bookings = Booking.objects.filter(
        provider=request.user
    ).order_by("-booking_date")

    return render(
        request,
        "provider/provider_bookings.html",
        {
            "bookings": bookings
        }
    )


def contact_us(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        return render(request, "contacts.html", {"success": True})

    return render(request, "contacts.html")
