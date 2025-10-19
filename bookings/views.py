from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Q, Count, Sum, Case, When, Value, IntegerField
import requests
from datetime import datetime
from .models import Booking, UserProfile
from .forms import BookingForm, BookingStatusForm


# Helper function to check if user is admin
def is_admin(user):
    """Check if user is admin/staff - supports both Django staff and profile-based roles"""
    if not user.is_authenticated:
        return False
    
    # Check Django built-in staff/superuser status first
    if user.is_staff or user.is_superuser:
        return True
    
    # Fall back to profile role check for backward compatibility
    try:
        return user.profile.role == 'admin'
    except (UserProfile.DoesNotExist, AttributeError):
        return False


# Weather API Integration
def get_weather_data(city=None):
    """Fetch weather data from OpenWeather API"""
    if not city:
        city = settings.OPENWEATHER_CITY
    
    api_key = settings.OPENWEATHER_API_KEY
    
    if not api_key:
        return {
            'error': 'Weather API key not configured',
            'recommendation': 'Weather conditions unavailable'
        }
    
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        icon = data['weather'][0]['icon']
        
        # Generate car wash recommendation
        is_good_for_wash = True
        if condition in ['Rain', 'Drizzle', 'Thunderstorm']:
            recommendation = 'Not recommended - Rain expected. Consider rescheduling.'
            is_good_for_wash = False
        elif condition in ['Dust', 'Sand']:
            recommendation = 'Not ideal - Dusty conditions. Your car might get dirty quickly.'
            is_good_for_wash = False
        elif temp > 35:
            recommendation = 'Good for a car wash, but very hot! Early morning or late afternoon is better.'
        elif temp < 15:
            recommendation = 'Good for a car wash, but quite cool. Dress warmly!'
        else:
            recommendation = 'Perfect weather for a car wash!'
        
        return {
            'location': data['name'],
            'temperature': round(temp),
            'condition': condition,
            'description': description,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'icon': icon,
            'recommendation': recommendation,
            'is_good_for_wash': is_good_for_wash
        }
    except Exception as e:
        return {
            'error': str(e),
            'recommendation': 'Weather data unavailable'
        }


# Public Views
def home(request):
    """Homepage view - redirects logged-in users to their dashboard"""
    if request.user.is_authenticated:
        if is_admin(request.user):
            return redirect('admin_dashboard')
        return redirect('user_dashboard')
    
    # Get featured services for landing page
    from .models import Service
    featured_services = Service.objects.filter(category='package', is_active=True).order_by('display_order')[:3]
    
    context = {
        'featured_services': featured_services,
    }
    return render(request, 'bookings/home.html', context)


def contact(request):
    """Contact page view"""
    return render(request, 'bookings/contact.html')


def register(request):
    """User registration with Supabase"""
    if request.user.is_authenticated:
        if is_admin(request.user):
            return redirect('admin_dashboard')
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        
        try:
            from .supabase_client import get_supabase_client
            supabase = get_supabase_client()
            
            # Register with Supabase
            response = supabase.auth.sign_up({
                "email": email,
                "password": password,
                "options": {
                    "data": {
                        "first_name": first_name,
                        "last_name": last_name,
                        "phone": phone
                    }
                }
            })
            
            if response.user:
                # Create Django user
                username = email.split('@')[0]
                user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        'email': email,
                        'first_name': first_name,
                        'last_name': last_name,
                    }
                )
                
                # Create user profile
                UserProfile.objects.update_or_create(
                    user=user,
                    defaults={
                        'phone': phone,
                        'role': 'customer',
                        'supabase_id': str(response.user.id)
                    }
                )
                
                messages.success(request, 'Account created! Please check your email for verification.')
                return redirect('login')
            else:
                messages.error(request, 'Registration failed. Please try again.')
                
        except Exception as e:
            messages.error(request, f'Registration error: {str(e)}')
    
    return render(request, 'bookings/register.html')


