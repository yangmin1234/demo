# -*- coding: utf-8 -*-
import json
from dajaxice.decorators import dajaxice_register

__author__ = 'Administrator'

@dajaxice_register()
def get_length(request, length):
	"""
	更改黄金提货的状态，目前处于废弃状态
	:param request:
	:return:
	"""
	try:
		length_result = length
		print length_result
		return json.dumps({"status": True})
	except:
		return json.dumps({"status": False})