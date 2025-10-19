from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking, UserProfile
from datetime import date, time


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_profile_creation(self):
        """Test that UserProfile is created for new user"""
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.role, 'customer')
        self.assertEqual(str(profile), 'testuser - customer')


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.booking = Booking.objects.create(
            user=self.user,
            customer_name='John Doe',
            customer_email='john@example.com',
            customer_phone='09123456789',
            vehicle_type='sedan',
            vehicle_plate='ABC1234',
            service='basic',
            booking_date=date(2024, 12, 25),
            booking_time=time(10, 0),
            price=150.00
        )
    
    def test_booking_creation(self):
        """Test that Booking is created correctly"""
        self.assertEqual(self.booking.customer_name, 'John Doe')
        self.assertEqual(self.booking.status, 'pending')
        self.assertEqual(str(self.booking), 'John Doe - Basic Wash on 2024-12-25')
    
    def test_booking_price(self):
        """Test booking price"""
        self.assertEqual(float(self.booking.price), 150.00)


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        UserProfile.objects.create(user=self.user, role='customer')
    
    def test_home_page(self):
        """Test home page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Car Wash System')
    
    def test_login_page(self):
        """Test login page loads"""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')
    
    def test_dashboard_requires_login(self):
        """Test dashboard requires authentication"""
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_authenticated_dashboard(self):
        """Test authenticated user can access dashboard"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