def user_login(request):
    """User login with Supabase"""
    if request.user.is_authenticated:
        if is_admin(request.user):
            return redirect('admin_dashboard')
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        
        try:
            # Check if input is email or username
            if '@' in username_or_email:
                # It's an email - use Supabase auth
                email = username_or_email
                from .supabase_client import get_supabase_client
                supabase = get_supabase_client()
                
                # Sign in with Supabase
                response = supabase.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })
                
                if response.user:
                    # Find or create Django user
                    username = email.split('@')[0]
                    user, created = User.objects.get_or_create(
                        email=email,
                        defaults={'username': username}
                    )
                    
                    # Get or create user profile
                    profile, _ = UserProfile.objects.get_or_create(
                        user=user,
                        defaults={
                            'supabase_id': str(response.user.id),
                            'role': 'customer'
                        }
                    )
                    
                    # Log in to Django session
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    
                    # Store Supabase session
                    request.session['supabase_access_token'] = response.session.access_token
                    request.session['supabase_refresh_token'] = response.session.refresh_token
                    
                    # Redirect based on user role
                    if is_admin(user):
                        messages.success(request, f'Welcome back, Admin {user.username}!')
                        return redirect('admin_dashboard')
                    else:
                        messages.success(request, f'Welcome back, {user.username}!')
                        return redirect('user_dashboard')
                else:
                    messages.error(request, 'Invalid credentials.')
            else:
                # It's a username - use Django auth
                username = username_or_email
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    # Redirect based on user role
                    if is_admin(user):
                        messages.success(request, f'Welcome back, Admin {user.username}!')
                        return redirect('admin_dashboard')
                    else:
                        messages.success(request, f'Welcome back, {user.username}!')
                        return redirect('user_dashboard')
                else:
                    messages.error(request, 'Invalid username or password.')
                
        except Exception as e:
            messages.error(request, f'Login error: {str(e)}')
    
    return render(request, 'bookings/login.html')


def user_logout(request):
    """User logout from Supabase and Django"""
    try:
        from .supabase_client import get_supabase_client
        supabase = get_supabase_client()
        
        # Get access token from session
        access_token = request.session.get('supabase_access_token')
        
        if access_token and supabase:
            # Sign out from Supabase
            supabase.auth.sign_out()
        
        # Clear Supabase session data
        request.session.pop('supabase_access_token', None)
        request.session.pop('supabase_refresh_token', None)
        
    except Exception as e:
        print(f'Supabase logout error: {e}')
    
    # Logout from Django
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


