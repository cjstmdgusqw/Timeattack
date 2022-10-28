from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def ArticleView(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

