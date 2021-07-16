from rest_framework import generics
from blog import serializers
from .models import Post

class BlogList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.BlogSerializer

class BlogDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.BlogSerializer