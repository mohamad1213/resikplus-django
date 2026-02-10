from apps.accounts.models import User
try:
    u = User.objects.get(email='tatam@gmail.com')
    print(f'User found: {u.email}')
    print(f'Is Active: {u.is_active}')
    print(f'Check Password "tatam": {u.check_password("tatam")}')
    
    # If not active, activate it
    if not u.is_active:
        print("Activating user...")
        u.is_active = True
        u.save()
        print("User activated.")
        
    # If password wrong, reset it (optional, but helpful if user insists it's correct)
    if not u.check_password("tatam"):
        print("Resetting password to 'tatam'...")
        u.set_password("tatam")
        u.save()
        print("Password reset.")

except User.DoesNotExist:
    print('User not found. Creating...')
    u = User.objects.create_user(email='tatam@gmail.com', password='tatam')
    u.is_active = True
    u.is_staff = True # Assuming admin for now based on context
    u.is_superuser = True
    u.save()
    print('User created and activated.')
