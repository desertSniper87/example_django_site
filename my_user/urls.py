from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, MutualFriendshipList, PendingFriendshipList, FriendshipDetail, \
    FriendshipCreate


USER_ROUTER = routers.DefaultRouter()
USER_ROUTER.register(r'', UserViewSet, base_name='user')

urlpatterns = [
    url(
        r'^friendship/mutual/(?P<user>[0-9]+)$',
        MutualFriendshipList.as_view(),
        name='friendship-list-mutual'
    ),
    url(r'^friendship/pending/$', PendingFriendshipList.as_view(), name='friendship-list-pending'),
    url(r'^friendship/(?P<pk>[0-9]+)/$', FriendshipDetail.as_view(), name='friendship-detail'),
    url(r'^friendship/$', FriendshipCreate.as_view(), name='friendship-list'),
    url(r'^', include(USER_ROUTER.urls)),
]
