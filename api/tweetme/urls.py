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
from django.urls import include
from rest_framework import routers

from tweetme.apps.accounts.views import AccountViewSet, UserViewSet
from tweetme.apps.tweets.views import home_view, tweet_get_delete_view, TweetListCreateAPIView
from tweetme.apps.friendships.views import FriendshipViewSet

router = routers.DefaultRouter()
router.register(r'api/accounts', AccountViewSet, basename='accounts')
router.register(r'api/users', UserViewSet, basename='users')
router.register(r'api/friendships', FriendshipViewSet, basename='friendships')

urlpatterns = [
    url('', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/tweet/(?P<tweet_id>\d+)', tweet_get_delete_view),
    url(r'^api/tweets', TweetListCreateAPIView.as_view()),
]
