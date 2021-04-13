import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from tweetme.apps.tweets.models import Tweet
from tweetme.apps.tweets.serializers import TweetSerializer
from tweetme.apps.tweets.forms import TweetForm


def home_view(request, *args, **kwargs):
    return render(
        request, "home.html",
        context={}, status=200)

@api_view(['POST'])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)

    if serializer.is_valid(raise_exception=True):
        tweet = serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)

@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except Tweet.DoesNotExist:
        return Response({}, status=404)

    serilizer = TweetSerializer(tweet)
    return Response(serilizer.data, status=200)

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    serilizer = TweetSerializer(tweets, many=True)
    return Response(serilizer.data, status=200)

    
