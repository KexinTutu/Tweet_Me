import random
from django.conf import settings
from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, JsonResponse
from tweetme.apps.tweets.models import Tweet
from tweetme.apps.tweets.serializers import TweetSerializer
from tweetme.apps.tweets.forms import TweetForm


def home_view(request, *args, **kwargs):
    return render(
        request, "home.html",
        context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST or None)
    if serializer.is_valid():
        tweet = serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({}, status=400)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404

    return render(
        request, "tweet_detail.html",
        context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweet_list = [tweet.serialize() for tweet in tweets]
    data = {
        "reponse": tweet_list
    }
    return JsonResponse(data)

    
