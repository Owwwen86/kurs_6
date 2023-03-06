from rest_framework import serializers
from ads.models import Comment, Ad


class AdSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='id')

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    phone = serializers.CharField(source='author.phone')
    author_id = serializers.IntegerField(source='author.id')
    pk = serializers.IntegerField(source='id')

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",
                  "author_id", ]


class CommentCreateSerializer(serializers.ModelSerializer):
    author_id = serializers.SerializerMethodField()
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    author_image = serializers.SerializerMethodField()

    def get_author_id(self, obj):
        author_id = obj.author.id
        return author_id

    def get_author_first_name(self, obj):
        author_first_name = obj.author.first_name
        return author_first_name

    def get_author_last_name(self, obj):
        author_last_name = obj.author.last_name
        return author_last_name

    def get_author_image(self, obj):
        author_image = obj.author.image
        return author_image

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at", "author_first_name", "author_last_name", "ad_id",
                  "author_image"]


class CommentSerializer(serializers.ModelSerializer):

    pk = serializers.IntegerField(source='id')
    author_id = serializers.IntegerField(source='author.id')
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_image = serializers.ImageField(source='author.image')

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at", "author_first_name", "author_last_name", "ad_id",
                  "author_image"]
