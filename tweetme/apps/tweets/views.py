from django.shortcuts import render

from django.http import HttpResponse, Http404, JsonResponse
from tweetme.apps.tweets.models import Tweet


def home_view(request, *args, **kwargs):
    return render(
        request, "home.html",
        context={}, status=200)

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
    tweet_list = [{'id': tweet.id, 'content': tweet.content} for tweet in tweets]
    data = {
        "reponse": tweet_list
    }
    return JsonResponse(data)

    
