from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserFollowSerializer, FollowActionSerializer
from .models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request):
    serializer = FollowActionSerializer(data=request.data)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        user_to_follow = get_object_or_404(get_user_model(), id=user_id)
        
        if request.user.follow(user_to_follow):
            return Response({
                'status': 'success',
                'message': f'You are now following {user_to_follow.username}'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'error',
                'message': 'Unable to follow user'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request):
    serializer = FollowActionSerializer(data=request.data)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        user_to_unfollow = get_object_or_404(get_user_model(), id=user_id)
        
        if request.user.unfollow(user_to_unfollow):
            return Response({
                'status': 'success',
                'message': f'You have unfollowed {user_to_unfollow.username}'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'error',
                'message': 'Unable to unfollow user'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def following_list(request):
    following = request.user.following.all()
    serializer = UserFollowSerializer(following, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followers_list(request):
    followers = request.user.followers.all()
    serializer = UserFollowSerializer(followers, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_detail(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    serializer = UserFollowSerializer(user, context={'request': request})
    return Response(serializer.data)