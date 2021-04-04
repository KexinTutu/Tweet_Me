import random
from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, JsonResponse
from tweetme.apps.tweets.models import Tweet
from tweetme.apps.tweets.forms import TweetForm


def home_view(request, *args, **kwargs):
    return render(
        request, "home.html",
        context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.save()
        if next_url:
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'form.html', context={"form": form})

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
    tweet_list = [{'id': tweet.id, 'content': tweet.content, 'likes': random.randint(0, 300)} for tweet in tweets]
    data = {
        "reponse": tweet_list
    }
    return JsonResponse(data)

    
