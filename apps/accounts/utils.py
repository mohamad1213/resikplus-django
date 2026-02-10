import random
from django.core.mail import EmailMessage
from django.conf import settings

from apps.accounts.models import OneTimePassword, User


def generateOtp():
    """Generate a 6-digit OTP"""
    otp = random.randint(100000, 999999)
    return str(otp)

def send_code_to_user(email):
    subject = 'one-time password (OTP) Verification Code'
    otp_code = generateOtp()
    print(otp_code)
    user= User.objects.get(email=email)
    current_site = 'example.com'  
    email_body = f'hello {user.first_name} thanks for signing up on {current_site}. please use this code to verify your account {otp_code}'
    from_email = settings.DEFAULT_FROM_EMAIL
    
    OneTimePassword.objects.create(user=user, code=otp_code)
    send_mail = EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[email])
    send_mail.send(fail_silently=False)
    