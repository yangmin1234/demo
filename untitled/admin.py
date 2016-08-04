# -*- coding: utf-8 -*-
from untitled.models import Holiday, DateChoose

__author__ = 'Administrator'
from django.contrib import admin
class HolidayAdmin(admin.ModelAdmin):

	fieldsets = [(None, {'fields': ('name', 'start_time', 'end_time',)}), ]
	search_fields = ('name',)
	list_display = ('name', 'start_time', 'end_time', 'create_time', )

	def has_add_permission(self, request):
		return True

	def has_delete_permission(self, request, obj=None):
		return True

	# def save_model(self, request, obj, form, change):
	# 	"""
	# 	保存分组信息
	# 	:param request:
	# 	:param obj:
	# 	:param form:
	# 	:param change:
	# 	:return:
	# 	"""
	# 	obj.create_staff = request.user.staff
	# 	obj.save()

class DateChooseAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ('room_name', 'start_time', 'end_tiem',)}), ]
	search_fields = ('room_name',)
	list_display = ('room_name', 'start_time', 'end_tiem', )

admin.site.register(Holiday, HolidayAdmin)
admin.site.register(DateChoose, DateChooseAdmin)
