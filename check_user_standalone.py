
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.accounts.models import User

try:
    try:
        u = User.objects.get(email='tatam@gmail.com')
        print(f'User found: {u.email}')
        print(f'Is Active: {u.is_active}')
        print(f'Is Staff: {u.is_staff}')
        
        if not u.check_password("tatam"):
            print("Password invalid. Resetting to 'tatam'...")
            u.set_password("tatam")
            u.save()
            print("Password reset.")
        else:
            print("Password is correct.")
            
        if not u.is_active:
             print("Activating user...")
             u.is_active = True
             u.save()
             print("User activated.")
             
        if not u.is_staff:
             print("Making user staff...")
             u.is_staff = True
             u.save()
             print("User is now staff.")

    except User.DoesNotExist:
        print('User not found. Creating...')
        u = User.objects.create_user(email='tatam@gmail.com', password='tatam')
        # create_user handles password hashing, but create_user usually expects username field if it's not email.
        # Since USERNAME_FIELD = email, create_user(email=..., password=...) works generally or create_user(username=..., email=..., ...)
        # Our model defines USERNAME_FIELD = 'email', so first arg is likely expected to be email or we pass as kwarg.
        # Looking at AbstractUser source, create_user(username, email, password).
        # But we replaced username with email? No, we likely still have username field unless we removed it or set USERNAME_FIELD='email'.
        # Let's check model again. It inherits AbstractUser. AbstractUser has username. We didn't remove it.
        # But USERNAME_FIELD='email'.
        
        # Safe bet:
        u.is_active = True
        u.is_staff = True
        u.is_superuser = True
        u.save()
        print('User created and activated.')

except Exception as e:
    print(f"Error: {e}")
