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
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

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
                return Response(status=status.HTTP_200_OK,data={"message":"Message sent successfully!!"})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={"message":"An error occurred"})
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def send_email_with_template(request):
    # if request.method == 'POST':
    if request.method == 'POST':
        try:
            # Extract data from the request
            subject = "Thank you For Contacting Joseph Omondi.".capitalize()
            name = request.data['name']
            recepient_list = request.data['email']
           
            context = {
                'name': name,
            }
            html_content = render_to_string('email_template.html', context)
            
            # Create the email message
            email = EmailMultiAlternatives(subject, '', settings.EMAIL_HOST_USER, [recepient_list])
            email.attach_alternative(html_content, "text/html")
            
            # Send the email user
            email.send()
            
            subject = request.data['subject'] + " from " + request.data['name']
            message = request.data['message']
            name = request.data['name']
            recepient_list = request.data['email']
            print(message)
            # send email to self
            send_mail(subject=subject, message=message,from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_HOST_USER])
            
            # Save the email data
            serializer = EmailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK, data={"message": "Message sent successfully!"})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "An error occurred"})
    return Response(status=status.HTTP_400_BAD_REQUEST)
