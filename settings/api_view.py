from .serializers import AboutSerializer , FAQSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import About , FAQ


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