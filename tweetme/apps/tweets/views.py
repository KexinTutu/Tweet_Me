from django.shortcuts import render

from django.http import HttpResponse, Http404
from tweetme.apps.tweets.models import Tweet


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        print (tweet_id)
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404

    return render(
        request, "tweet_detail.html",
        context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    try:
        obj = Tweet.objects.get()
    except:
        raise Http404

    return HttpResponse(obj.id)
