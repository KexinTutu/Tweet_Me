"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from tweetme.apps.tweets.views import home_view, tweet_detail_view, tweet_list_view, tweet_create_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', home_view),
    url(r'^tweet/create', tweet_create_view),
    url(r'^tweet/(?P<tweet_id>\d)', tweet_detail_view),
    url(r'^tweets', tweet_list_view),
]