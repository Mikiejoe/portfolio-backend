from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
from .models import Project, Photo
from .serializers import ProjectSerializer, PhotoSerializer,EmailsSerializer

class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class PhotoListCreateAPIView(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    
@api_view(["POST"])
def send_email(request):    
    if request.method == 'POST':
        # Extract data from the request and send the data to my email
        try:
            print(request.data)                
            subject = request.data['subject'] + " from " + request.data['name']
            message = request.data['message']
            name = request.data['name']
            recepient_list = request.data['email']
            message = f"Dear {name},\nThank you for reaching out to me through my portfolio, I will get back to you as soon as possible."
            print(message)
            send_mail(subject=subject, message=message,from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_HOST_USER])
        
            
            # Send a confirmation email to the user
            subject = "Joseph Omondi Received a message from you."
            name = request.data['name']
            message = f"Dear {name},\nThank you for reaching out to me through my portfolio, I will get back to you as soon as possible."
            print(message)
            res = send_mail(subject, message,from_email=settings.EMAIL_HOST_USER, recipient_list=[recepient_list])
            print("result is ",res)
            serializer = EmailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={"message":"An error occurred"})
    return Response(status=status.HTTP_400_BAD_REQUEST)