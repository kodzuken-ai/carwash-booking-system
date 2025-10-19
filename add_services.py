# Run this script to populate initial services
# Command: python manage.py shell < add_services.py

from bookings.models import Service

# Clear existing services
Service.objects.all().delete()

# Service Packages
Service.objects.create(
    name="Basic Wash",
    description="Exterior wash and dry",
    category="package",
    price=25,
    duration=30,
    icon="fa-droplet",
    features="Exterior wash, Hand dry, Tire shine",
    display_order=1
)

Service.objects.create(
    name="Deluxe Wash",
    description="Complete exterior care",
    category="package",
    price=45,
    duration=60,
    icon="fa-spray-can",
    features="Everything in Basic, Wheel cleaning, Window polish, Wax application",
    display_order=2
)

Service.objects.create(
    name="Premium Detail",
    description="Full interior & exterior",
    category="package",
    price=85,
    duration=120,
    icon="fa-star",
    features="Everything in Deluxe, Interior vacuum, Dashboard polish, Leather treatment",
    display_order=3
)

# Individual Services
Service.objects.create(
    name="Exterior Wash",
    description="Professional exterior hand wash",
    category="individual",
    price=15,
    duration=15,
    icon="fa-spray-can",
    display_order=1
)

Service.objects.create(
    name="Interior Cleaning",
    description="Vacuum and interior wipe down",
    category="individual",
    price=20,
    duration=20,
    icon="fa-air-freshener",
    display_order=2
)

Service.objects.create(
    name="Wheel Cleaning",
    description="Deep wheel and rim cleaning",
    category="individual",
    price=10,
    duration=10,
    icon="fa-circle-notch",
    display_order=3
)

Service.objects.create(
    name="Window Cleaning",
    description="Crystal clear window polish",
    category="individual",
    price=8,
    duration=8,
    icon="fa-window-maximize",
    display_order=4
)

Service.objects.create(
    name="Wax Application",
    description="Protective wax coating",
    category="individual",
    price=15,
    duration=15,
    icon="fa-shield-alt",
    display_order=5
)

Service.objects.create(
    name="Tire Shine",
    description="Make your tires shine like new",
    category="individual",
    price=5,
    duration=5,
    icon="fa-star",
    display_order=6
)

Service.objects.create(
    name="Dashboard Polish",
    description="Dashboard cleaning and shine",
    category="individual",
    price=10,
    duration=10,
    icon="fa-tachometer-alt",
    display_order=7
)

Service.objects.create(
    name="Leather Treatment",
    description="Condition and protect leather seats",
    category="individual",
    price=12,
    duration=12,
    icon="fa-couch",
    display_order=8
)

print("✅ Successfully created all services!")
print(f"Total Services: {Service.objects.count()}")
print(f"Packages: {Service.objects.filter(category='package').count()}")
print(f"Individual Services: {Service.objects.filter(category='individual').count()}")
