import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tweetme.apps.tweets.models import Tweet
from tweetme.apps.tweets.serializers import TweetSerializer
from tweetme.apps.tweets.forms import TweetForm


def home_view(request, *args, **kwargs):
    return render(
        request, "home.html",
        context={}, status=200)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def tweet_get_delete_view(request, tweet_id, *args, **kwargs):
    try:
        print(tweet_id)
        tweet = Tweet.objects.get(id=tweet_id)
    except Tweet.DoesNotExist:
        return Response({"message": "Tweet not exist."}, status=404)

    if request.method == 'GET':
        # Get
        serilizer = TweetSerializer(tweet)
        return Response(serilizer.data, status=200)
    elif request.method == 'DELETE':
        # Delete
        if tweet.user != request.user:
            # this tweet doesn't belong to the user
            return Response({"message": "You cannot delete this tweet."}, status=404)
        tweet.delete()
        return Response({"message": "Tweet deleted."}, status=200)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_create_list_view(request, *args, **kwargs):
    if request.method == 'POST':
        # Create
        serializer = TweetSerializer(data=request.POST)

        if serializer.is_valid(raise_exception=True):
            tweet = serializer.save(user=request.user)
            return JsonResponse(serializer.data, status=201)
    elif request.method == 'GET':
        # List
        tweets = Tweet.objects.all()
        serilizer = TweetSerializer(tweets, many=True)
        return Response(serilizer.data, status=200)

    
