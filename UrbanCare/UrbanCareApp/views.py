from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User, ProviderProfile, Booking, Notification, ContactMessage


# ========================
# PUBLIC PAGES
# ========================

def home_page(request):
    """Render the homepage."""
    return render(request, 'homepage.html')


def about_page(request):
    """Render the about page."""
    return render(request, 'about.html')


def service_page(request):
    """Render the main services page."""
    return render(request, 'services.html')


def electricity_page(request):
    """Render the electrician-specific service page."""
    return render(request, 'electrician.html')


def contact_us(request):
    """Handle contact form submission and display contact page."""
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


# ========================
# AUTHENTICATION VIEWS
# ========================

def login_view(request):
    """Handle user login."""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on user role
            if user.role == "provider":
                return redirect("provider_dashboard")
            return redirect("homepage")

        # Invalid credentials
        return render(
            request,
            "registration/login.html",
            {"error": "Invalid email or password"}
        )

    return render(request, "registration/login.html")


def signup_view(request):
    """Handle user registration for both customers and providers."""
    if request.method == "POST":
        role = request.POST.get("account_type")
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        # Validation
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
            # Create user
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                role=User.PROVIDER if role == "provider" else User.CUSTOMER
            )

            user.first_name = fullname
            user.save()

            # Create provider profile if applicable
            if role == "provider":
                ProviderProfile.objects.create(
                    user=user,
                    province=request.POST.get("province"),
                    district=request.POST.get("district"),
                    municipality=request.POST.get("city"),
                    citizenship_Num=request.POST.get("citizenship_number"),
                    czn_front=request.FILES.get("id_front"),
                    czn_back=request.FILES.get("id_back"),
                    service_type=", ".join(request.POST.getlist("services")),
                    experience_years=request.POST.get("experience"),
                    short_bio=request.POST.get("bio")
                )

            return redirect("login")

        except Exception as e:
            return render(
                request,
                "registration/signup.html",
                {"error": str(e)}
            )

    return render(request, "registration/signup.html")


# ========================
# CUSTOMER VIEWS
# ========================

@login_required
def book_service(request, service_code):
    """Allow logged-in customers to book a service."""
    if request.method == "POST":
        Booking.objects.create(
            customer=request.user,
            service=service_code,
            status="Pending"
        )
        return redirect("booking")  # Consider renaming to customer_bookings

    return render(request, "booking_service.html", {  # Fixed typo
        "service": service_code
    })


@login_required
def customer_bookings(request):
    """Display all bookings made by the current customer."""
    bookings = Booking.objects.filter(
        customer=request.user
    ).order_by("-booking_date")

    return render(
        request,
        "booking.html",
        {"bookings": bookings}
    )


# ========================
# PROVIDER VIEWS
# ========================

@login_required
def provider_dashboard(request):
    """Provider dashboard with recent notifications."""
    notifications = Notification.objects.filter(
        provider=request.user
    ).order_by("-created_at")

    return render(
        request,
        "provider/dashboard.html",
        {"notifications": notifications}
    )


@login_required
def provider_bookings(request):
    """Display all bookings assigned to the provider."""
    bookings = Booking.objects.filter(
        provider=request.user
    ).order_by("-booking_date")

    return render(
        request,
        "provider/provider_bookings.html",
        {"bookings": bookings}
    )


@login_required
def accept_booking(request, booking_id):
    """Accept a booking request."""
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
    """Reject a booking request."""
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        provider=request.user
    )
    booking.status = "Rejected"
    booking.save()
    return redirect("provider/provider_bookings")


@login_required
def provider_notifications(request):
    """Display all notifications for the provider."""
    notifications = Notification.objects.filter(
        provider=request.user
    ).order_by("-created_at")

    return render(
        request,
        "provider/provider_notifications.html",
        {"notifications": notifications}
    )


@login_required
def provider_profile(request):
    """Display provider's profile information."""
    profile = get_object_or_404(ProviderProfile, user=request.user)

    return render(
        request,
        "provider/profile.html",
        {"profile": profile}
    )