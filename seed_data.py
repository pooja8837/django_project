import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_booking.settings')
django.setup()

from booking.models import FitnessClass
from datetime import datetime, timedelta
from pytz import timezone

ist = timezone("Asia/Kolkata")

FitnessClass.objects.all().delete()

classes = [
    {"name": "Yoga", "datetime": ist.localize(datetime.now() + timedelta(days=1)), "instructor": "Alice", "available_slots": 10},
    {"name": "Zumba", "datetime": ist.localize(datetime.now() + timedelta(days=2)), "instructor": "Bob", "available_slots": 5},
    {"name": "HIIT", "datetime": ist.localize(datetime.now() + timedelta(days=3)), "instructor": "Charlie", "available_slots": 8},
]

for c in classes:
    FitnessClass.objects.create(**c)
