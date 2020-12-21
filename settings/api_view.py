from .serializers import AboutSerializer , FAQSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import About , FAQ
from django.core.mail import send_mail
from django.conf import settings

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def about_api(request):
    about = About.objects.last()
    data = AboutSerializer(about).data
    return Response({'success':True , 'data':data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def faq_api(request):
    faq = FAQ.objects.all()
    data = FAQSerializer(faq , many=True).data
    return Response({'success':True , 'data':data})


@api_view(['POST'])
def contact_api(request):
    subject = request.POST['subject']
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    send_mail(
        subject,
        f'message from {name} \n email : {email} \n Message : {message}',
        email,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
    return Response({'Success': True , 'Message': 'Message Sent Successfully '})