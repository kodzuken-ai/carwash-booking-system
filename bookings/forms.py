from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, UserProfile


class UserRegisterForm(UserCreationForm):
    """User registration form with additional fields"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=50, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom CSS classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })


class BookingForm(forms.ModelForm):
    """Booking creation form"""
    
    # Define available time slots (8 AM to 5 PM)
    TIME_SLOTS = [
        ('08:00:00', '8:00 AM'),
        ('09:00:00', '9:00 AM'),
        ('10:00:00', '10:00 AM'),
        ('11:00:00', '11:00 AM'),
        ('12:00:00', '12:00 PM'),
        ('13:00:00', '1:00 PM'),
        ('14:00:00', '2:00 PM'),
        ('15:00:00', '3:00 PM'),
        ('16:00:00', '4:00 PM'),
        ('17:00:00', '5:00 PM'),
    ]
    
    booking_time = forms.ChoiceField(
        choices=TIME_SLOTS,
        widget=forms.Select(attrs={'class': 'form-control', 'required': True}),
        label='Appointment Time',
        help_text='Note: Each time slot has a maximum of 5 bookings'
    )
    
    class Meta:
        model = Booking
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'vehicle_type',
            'vehicle_plate',
            'service',
            'booking_date',
            'booking_time',
            'notes'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'vehicle_plate': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'service': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Pre-fill customer information from user profile if available
        if user and user.is_authenticated:
            self.fields['customer_name'].initial = user.get_full_name() or user.username
            self.fields['customer_email'].initial = user.email
            if hasattr(user, 'profile'):
                self.fields['customer_phone'].initial = user.profile.phone


class BookingStatusForm(forms.ModelForm):
    """Form for updating booking status (admin only)"""
    
    class Meta:
        model = Booking
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'})
        }