def password_reset_request(request):
    """Send password reset email via Supabase"""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        try:
            from .supabase_client import get_supabase_client
            supabase = get_supabase_client()
            supabase.auth.reset_password_for_email(email)
            messages.success(request, 'Password reset email sent! Check your inbox.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'bookings/password_reset.html')


# Authenticated User Views
@login_required
def user_dashboard(request):
    """Regular user dashboard view"""
    # Get all user's bookings for statistics
    all_bookings = Booking.objects.filter(user=request.user)
    
    # Get only upcoming bookings (pending, confirmed, in-progress) sorted by soonest first
    bookings = all_bookings.filter(
        status__in=['pending', 'confirmed', 'in-progress']
    ).order_by('booking_date', 'booking_time')
    
    # Get statistics
    total_bookings = all_bookings.count()
    pending_bookings = all_bookings.filter(status='pending').count()
    completed_bookings = all_bookings.filter(status='completed').count()
    
    # Get weather data for logged-in users
    weather = get_weather_data()
    
    context = {
        'bookings': bookings[:10],  # Show next 10 upcoming bookings
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'completed_bookings': completed_bookings,
        'weather': weather,
    }
    return render(request, 'user/dashboard.html', context)


@login_required
def user_services(request):
    """User services page - browse and search services"""
    from .models import Service
    
    # Get all active services
    packages = Service.objects.filter(category='package', is_active=True)
    individual_services = Service.objects.filter(category='individual', is_active=True)
    
    context = {
        'packages': packages,
        'individual_services': individual_services,
    }
    return render(request, 'user/services.html', context)


@login_required
def user_bookings(request):
    """User bookings page - view all bookings"""
    from django.core.paginator import Paginator
    
    # Get all user's bookings
    bookings = Booking.objects.filter(user=request.user)
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        bookings = bookings.filter(status=status_filter)
    
    # Filter by service
    service_filter = request.GET.get('service', '')
    if service_filter:
        bookings = bookings.filter(service=service_filter)
    
    # Filter by date
    date_filter = request.GET.get('date', '')
    if date_filter:
        bookings = bookings.filter(booking_date=date_filter)
    
    # Order by date descending (newest first)
    bookings = bookings.order_by('-booking_date', '-booking_time')
    
    # Pagination (7 per page)
    paginator = Paginator(bookings, 7)
    page = request.GET.get('page', 1)
    bookings_obj = paginator.get_page(page)
    
    context = {
        'bookings': bookings_obj,
        'status_filter': status_filter,
        'service_filter': service_filter,
        'date_filter': date_filter,
    }
    return render(request, 'user/bookings.html', context)


@login_required
def create_booking(request):
    """Create new booking view"""
    from .models import Service
    from datetime import date
    
    # Get selected service from URL parameter
    service_id = request.GET.get('service')
    selected_service = None
    if service_id:
        try:
            selected_service = Service.objects.get(id=service_id, is_active=True)
        except Service.DoesNotExist:
            messages.warning(request, 'Selected service not found.')
    
    # Get all active services for the dropdown
    all_services = Service.objects.filter(is_active=True)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            
            # Validate date is not in the past
            if booking.booking_date < date.today():
                messages.error(request, 'Cannot book appointments in the past. Please select a future date.')
                return render(request, 'user/create_booking.html', {
                    'form': form,
                    'selected_service': selected_service,
                    'all_services': all_services,
                })
            
            # Check if time slot is available (max 5 bookings per time slot per day)
            existing_bookings = Booking.objects.filter(
                booking_date=booking.booking_date,
                booking_time=booking.booking_time
            ).exclude(status='cancelled').count()
            
            if existing_bookings >= 5:
                messages.error(request, f'Sorry, the time slot {booking.booking_time.strftime("%I:%M %p")} on {booking.booking_date.strftime("%B %d, %Y")} is fully booked. Please select a different time.')
                return render(request, 'user/create_booking.html', {
                    'form': form,
                    'selected_service': selected_service,
                    'all_services': all_services,
                })
            
            # Get price and service type from Service model if service exists in database
            service_id_from_form = request.POST.get('service_id')
            if service_id_from_form:
                try:
                    service = Service.objects.get(id=service_id_from_form)
                    booking.price = service.price
                    
                    # Map service name to service type
                    service_name_lower = service.name.lower()
                    if 'basic' in service_name_lower:
                        booking.service = 'basic'
                    elif 'deluxe' in service_name_lower:
                        booking.service = 'deluxe'
                    elif 'premium' in service_name_lower or 'detail' in service_name_lower:
                        booking.service = 'premium'
                    elif 'interior' in service_name_lower:
                        booking.service = 'interior'
                    elif 'full' in service_name_lower:
                        booking.service = 'fulldetail'
                    else:
                        booking.service = 'basic'  # Default fallback
                        
                except Service.DoesNotExist:
                    # Fallback to old price map
                    price_map = {
                        'basic': 25.00,
                        'premium': 45.00,
                        'deluxe': 85.00,
                    }
                    booking.price = price_map.get(booking.service, 25.00)
            else:
                booking.price = 25.00
            
            booking.save()
            messages.success(request, 'Booking created successfully! Your booking is pending confirmation from our team.')
            return redirect('user_dashboard')
    else:
        form = BookingForm(user=request.user)
    
    context = {
        'form': form,
        'selected_service': selected_service,
        'all_services': all_services,
    }
    return render(request, 'user/create_booking.html', context)


@login_required
def booking_detail(request, booking_id):
    """View booking details"""
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Check if user owns this booking or is admin
    if booking.user != request.user and not is_admin(request.user):
        messages.error(request, 'You do not have permission to view this booking.')
        return redirect('user_dashboard')
    
    return render(request, 'user/booking_detail.html', {'booking': booking})


@login_required
def delete_booking(request, booking_id):
    """Delete a booking"""
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Check if user owns this booking or is admin
    if booking.user != request.user and not is_admin(request.user):
        messages.error(request, 'You do not have permission to delete this booking.')
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('user_dashboard')
    
    return render(request, 'user/confirm_delete.html', {'booking': booking})


# Admin Views
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    """Admin dashboard view - Manage all users and bookings"""
    from django.core.paginator import Paginator
    from django.contrib.auth.models import User
    
    # Get all bookings
    bookings = Booking.objects.all().select_related('user')
    
    # Get all users with booking count annotation
    # Order by: admin role first, then by date joined (newest first)
    users = User.objects.all().select_related('profile').annotate(
        booking_count=Count('bookings'),
        role_order=Case(
            When(profile__role='admin', then=Value(0)),
            default=Value(1),
            output_field=IntegerField()
        )
    ).order_by('role_order', '-date_joined')
    
    # Get statistics
    total_bookings = bookings.count()
    pending_bookings = bookings.filter(status='pending').count()
    confirmed_bookings = bookings.filter(status='confirmed').count()
    completed_bookings = bookings.filter(status='completed').count()
    cancelled_bookings = bookings.filter(status='cancelled').count()
    total_users = users.count()
    
    # Calculate revenue from completed bookings
    revenue = bookings.filter(status='completed').aggregate(total=Sum('price'))['total'] or 0
    
    # Filter by search query
    search_query = request.GET.get('search', '')
    if search_query:
        bookings = bookings.filter(
            Q(customer_name__icontains=search_query) |
            Q(customer_email__icontains=search_query) |
            Q(vehicle_plate__icontains=search_query)
        )
    
    # Filter by status (default to all statuses)
    status_filter = request.GET.get('status', '')
    if status_filter:
        bookings = bookings.filter(status=status_filter)
    
    # Filter by service
    service_filter = request.GET.get('service', '')
    if service_filter:
        bookings = bookings.filter(service=service_filter)
    
    # Filter by date (no default filter)
    date_filter = request.GET.get('date', '')
    if date_filter:
        bookings = bookings.filter(booking_date=date_filter)
    
    # Filter users by search
    user_search = request.GET.get('user_search', '')
    if user_search:
        users = users.filter(
            Q(username__icontains=user_search) |
            Q(email__icontains=user_search) |
            Q(first_name__icontains=user_search) |
            Q(last_name__icontains=user_search)
        )
    
    # Pagination for bookings (7 per page)
    # Sort by date (soonest first), then by time
    bookings_list = bookings.order_by('booking_date', 'booking_time')
    bookings_paginator = Paginator(bookings_list, 7)
    bookings_page = request.GET.get('bookings_page', 1)
    bookings_obj = bookings_paginator.get_page(bookings_page)
    
    # Pagination for users (7 per page)
    users_paginator = Paginator(users, 7)
    users_page = request.GET.get('users_page', 1)
    users_obj = users_paginator.get_page(users_page)
    
    # Get all services for Services tab
    from .models import Service
    all_services = Service.objects.all().order_by('category', 'display_order', 'name')
    
    # Pagination for services (7 per page)
    services_paginator = Paginator(all_services, 7)
    services_page = request.GET.get('services_page', 1)
    services_obj = services_paginator.get_page(services_page)
    
    context = {
        'bookings': bookings_obj,
        'users': users_obj,
        'services': services_obj,
        'total_bookings': total_bookings,
        'total_users': total_users,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'completed_bookings': completed_bookings,
        'cancelled_bookings': cancelled_bookings,
        'revenue': revenue,
        'search_query': search_query,
        'status_filter': status_filter,
        'service_filter': service_filter,
        'date_filter': date_filter,
        'user_search': user_search,
    }
    return render(request, 'admin/dashboard.html', context)


@login_required
@user_passes_test(is_admin)
def update_booking_status(request, booking_id):
    """Update booking status (admin only) - Handles POST from dropdown on admin dashboard"""
    booking = get_object_or_404(Booking, id=booking_id)
    old_status = booking.status  # Store the old status
    
    if request.method == 'POST':
        # Get new status from POST data
        new_status = request.POST.get('status')
        valid_statuses = [choice[0] for choice in Booking.STATUS_CHOICES]
        
        if not new_status:
            messages.error(request, 'No status provided.')
            return redirect('admin_dashboard')
            
        if new_status in valid_statuses:
            booking.status = new_status
            booking.save()
            
            # Send confirmation email when status changes to 'confirmed'
            if old_status != 'confirmed' and new_status == 'confirmed':
                from .emails import send_booking_confirmation_email
                email_sent = send_booking_confirmation_email(booking)
                
                if email_sent:
                    messages.success(request, f'Booking confirmed! Confirmation email sent to {booking.customer_email}.')
                else:
                    messages.success(request, f'Booking status updated to {new_status}.')
                    messages.warning(request, 'However, confirmation email could not be sent.')
            else:
                messages.success(request, f'Booking status updated to {booking.get_status_display()}.')
            
            return redirect('admin_dashboard')
        else:
            messages.error(request, f'Invalid status "{new_status}". Valid options are: {", ".join(valid_statuses)}')
            return redirect('admin_dashboard')
    else:
        # GET request - redirect to admin dashboard
        messages.info(request, 'Please use the status dropdown on the dashboard to update booking status.')
        return redirect('admin_dashboard')


# Service CRUD Views
@login_required
@user_passes_test(is_admin)
def create_service(request):
    """Create new service (admin only)"""
    from .models import Service
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        icon = request.POST.get('icon', 'fa-car')
        features = request.POST.get('features', '')
        is_active = request.POST.get('is_active') == 'on'
        display_order = request.POST.get('display_order', 0)
        
        Service.objects.create(
            name=name,
            description=description,
            category=category,
            price=price,
            duration=duration,
            icon=icon,
            features=features,
            is_active=is_active,
            display_order=display_order
        )
        messages.success(request, 'Service created successfully!')
        from django.urls import reverse
        return redirect(reverse('admin_dashboard') + '?tab=services')
    
    return render(request, 'admin/service_form.html', {'action': 'Create'})


@login_required
@user_passes_test(is_admin)
def edit_service(request, service_id):
    """Edit existing service (admin only)"""
    from .models import Service
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.description = request.POST.get('description')
        service.category = request.POST.get('category')
        service.price = request.POST.get('price')
        service.duration = request.POST.get('duration')
        service.icon = request.POST.get('icon', 'fa-car')
        service.features = request.POST.get('features', '')
        service.is_active = request.POST.get('is_active') == 'on'
        service.display_order = request.POST.get('display_order', 0)
        service.save()
        
        messages.success(request, 'Service updated successfully!')
        from django.urls import reverse
        return redirect(reverse('admin_dashboard') + '?tab=services')
    
    return render(request, 'admin/service_form.html', {'service': service, 'action': 'Edit'})


@login_required
@user_passes_test(is_admin)
def delete_service(request, service_id):
    """Delete service (admin only)"""
    from .models import Service
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, f'Service "{service.name}" deleted successfully!')
    from django.urls import reverse
    return redirect(reverse('admin_dashboard') + '?tab=services')


# API endpoint for weather (AJAX)
def weather_api(request):
    """Return weather data as JSON"""
    city = request.GET.get('city', settings.OPENWEATHER_CITY)
    weather = get_weather_data(city)
    return JsonResponse(weather)
