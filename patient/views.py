from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer, RegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# for idetifying user and encoding and decoding his info
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.contrib.auth import authenticate, login, logout

# for sending email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class UserregistrationApiView(APIView):
    serializer_class = RegistrationSerializer

    # ei class based view ta just khali pathle get request er jonno error dibe tai custom post method diye shajay nite hobe

# same to same form a jevabe CBV er custom post method lekha hoy oivabei same structure follow kora hoitese
    def post(self, request):
        serializer = self.serializer_class(data = request.data) #uporer serializer ta niye asha hoilo eita user creation model related sob data niyeashbe sathe errors gulo o

        if serializer.is_valid():
            user = serializer.save()
            # print(user)

            token = default_token_generator.make_token(user)
            print('token ', token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print( 'uid ', uid)
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"

            # auto email sending setup
            email_subject = "Confirmation email"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()

            return Response('Check your email for confirmation')
        
        return Response(serializer.errors)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


# user login view

class UserLoginAPIView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)

            if user:
                token , _ = Token.objects.get_or_create(user=user) # ei Token model ta rest_framework er moddhe thake eta add korar por migrate kore nite hoy
                # print(_)
                # print(token.key)
                login(request, user)
                return Response({'token': token.key , 'user_id': user.id})
            else :
                return Response({'error': 'Invalid Credential' })
        return Response(serializer.errors)
    
# akhon user k logout kore db theke token ta k delete kore dite abr r akta apiview er class likhte hobe
class UserLogoutAPIView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')