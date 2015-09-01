# -*- coding: utf-8 -*-
### ホットペッパーのAPIからXMLを取得し、店舗の基本情報をデータベースに登録する
import urllib2
from xml.etree.ElementTree import *
from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User
from myapp.models import Shop,Myreview,Review,evalInfo

#キーは登録したアカウントのものを使う
response = urllib2.urlopen('http://api.hotpepper.jp/GourmetSearch/V110/?key=?????????&ShopAddress=%E4%BB%99%E5%8F%B0&genre=G013&Count=100')
xmlString = response.read()
elem = fromstring(xmlString)
length = int(elem.find(".//NumberOfResults").text)
#nameの取得
name_list = []
for e in elem.getiterator("ShopName"):
  name_list.append(e.text)


#addressの取得
address_list = []
for e in elem.getiterator("ShopAddress"):
  address_list.append(e.text)


#openingの取得
opening_list = []
for e in elem.getiterator("Open"):
  opening_list.append(e.text)


#closedの取得
closed_list = []
for e in elem.getiterator("Close"):
  closed_list.append(e.text)


#photoの取得
photo_list = []
for e in elem.getiterator("PcMiddleImg"):
  photo_list.append(e.text)


#latの取得
lat_list = []
for e in elem.getiterator("Latitude"):
  lat_list.append(e.text)


#lngの取得
lng_list = []
for e in elem.getiterator("Longitude"):
  lng_list.append(e.text)


#店情報の登録
temp_list = range(0,length)
for index in temp_list:
  shop = Shop(name=name_list[index],tell='',address=address_list[index], opening=opening_list[index],closed=closed_list[index],photo=photo_list[index],lat=lat_list[index],lng=lng_list[index])
  shop.save()
  eval_info = evalInfo(shop = shop)
  eval_info.save()
  



