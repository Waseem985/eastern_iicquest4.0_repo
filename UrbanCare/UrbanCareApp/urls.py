from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_page, name='homepage'),
    path('provider/dashboard', views.provider_dashboard, name='provider_dashboard'),
    path('about', views.about_page, name='about'),
    path('service', views.service_page, name='service'),
    path("login/", views.login_view, name="login"),
    path('service\Electrician', views.electrcity_page, name='electric'),
]