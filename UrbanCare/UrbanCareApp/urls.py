from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_page, name='homepage'),
    path('about', views.about_page, name='about'),
    path('service', views.service_page, name='service'),
    path('service\Electrician', views.electrcity_page, name='electric'),
]