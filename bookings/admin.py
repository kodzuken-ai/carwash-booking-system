from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Booking, UserProfile, Service


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ('phone', 'role')


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role', 'is_staff')
    
    def get_role(self, obj):
        try:
            return obj.profile.role
        except UserProfile.DoesNotExist:
            return 'N/A'
    get_role.short_description = 'Role'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'customer_email',
        'vehicle_type',
        'service',
        'booking_date',
        'booking_time',
        'status',
        'price',
        'created_at'
    )
    list_filter = ('status', 'vehicle_type', 'service', 'booking_date')
    search_fields = ('customer_name', 'customer_email', 'vehicle_plate', 'customer_phone')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'booking_date'
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('user', 'customer_name', 'customer_email', 'customer_phone')
        }),
        ('Vehicle Information', {
            'fields': ('vehicle_type', 'vehicle_plate')
        }),
        ('Service Details', {
            'fields': ('service', 'booking_date', 'booking_time', 'price', 'status')
        }),
        ('Weather Information', {
            'fields': ('weather_condition', 'weather_temperature', 'weather_description'),
            'classes': ('collapse',)
        }),
        ('Additional Information', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_confirmed', 'mark_as_completed', 'mark_as_cancelled']
    
    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='confirmed')
    mark_as_confirmed.short_description = "Mark selected bookings as Confirmed"
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = "Mark selected bookings as Completed"
    
    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
    mark_as_cancelled.short_description = "Mark selected bookings as Cancelled"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration', 'is_active', 'display_order')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('is_active', 'display_order')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category', 'icon')
        }),
        ('Pricing & Duration', {
            'fields': ('price', 'duration')
        }),
        ('Features', {
            'fields': ('features',),
            'description': 'Enter features separated by commas (e.g., Exterior wash, Hand dry, Tire shine)'
        }),
        ('Display Settings', {
            'fields': ('is_active', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Customize admin site
admin.site.site_header = "Car Wash System Administration"
admin.site.site_title = "Car Wash Admin"
admin.site.index_title = "Welcome to Car Wash Management System"
