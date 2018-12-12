# -*- coding: utf-8 -*-

__author__ = 'ym'
from django.db import models

class Holiday(models.Model):

	DEL_STATUS_AVAILABLE = 0
	DEL_STATUS_NOT_AVAILABLE = 0
	DEL_STATUS = {DEL_STATUS_AVAILABLE: "可用", DEL_STATUS_NOT_AVAILABLE: "不可用"}

	name = models.CharField(max_length=50, verbose_name="假日名称")
	start_time = models.DateField(verbose_name="假日开始时间")
	end_time = models.DateField(verbose_name="假日结束时间")
	create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	del_status = models.IntegerField(default=0, choices=DEL_STATUS.items(), verbose_name="删除状态")

	def __unicode__(self):
		return self.name


class DateChoose(models.Model):
	room_name = models.CharField(max_length=50, verbose_name="房间名称")
	start_time = models.DateField(verbose_name="开始入住时间")
	end_tiem = models.DateField(verbose_name="离开时间")


class support(models.Model):
	name = models.CharField(max_length=200, verbose_name="昵称")
	price = models.CharField(max_length=20, verbose_name="金额")
	image = models.CharField(max_length=500, verbose_name="头像")



