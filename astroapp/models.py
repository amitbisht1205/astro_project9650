from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
GENDER_CHOICE=(
    ('MALE','Male'),
    ('FEMALE','Female'),
)
# Create your models here.
class BhagyankPrediction(models.Model):
    Bhagyank=models.IntegerField()
    Bhagyank_prediction_eng=models.CharField(max_length=200)
    Bhagyank_prediction_hin=models.CharField(max_length=200)

    def __str__(self):
        return str(self.Bhagyank)
    
class BhagyankPrediction(models.Model):
    Bhagyank=models.IntegerField()
    Bhagyank_Prediction_eng=models.CharField(max_length=2000)
    Bhagyank_Prediction_hin=models.CharField(max_length=2000)

    def __str__(self):
        return str(self.Bhagyank)
    
class TarotCardPrediction(models.Model):
    card_num = models.IntegerField(null=True,blank=True)
    card_name=models.CharField(max_length=2000)
    card_image=models.FileField(upload_to='images/')
    Prediction_Up_eng = models.CharField(max_length=4000)
    Prediction_Down_eng = models.CharField(max_length=4000)
    Prediction_Up_hin = models.CharField(max_length=4000)
    Prediction_Down_hin = models.CharField(max_length=4000)
    
    
    
class CardPrediction(models.Model):
    card_num = models.IntegerField()
    card_name=models.CharField(max_length=100)
    card_image=models.FileField(upload_to='images/',null=True,blank=True)
    Prediction_Up_eng = models.CharField(max_length=200)
    Prediction_Down_eng = models.CharField(max_length=200)
    Prediction_Up_hin = models.CharField(max_length=200)
    Prediction_Down_hin = models.CharField(max_length=200)


class NumerologyHistory(models.Model):
    Name = models.CharField(max_length=255)
    Gender = models.CharField(choices=GENDER_CHOICE,max_length=10,default='Male')
    DOB = models.DateField()
    TOB = models.TimeField()
    POB = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Numerology History"

    
     


class MoolankPrediction(models.Model):
    Moolank = models.IntegerField()
    Moolank_Prediction_eng = models.CharField(max_length=3000)
    Moolank_Prediction_hin = models.CharField(max_length=3000)    



class CustomUserManager(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('you have not provided valid mail')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()

        return user
    def create_user(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True,null=True)
        


    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=['phone_number']

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'


    def __str__(self):
        return self.first_name    
    

class KundliData(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # Add other fields as needed
    class Meta:
        verbose_name='kundli data'
        verbose_name_plural='kundli data'

    def __str__(self):
        return self.name     
    
class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp_value = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # Set the expiration time (e.g., 5 minutes)
        expiration_time = timezone.now() - timezone.timedelta(minutes=5)
        return self.created_at >= expiration_time
