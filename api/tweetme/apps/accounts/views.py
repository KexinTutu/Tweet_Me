from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tweetme.apps.accounts.serializers import SignupSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class AccountViewSet(viewsets.ViewSet):
    serializer_class = SignupSerializer

    @action(methods=['POST'], detail=False)
    def sign_up(self, request):
        serializer = SignupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'errors': serializer.errors
            }, status=400)

        user = serializer.save()
        login(request, user)
        return Response(status=201)
