# author: HuYong  # coding=utf-8
from django.conf.urls import url, include
from rest_framework import routers

import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
	url(r'^user/$', views.UserList.as_view()),
	url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^user_delete/(?P<pk>[0-9]+)/$', views.DeleteUser.as_view()),
]
