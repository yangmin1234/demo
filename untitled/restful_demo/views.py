# -*- coding:utf-8 -*
import json

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import viewsets

from untitled.restful_demo.models import User
from untitled.restful_demo.serializer import UserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
	"""
		获取用户列表或新增用户
	"""
	serializer_class = UserSerializer
	if request.method == "GET":
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		print request.body
		serializer = UserSerializer(data=json.loads(request.body))
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
class UserList(ListAPIView):
	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.order_by('-id')

class UserDetail(RetrieveAPIView):
	# serializer_class = UserSerializer

	def get_object(self):
		return get_object_or_404(User, pk=self.kwargs.get("pk"))

class DeleteUser(DestroyAPIView):

	def delete(self, request, *args, **kwargs):
		return get_object_or_404(User, pk=self.kwargs.get("pk")).delete()



class UserViewSet(viewsets.ModelViewSet):
	"""
	允许查看和编辑user 的 API endpoint
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer



@api_view(['GET', 'PUT', 'DELETE'])
def User_detial(request, pk):
	try:
		user = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET":
		serializer = UserSerializer(user)
		return Response(serializer.data)

	elif request.method == "PUT":
		serializer = UserSerializer(user, data=json.loads(request.body))
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == "DELETE":
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
