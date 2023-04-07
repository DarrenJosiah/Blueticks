from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = (ContactSerializer)

# def update_contact(request, contact_id):
#     contact = Contact.objects.get()
    
# Use when http://127.0.0.1:8000/api/contact/1/
    # @action (detail=True, methods=['POST'])
    # def update_contact(self, request, pk=None):
    #     if 'stars' in request.data:

    #         contact = Contact.objects.get(id=pk)
    #         stars = request.data['stars']
    #         user = User.objects.get(id=1)
    #         # print('contact name', contact.name)
    #         print('contact name', user.username)

    #         response = {'message': 'its working'}
    #         return Response(response, status,status=status.HTTP_200_OK)
    #     else: 
    #         response = {'message': 'You need to provide stars'}
    #         return Response(response, status,status=status.HTTP_400_BAD_REQUEST)