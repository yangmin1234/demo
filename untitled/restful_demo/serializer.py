# author: ym  # coding=utf-8
from rest_framework import serializers

from untitled.restful_demo.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("id", "username", "password")
