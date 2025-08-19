from rest_framework import serializers
from .models import Post, Comment
from django.conf import settings

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at')

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comments_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'author', 'author_username', 'title', 'content', 
                 'created_at', 'updated_at', 'comments_count', 'comments')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'comments_count')
    
    def get_comments_count(self, obj):
        return obj.comments_count()