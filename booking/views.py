from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

class FitnessClassList(APIView):
    def get(self, request):
        classes = FitnessClass.objects.all()
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookClass(APIView):
    def post(self, request):
        class_id = request.data.get('class_id')
        name = request.data.get('client_name')
        email = request.data.get('client_email')

        if not all([class_id, name, email]):
            return Response({"error": "Missing fields"}, status=400)

        try:
            fitness_class = FitnessClass.objects.get(id=class_id)
        except FitnessClass.DoesNotExist:
            return Response({"error": "Class not found"}, status=404)

        if fitness_class.available_slots <= 0:
            return Response({"error": "No slots available"}, status=400)

        Booking.objects.create(fitness_class=fitness_class, client_name=name, client_email=email)
        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response({"message": "Booking successful"}, status=201)

class BookingList(APIView):
    def get(self, request):
        email = request.query_params.get("email")
        if not email:
            return Response({"error": "Email required"}, status=400)

        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


# Create your views here.
