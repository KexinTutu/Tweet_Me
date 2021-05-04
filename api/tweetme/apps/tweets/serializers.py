from django.conf import settings

from rest_framework import serializers

from tweetme.apps.tweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'


class TweetCreateSerializer(serializers.ModelSerializer):
    content = serializers.CharField(min_length=6, max_length=settings.MAX_TWEET_LENGTH)

    class Meta:
        model = Tweet
        fields = ['content']
