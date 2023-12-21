# astroapp/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, otp=None, **kwargs):
        # Your logic to authenticate the user based on phone number and OTP
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
            # Check if the OTP matches (you need to implement this)
            if user.check_otp(otp):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
