import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from tweetme.apps.tweets.models import Tweet
from tweetme.apps.tweets.serializers import TweetSerializer, TweetCreateSerializer
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


class TweetListCreateAPIView(ListCreateAPIView):
    queryset = Tweet.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TweetCreateSerializer
        return TweetSerializer

    def list(self, request, *args, **kwargs):
        """
        List all the tweets of a given user
        """
        if 'user_id' not in request.query_params:
            return Response('missing user_id', status=400)

        tweets = Tweet.objects.filter(
            user_id=request.query_params['user_id']
        ).order_by('-created_at')
        serializer = TweetSerializer(tweets, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
