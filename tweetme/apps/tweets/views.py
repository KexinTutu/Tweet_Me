import random
from django.conf import settings
from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, JsonResponse
from tweetme.apps.tweets.models import Tweet
from tweetme.apps.tweets.forms import TweetForm


def home_view(request, *args, **kwargs):
    return render(
        request, "home.html",
        context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = user
        tweet.save()
        if request.is_ajax():
            return JsonResponse(tweet.serialize(), status=201)

        if next_url:
            return redirect(next_url)
        form = TweetForm()
    elif form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
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
    tweet_list = [tweet.serialize() for tweet in tweets]
    data = {
        "reponse": tweet_list
    }
    return JsonResponse(data)

    
