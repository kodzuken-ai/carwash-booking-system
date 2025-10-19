from django.urls import path
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    
    # Authentication (Supabase)
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    
    # User dashboard and bookings
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user/services/', views.user_services, name='user_services'),
    path('user/bookings/', views.user_bookings, name='user_bookings'),
    path('user/booking/create/', views.create_booking, name='create_booking'),
    path('user/booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('user/booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    
    # Staff/Admin dashboard and management
    path('staff/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff/booking/<int:booking_id>/status/', views.update_booking_status, name='update_booking_status'),
    
    # Admin service management
    path('staff/service/create/', views.create_service, name='create_service'),
    path('staff/service/<int:service_id>/edit/', views.edit_service, name='edit_service'),
    path('staff/service/<int:service_id>/delete/', views.delete_service, name='delete_service'),
    
    # API endpoints
    path('api/weather/', views.weather_api, name='weather_api'),
]
