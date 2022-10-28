from django.forms import modelformset_factory
from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer): # 모델기반을 돌아갈
    class Meta:
        model = Article
        fields = "__all__"
