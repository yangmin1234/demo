# -*- coding: utf-8 -*-
import json
import logging
from lxml import etree
import urllib2
import bs4
import datetime
import time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import requests
# logger = logging.getLogger(__name__)
import sys
from untitled.models import Holiday, DateChoose, support

logger = logging.getLogger('spider')

# def catch_info(url, page_no):
# 	"""
# 	对传入的页面进行抓取,如果未传入页码则对所有数据进行抓取。
# 	:param url:
# 	:param page_no:
# 	:return:
# 	"""
# 	if not page_no:
# 		page_no = 1
# 	page_no = int(page_no)
# 	while page_no <= 76604:
# 		page_no = catch_page_info(url, page_no)

# 一共两种方法，一种用request,另一种是urlopen,都能爬到页面，剩下的就是对页面的分析了
def catch_page_info(request):
	"""
	对传入的网页地址和页码信息进行抓取。
	:param url:
	:param page_no:
	:return:
	"""
	# if page_no:
	# 	url = "%s?page=%s" % (url, page_no)
	# company_list_one = CompanyInfo.objects.filter(page_no=page_no)
	# if company_list_one:
	# 	# print "%s页数据已经存在" % page_no
	# 	logger.info("%s Data already exists" % page_no)
	# 	return page_no + 1
	url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=西湖&oq=西湖&rsp=-1"
	# response = requests.get(url, timeout=200)
	# respHtml = response.text
	# soup = bs4.BeautifulSoup(respHtml)
	# a_list = soup.select('a')
	# for a in a_list:
	# 	try:
	# 		if 'b_and' in a['id']:
	# 			myurl = a['href']
	# 	except:
	# 		pass
	content=urllib2.urlopen(url).read()
	# typeEncode = sys.getfilesystemencoding()
	# json_drive_ret = json.loads(content)
	# html = content.decode("utf-8").encode(typeEncode)
	# soup=BeautifulSoup(html,”lxml”)
	# return render_to_response("aa.html", locals(), context_instance=RequestContext(request))
	return HttpResponse(content)
	# soup = bs4.BeautifulSoup(respHtml)
	# tds = [a.text for a in soup.select('tr.rowOdd td')]
	# code = ""
	# name = ""
	# phone = ""
	# address = ""
	# i = 0
	# # company_list_two = CompanyInfo.objects.filter(page_no=page_no)
	# # if company_list_two:
	# # 	# print "%s页数据已经存在" % page_no
	# # 	logger.info("%s Data already exists" % page_no)
	# # 	return page_no + 1
	# after = datetime.datetime.now()
	# gap = (after - before).seconds
	# if tds:
	# 	for td in tds:
	# 		i += 1
	# 		if i == 1:
	# 			code = td
	# 		elif i == 2:
	# 			name = td
	# 		elif i == 3:
	# 			phone = td
	# 		elif i == 4:
	# 			address = td
	# 			# company = CompanyInfo(code=code, name=name, phone=phone, address=address, page_no=page_no)
	# 			# company.save()
	# 			i = 0
	# 	after2 = datetime.datetime.now()
	# 	gap2 = (after2 - after).seconds
	# 	# print("%s page,load %s sec,save %s sec,successes %s" % (page_no, gap,gap2,after2))
	# 	logger.info("%s page,load %s sec,save %s sec,successes %s" % (page_no, gap,gap2,after2))
	# 	return page_no + 1
	# else:
	# 	# print("%s page,load %s sec load error" % (page_no, gap))
	# 	logger.info("%s page,load %s sec load error" % (page_no, gap))
	# 	time.sleep(10)
	# 	catch_page_info(url, page_no)

def day_count(request):
	day_list = DateChoose.objects.all()[0]
	holiday_count = weekday_count = usually_count = 0
	days = (day_list.end_tiem-day_list.start_time).days
	for i in range(days+1):
		day = day_list.start_time + datetime.timedelta(days=i)
		d_type = day_type(day)
		if d_type == "holiday":
			holiday_count += 1
		elif d_type == "weekend":
			weekday_count += 1
		else:
			usually_count += 1
	return render_to_response("aa.html", locals(), context_instance=RequestContext(request))



def day_type(time_a):
	# day = "2016-02-16"
	# time_a = datetime.date(int(day[:4]), int(day[5:7]), int(day[8:]))
	holiday_list = Holiday.objects.filter(del_status=Holiday.DEL_STATUS_AVAILABLE, start_time__lte=time_a, end_time__gte=time_a)
	weekday = time_a.weekday()
	if holiday_list:
		return "holiday"
		# a = "holiday"
	elif weekday == 5 or weekday == 6:
		return "weekend"
		# a = "weekend"
	else:
		return "usually"
		# a = "usually"
	# return render_to_response("aa.html", locals(), context_instance=RequestContext(request))

def test_kuaidi(request):
	url = "http://www.kuaidi100.com/applyurl?key=9ac89689dcb6e34c&com=huitongkuaidi&nu=70074806041046"
	json_str = urllib2.urlopen(url).read()
	# json_ret = json.loads(json_str)
	print json_str
	return render_to_response("aa.html", locals(), context_instance=RequestContext(request))

