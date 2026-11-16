import random
from datetime import timedelta
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import OTPVerification
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer,LoginSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
     user = serializer.save()

     send_mail(
        'Welcome to Our Application',
        f'Hello {user.username}, your account has been created successfully.',
        None,
        [user.email],
    )


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def destroy(self,request,*args,**kwargs): 
        user = self.get_object()
        user.status = 'Inactive'
        user.save(update_fields=['status'])
        return Response(
            {'message':'User deactivated successfully.'},
            status= status.HTTP_200_OK
        )
class SendOTPAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        email = request.data.get('email')

        try:
            user = User.objects.get(email=email, status='Active')
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        otp = str(random.randint(100000, 999999))

        OTPVerification.objects.update_or_create(
            user=user,
            defaults={
                'otp': otp,
                'created_at': timezone.now(),
                'is_verified': False,
                'purpose':'verification'
            }
        )

        send_mail(
            'Your OTP Verification Code',
            f'Your OTP is {otp}. It is valid for 5 minutes.',
            None,
            [email],
        )

        return Response({
            'message': 'OTP sent successfully.'
        })

class VerifyOTPAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        email = request.data.get('email')
        otp = request.data.get('otp')
        purpose = request.data.get('purpose', 'verification')

        if purpose not in ['verification', 'password_reset']:
            return Response(
                {'error': 'Invalid OTP purpose.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email)
            otp_record = OTPVerification.objects.get(user=user)
        except (User.DoesNotExist, OTPVerification.DoesNotExist):
            return Response(
                {'error': 'Invalid email or OTP.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if otp_record.purpose != purpose:
            return Response(
                {'error': 'Invalid OTP purpose.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if otp_record.otp != otp:
            return Response(
                {'error': 'Invalid OTP.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if timezone.now() - otp_record.created_at > timedelta(minutes=5):
            return Response(
                {'error': 'OTP has expired.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        otp_record.is_verified = True
        otp_record.save()

        return Response({
            'message': 'OTP verified successfully.'
        })
    

class ForgotPasswordAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        email = request.data.get('email')

        try:
            user = User.objects.get(email=email, status='Active')
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        otp = str(random.randint(100000, 999999))

        OTPVerification.objects.update_or_create(
            user=user,
            defaults={
                'otp': otp,
                'created_at': timezone.now(),
                'is_verified': False,
                'purpose': 'password_reset'
            }
        )

        send_mail(
            'Password Reset OTP',
            f'Your password reset OTP is {otp}. It is valid for 5 minutes.',
            None,
            [email]
        )

        return Response({
            'message': 'Password reset OTP sent successfully.'
        })    
class ResetPasswordAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        email = request.data.get('email')
        otp = request.data.get('otp')
        new_password = request.data.get('new_password')

        try:
            user = User.objects.get(email=email, status='Active')
            otp_record = OTPVerification.objects.get(user=user)
        except (User.DoesNotExist, OTPVerification.DoesNotExist):
            return Response(
                {'error': 'Invalid email or OTP.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not otp_record.is_verified:
            return Response(
                {'error': 'Please verify OTP first.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if otp_record.purpose != 'password_reset':
            return Response(
        {'error': 'This OTP is not valid for password reset.'},
        status=status.HTTP_400_BAD_REQUEST
    )

        if timezone.now() - otp_record.created_at > timedelta(minutes=5):
            return Response(
                {'error': 'OTP has expired.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if otp_record.otp != otp:
            return Response(
                {'error': 'Invalid OTP.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not new_password:
            return Response(
                {'error': 'New password is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validate_password(new_password, user)
        except ValidationError as error:
            return Response(
                {'error': error.messages},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        otp_record.delete()

        return Response({
            'message': 'Password reset successfully.'
        })
class LoginAPIView(APIView):

     permission_classes = [AllowAny]

     def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)

            return Response({
                'message': 'Login successful.',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
       
    