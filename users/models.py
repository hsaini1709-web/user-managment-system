from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     PROFILE_CHOICES = [
        ('Administrator','Administrator'),
        ('Standard','Standard'),
        ('Developer','Developer'),
        ('Client',"Client"),
        ('Human Resource','Human Resource'),
    ]
     GENDER_CHOICES = [
          ('Male','Male'),
          ('Female','Female'),
          ('Other','Other'),              
     ]
     BLOOD_GROUP_CHOICES = [
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-',"AB-"),
    ('O+','O+'),
    ('O-','O-')
    ]

     STATUS_CHOICES = [
    ('Active','Active'),
    ('Inactive','Inactive'),
    ]
     email = models.EmailField(unique=True,null=True,blank=True)
     profiles = models.CharField(null=True,blank=True,
    max_length=20,
    choices=PROFILE_CHOICES,
    default='Standard'
    )
     date_of_birth= models.DateField(null=True,blank=True)
     gender = models.CharField(
    max_length=10,
    choices=GENDER_CHOICES,
    null=True,
    blank=True
    )
     nationality = models.CharField(max_length=100,blank=True,null=True)
     image = models.ImageField(
          upload_to='profile_images/',
          null=True,
          blank=True
     )
     blood_group = models.CharField(
          max_length =3,
        choices=BLOOD_GROUP_CHOICES,
        null=True,
        blank=True
     )
     phone = models.CharField(max_length=15, blank=True,null=True)
     permanent_address = models.TextField(blank=True,null=True)
     current_address = models.TextField(blank=True,null=True)
     emergency_contact_name = models.CharField(max_length=100, blank=True,null=True)
     emergency_contact_number = models.CharField(max_length=15,blank=True,null=True)
     emergency_contact_relationship = models.CharField(max_length=50,blank=True,null=True)
     status = models.CharField(
          max_length=10,
          choices=STATUS_CHOICES,
          default='Active',
          null=True,
          blank=True
     )
     def __str__(self):
         return self.username
class OTPVerification(models.Model):

    PURPOSE_CHOICES = [
        ('verification', 'Verification'),
        ('password_reset', 'Password Reset'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    purpose = models.CharField(
        max_length=20,
        choices=PURPOSE_CHOICES,
        default='verification'
    )
    otp_request_count = models.PositiveSmallIntegerField(default=0)
    otp_window_start = models.DateTimeField(
        null=True,
        blank=True
    )
    otp_blocked_until = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
    