# 步行规划
WALKING_URL = "http://restapi.amap.com/v3/direction/walking?origin=%s&destination=%s&output=json&key=98e5dfe0d5f1e7a83b489c586242e2ca"
# 驾车规划
DRIVING_URL = "http://restapi.amap.com/v3/direction/driving?key=98e5dfe0d5f1e7a83b489c586242e2ca&origin=%s&destination=%s&output=json&originid=&destinationid=&extensions=base&strategy=0&waypoints=&avoidpolygons=&avoidroad="
# 行驶距离测量
DRIVEING_DISTANCE_URL = "http://restapi.amap.com/v3/distance?origins=%s&destination=%s&output=json&key=98e5dfe0d5f1e7a83b489c586242e2ca"
# 公交路径规划
TRANSIT_URL = "http://restapi.amap.com/v3/direction/transit/integrated?origin=%s&destination=%s&city=杭州&output=json&key=98e5dfe0d5f1e7a83b489c586242e2ca"
def test_webapi(request):
	drive_url = DRIVING_URL % ("120.02634,30.123708", "120.16349,30.271074")
	json_drive_str = urllib2.urlopen(drive_url).read()
	json_drive_ret = json.loads(json_drive_str)
	if json_drive_ret.get("status") == "1":
		drive_distance = json_drive_ret.get("route").get("paths")[0].get("distance")
		drive_duration = json_drive_ret.get("route").get("paths")[0].get("duration")
	walk_url = WALKING_URL % ("120.02634,30.123708", "120.16349,30.271074")
	json_walk_str = urllib2.urlopen(walk_url).read()
	json_walk_ret = json.loads(json_walk_str)
	if json_walk_ret.get("status") == "1":
		walk_distance = json_walk_ret.get("route").get("paths")[0].get("distance")
		walk_duration = json_walk_ret.get("route").get("paths")[0].get("duration")
	drive_distance_url = DRIVEING_DISTANCE_URL % ("120.02634,30.123708", "120.16349,30.271074")
	json_str = urllib2.urlopen(drive_distance_url).read()
	json_ret = json.loads(json_str)
	if json_ret.get("status") == "1":
		distance = json_ret.get("results")[0].get("distance")
		duration = json_ret.get("results")[0].get("duration")
	trans_url = TRANSIT_URL % ("120.02634,30.123708", "120.16349,30.271074")
	json_trans_str = urllib2.urlopen(trans_url).read()
	json_trans_ret = json.loads(json_trans_str)
	if json_trans_ret.get("status") == "1":
		distance = json_trans_ret.get("route").get("distance")
		taxi_cost = json_trans_ret.get("route").get("taxi_cost")
		trans_list = json_trans_ret.get("route").get("transits")
		for trans in trans_list:
			trans_distance = trans["distance"]
			trans_duration = trans["duration"]
	return render_to_response("aa.html", locals(), context_instance=RequestContext(request))


def test_jsapi(request):
	point_list = [[(116.387271, 39.922501), (116.368904, 39.923423)], [(116.306015, 39.979809), (116.490572, 39.806862)]]
	return render_to_response("test_js.html", locals(), context_instance=RequestContext(request))

def test_map(request):
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))

api_url = "http://127.0.0.1:8003/api/user/"
def test_api(request):
	data = urllib.urlopen(api_url).read()
	return HttpResponse(data)


import time
import urllib
import re
api = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s"  # api地址
string = "1234567890"                   # 所有字母
string_len = len(string)                                          # 长度
import os
module_dir = os.path.dirname(__file__)  # get current directory
fname = os.path.join(module_dir, 'name.txt')
# fname = 'name.txt'                                                # 还没被注册的域名写入该文件
suffix = '.com'                                                   # 域名后缀
domain_lenth_range = range(3, 5)                                  # 字母组合的长度，3到5但不包括5


def min(num):
	"""初始化第一个值数字列表"""
	name = []
	for i in range(num):
		name.append(0)
	return name


def max(num, max_num):
	"""返回最大的值数字列表"""
	name = []
	for i in range(num):
		name.append(max_num)
	return name


def num_2_string(name, string):
	"""将数字列表转化为字母组合列表"""
	new_name = []
	for i in name:
		new_name.append(string[i])
	return ''.join(new_name)

ip_daili = {"http": "http://183.129.178.14:8080"}
def is_ava(domain):
	"""判断该域名是否被注册"""
	try:
		data = urllib.urlopen(api % domain, proxies=ip_daili).read()
		ava_pattern = re.compile(r'<original>(.*) : .*</original>')
		perm_pattern = re.compile(r'Forbidden')
		result = ava_pattern.findall(data)
		if '210' in result:
			print '%s ---------> Ok' % domain
			return True
		elif '211' in result:
			print '%s ---------> No' % domain
			return False
		else:
			print 'Forbidden'
			return False
	except:
		return False


def domain_name(num):
	"""域名组合生成器"""
	name = min(num)
	last = max(num, string_len - 1)
	while True:
		yield num_2_string(name, string)
		if name == last:
			break
		name[num - 1] += 1
		while string_len in name:
			index = name.index(string_len)
			name[index] = 0
			name[index - 1] += 1

def run(domain_lenth):
	"""执行，如果每被注册就写到文件中"""
	f = open(fname, 'a')
	for domain in domain_name(domain_lenth):
		domain += suffix
		if is_ava(domain):
			f.write('%s\n' % domain)
			f.flush()
		time.sleep(0.5)


def test_canvas(request):
	return render_to_response("test_canvas.html", locals(), context_instance=RequestContext(request))
