from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Service(models.Model):
    """Car wash service model"""
    CATEGORY_CHOICES = [
        ('package', 'Service Package'),
        ('individual', 'Individual Service'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    icon = models.CharField(max_length=50, default='fa-car', help_text="FontAwesome icon class (e.g., fa-droplet)")
    features = models.TextField(blank=True, null=True, help_text="Comma-separated list of features")
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0, help_text="Order to display services")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - ₱{self.price}"
    
    def get_features_list(self):
        """Return features as a list"""
        if self.features:
            return [f.strip() for f in self.features.split(',')]
        return []
    
    def get_duration_display(self):
        """Return duration in user-friendly format"""
        hours = self.duration // 60
        minutes = self.duration % 60
        
        if hours > 0 and minutes > 0:
            return f"{hours} hr {minutes} min"
        elif hours > 0:
            return f"{hours} hr"
        else:
            return f"{minutes} min"
    
    class Meta:
        ordering = ['category', 'display_order', 'price']
        verbose_name = "Service"
        verbose_name_plural = "Services"


class UserProfile(models.Model):
    """Extended user profile with role and phone number"""
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")],
        blank=True
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    supabase_id = models.CharField(max_length=255, blank=True, null=True, help_text="Supabase User UUID")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class Booking(models.Model):
    """Car wash booking model"""
    VEHICLE_TYPES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('motorcycle', 'Motorcycle'),
    ]
    
    SERVICE_TYPES = [
        ('basic', 'Basic Wash'),
        ('premium', 'Premium Wash'),
        ('deluxe', 'Deluxe Wash'),
        ('interior', 'Interior Cleaning'),
        ('fulldetail', 'Full Detail'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    # User and customer info
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=50)
    
    # Vehicle info
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    vehicle_plate = models.CharField(max_length=50)
    
    # Service info
    service = models.CharField(max_length=20, choices=SERVICE_TYPES)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Weather info (optional)
    weather_condition = models.CharField(max_length=100, blank=True, null=True)
    weather_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weather_description = models.CharField(max_length=255, blank=True, null=True)
    
    # Additional info
    notes = models.TextField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.service} on {self.booking_date}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['booking_date']),
            models.Index(fields=['status']),
        ]
