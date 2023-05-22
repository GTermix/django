import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from main.models import Category


class PostModel:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(max_length=1024)


def encode():
    model = PostModel(title="Nothing", description="desc")
    model_sr = PostSerializer(model)
    json = JSONRenderer().render(model_sr.data)
    return json


def decode():
    response = io.BytesIO(b'{"title":"nthnh", "description":"desc"}')
    data = JSONParser().parse(response)
    serializer = PostSerializer(data=data)
    serializer.is_valid()


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.SlugField()

    def save(self):
        title = self.validated_data.get('title')
        slug = self.validated_data.get('slug')
        instance = Category.objects.create(title=title, slug=slug)
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
