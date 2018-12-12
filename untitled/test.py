# -*- coding: utf-8 -*-
import hashlib
import json
import urllib2
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

__author__ = 'ym'
def formatQueryParaMap(paraMap):
	"""格式化参数，签名验证过程需要使用"""
	slist = sorted(paraMap)
	buff = []
	for k in slist:
		v = paraMap[k]
		buff.append("{0}={1}".format(k, v))

	return "&".join(buff)

def test(request):
	url = "http://127.0.0.1:8000/card_api/api/"
	dict_data = {"key": "000026", "appsecret": "abcdefg123456", "commodity": "15003", "timestamp": str(time.time()), "phone": "18868196242", "number": "30M", "trade_id": "123456789", "notify_url": "http://127.0.0.1:8003/test_callback/"}
	format_string = formatQueryParaMap(dict_data)
	sign_string = hashlib.md5(format_string).hexdigest()
	del dict_data['appsecret']
	upload_string = formatQueryParaMap(dict_data)
	upload_string += ("&sign="+sign_string)
	url += ("?" + upload_string)
	data = json.loads(urllib2.urlopen(url).read())

	return HttpResponse(data)

@csrf_exempt
def test_callback(request):
	receive_msg = request.body
	receive_msg = json.loads(receive_msg)
	# receive_msg = request.POST
	reply_data = "success"
	return HttpResponse(reply_data, content_type="application/xml")


def test_a(request):
	# list_1 = [1, 2, 3, 4]
	# list_2 = [1, 2, 3, 4]
	# list_3 = [1, 2, 3, 4]
	# list_4 = [1, 2, 3, 4]
	# for idx, item in enumerate(list_1):
	# 	del item
	# for idx, item in enumerate(list_2):
	# 	list_2.remove(item)
	#
	# for idx, item in enumerate(list_3[:]):
	# 	list_3.remove(item)
	# for idx, item in enumerate(list_4):
	# 	list_4.pop(idx)
	funcs = []
	results = []
	for x in range(7):
		def some_func():
			return x
		funcs.append(some_func)
		results.append(some_func())
		funcs_results = [func() for func in funcs]
	print results, funcs_results
	return HttpResponse("success")