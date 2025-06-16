from django.urls import path
from .views import FitnessClassList, BookClass, BookingList

urlpatterns = [
    path('classes/', FitnessClassList.as_view()),
    path('book/', BookClass.as_view()),
    path('bookings/', BookingList.as_view()),
]
