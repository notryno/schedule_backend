# myapp/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    
    print('Request Data:', data)


    # Validate and save user data
    try:
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise ValueError('Email and password are required.')

        user = User.objects.create(
            email=email,
            password=make_password(password),  # Hash the password before saving
        )

        return Response({'message': 'User registered successfully'})
    except Exception as e:
        print('Error in registration:', str(e))  # Log the detailed error
        return Response({'error': str(e)}, status=400)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data
    print('Login Request Data:', data)
    print('Email for authentication:', data['email'].lower())
    print('Password for authentication:', data['password'])

    user = authenticate(email=data['email'].lower(), password=data['password'])
    print('Authenticated User:', user)

    if user is not None:
        # User is valid, generate and return an authentication token
        token, created = Token.objects.get_or_create(user=user)
        print('Generated Token:', token.key)
        return Response({'token': token.key})
    else:
        print('Authentication failed. Checking user in the database.')

        try:
            # Try to get the user from the database
            user_from_db = User.objects.get(email=data['email'].lower())
            print('User in the database:', user_from_db)
        except User.DoesNotExist:
            print('User not found in the database.')

        # User is not valid, return an error message
        return Response({'error': 'Invalid credentials'}, status=401)


    
    # try:
    #     email = data['email'].lower()
    #     password = data['password']

    #     # Get the user based on the provided email
    #     user = User.objects.get(email=email)

    #     # Check the password manually (no need for authenticate)
    #     if user.check_password(password):
    #         print('Password is correct.')

    #         # User is valid, generate and return an authentication token
    #         token, created = Token.objects.get_or_create(user=user)
    #         print('Generated Token:', token.key)
    #         return Response({'token': token.key})
    #     else:
    #         # Password is incorrect
    #         return Response({'error': 'Invalid credentials'}, status=401)

    # except User.DoesNotExist:
    #     # User with the provided email does not exist
    #     return Response({'error': 'Invalid credentials'}, status=401)
    # except Exception as e:
    #     # Other exceptions (handle them as needed)
    #     print('Error during login:', str(e))
    #     return Response({'error': 'An error occurred'}, status=500)

