from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import generics, permissions, mixins
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User

from users.serializers import UserSerializer


# Create your views here.
# @api_view(['POST'])
# def user_registration(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


# Todo: Remove after further Implementation
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authenticated_view(request):
    user = request.user
    profile = user.profile  # Assuming you have a OneToOne relationship between User and Profile
    return Response({'message': f'Hello, {user.username}! Your birth date is {profile.birth_date}.'})
