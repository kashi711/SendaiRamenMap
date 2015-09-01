#!/usr/bin/env python
# -*- coding: utf-8 -*-

### 店舗名リストの食べログレビューを拾ってきて
### 形態素解析->tf-idf値の計算->tf-idfを特徴量としたk-meansクラスタリングを行うプログラム###

import numpy as np
from numpy import array
from numpy.random import *
import requests
import lxml.html
import urllib2
import re
import sys
import MeCab
import scipy.spatial.distance as dis

from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
from myapp.models import Shop,Myreview,Review,evalInfo

#textが日本語かどうかを判定
def isJapanese(text):
  text = unicode(text,'utf-8')
  flag = True
  for c in text:
    if not ord(c) > 255:
      flag = False
      break
  return flag


#すべての店の名詞出現数を表示
def show_all_nouns():
  for k,v in sorted(all_nouns_total.items(),key=lambda x:x[1]):
    if v>1: print k,v


#指定したshop_nameの名詞出現数を表示
def show_select_nouns(shop_name,noun_list):
  for tup in noun_list:
    if tup[0] == shop_name:
      nouns = tup[1]
      for k,v in sorted(nouns.items(),key=lambda x:x[1]):
        if v>40: print k,v
      break


#ある名詞が出現する店の数を数え上げる
def make_AllNounsFlag(noun_list):
  for tup in noun_list:
    nouns = tup[1]
    for k,v in sorted(nouns.items(),key=lambda x:x[1]):
      all_nouns_flag.setdefault(k,0)
      all_nouns_flag[k]+=1


#commentを形態素解析し、結果をnounsに追加して返す
def morphological_analysis(comment,nouns):
  tagger=MeCab.Tagger("-Ochasen")
  comment = comment.encode('utf-8')
  node = tagger.parseToNode(comment)
  while node:
    if unicode(node.feature.split(",")[0],'utf-8') == u"名詞" and isJapanese(node.surface):  #名詞かつ日本語のみ取得
      nouns.setdefault(node.surface,0)
      nouns[node.surface]+=1
      all_nouns_total.setdefault(node.surface,0)
      all_nouns_total[node.surface]+=1
    node = node.next
  return nouns


#shop_nameで指定された店の食べログURLを取得
def get_search_result(shop_name):
  #Yahoo検索結果(HTML)の取得
  shop_name = re.sub(' *','',shop_name)
  URL = u'http://search.yahoo.co.jp/search?p=食べログ+' + shop_name + u'&amp;ei=UTF-8'
  req = requests.get(URL)
  root = lxml.html.fromstring(req.text)
  #検索結果の<a href=""></a>によるリンクを抽出し、目的のページのURLを取得
  anchors = root.xpath('//a')
  #先頭が宮城の食べログURLと一致したものを探す
  for anchor in anchors:
    result = anchor.attrib['href']
    if re.match("http://tabelog.com/miyagi/", result):
      URL = result
      break
  print(URL)
  return URL


#指定されたURLの店のコメントを取得し,形態素解析した結果を返す
def get_nouns(URL):
  req = requests.get(URL)
  root = lxml.html.fromstring(req.text)
  #ページ内のコメントリンクを取得し，コメントを形態素解析する
  #コメントリンクの取得
  anchors = root.xpath('//a[@class="rvw-item__rvw-title-target"]')
  nouns={}
  for anchor in anchors:
    print("http://tabelog.com/" + anchor.attrib['href'])
    url_comment = "http://tabelog.com/" + anchor.attrib['href']
    request_comment = urllib2.urlopen(url_comment)
    html = unicode(request_comment.read(),'utf-8') 
    #コメント本体をhtmlの形で取得する
    m = re.search(u'<div class="rvw-item__rvw-comment" property="v:description">',html)
    comment = html[m.end():len(html)]
    m = re.search(u'</div>',comment)
    comment = comment[0:m.end()]
    #タグの消去
    comment = re.sub(r'<.*?>',' ',comment)
    #MeCabを使ってコメントを形態素解析する
    nouns = morphological_analysis(comment,nouns)
  return nouns


#tf-idfを計算する(店ごとの単語・出現数辞書nounsとshop_listの長さNを入力)
def calc_tfidf(nouns,N):
  tf = {}
  idf = {}
  tfidf = {}
  total = sum(nouns.values())    #出現した名詞の総数
  #tf-idfの計算
  for k,v in sorted(nouns.items(),key=lambda x:x[1]):
    tf[k] = float(v)/total
    idf[k] = np.log(float(N)/all_nouns_flag.setdefault(k,1))+0
    tfidf[k] = tf[k] * idf[k]
  return tfidf


#tf-idfの特徴量を作る
def make_feature(tfidf_list):
  feature_list = []
  for tfidf_tupple in tfidf_list:
    shop_name = tfidf_tupple[0]
    tfidf = tfidf_tupple[1]
    feature = array([])
    for k,v in sorted(all_nouns_total.items(),key=lambda x:x[1]):
      vec = array([tfidf.setdefault(k,0)])
      feature = np.r_[feature,vec]
    tuple1 = (shop_name,feature)
    feature_list.append(tuple1)
  return feature_list


#k-means法でクラスタリングする
def clustering(K,feature_list):
  cluster = []    #各店のクラスタ
  #クラスタの初期化
  for var in range(0,len(feature_list)):
    #cluster += [var%K]
    cluster += [randint(0,K)]
  repeat = 50          #反復回数
  
  #各クラスタの重心を初期化
  center = []    
  for k in range(0,K):
    vec = array([0]*len(feature_list[0][1]))
    center.append(vec)
    
  #k-means法
  for var in range(0,repeat):
    #重心の計算
    total = [0]*K  #各クラスタの要素数
    for k in range(0,K):
      vec = array([0]*len(feature_list[0][1]))
      center[k] = vec
    for i,feature in enumerate(feature_list):
      center[cluster[i]] = center[cluster[i]] + feature[1]
      total[cluster[i]] += 1
    for k in range(0,K):
      try:
        center[k] = center[k]/float(total[k])
      except:
        center[k] = center[k]/1.0
    #各ベクトルのクラスタ再割り当て
    for i,feature in enumerate(feature_list):
      min_dist = 10000
      new_cluster = -1
      for j,c in enumerate(center):
        dist = np.linalg.norm(feature[1]-c)
        if dist < min_dist:
          min_dist = dist
          new_cluster = j
      cluster[i] = new_cluster
  return cluster



if __name__ == "__main__":
  #Djangoのデータベースから店名を取得し、店舗名リストshopsを作成
  AllShops = Shop.objects.all()
  shops = []
  for s in AllShops:
    shops.append(s.name)
    
  noun_list = []  #店名と名詞出現数のタプルのリスト
  global all_nouns_total,all_nouns_flag
  all_nouns_total = {}  #すべての店の名詞出現数辞書
  all_nouns_flag = {}    #名詞がいくつの店で出現したかを保存する辞書
  
  
  for shop_name in shops:
    URL = get_search_result(shop_name)
    URL = URL + "dtlrvwlst/"	#取得したURLにコメントページのURLを追加する
    nouns = get_nouns(URL)
    tuple1 = (shop_name,nouns)
    noun_list.append(tuple1)	#店名と名詞の出現数をタプルにして保存する
    for k,v in sorted(nouns.items(),key=lambda x:x[1]):
      if v>1: print k,v
    print (tuple1[0])

  #tf-idfの計算で使うAllNounsFlagを作成
  make_AllNounsFlag(noun_list)

  #各店舗ごとのtf-idfを計算し、店名とセットでリストに保存する
  tfidf_list = []
  for t in noun_list:
    tfidf = calc_tfidf(t[1],len(shops))
    tuple1 = (t[0],tfidf)
    tfidf_list.append(tuple1)
    for k,v in sorted(tfidf.items(),key=lambda x:x[1]):
      print k,v
    print

  #クラスタリングをするため特徴量として整形
  feature_list = make_feature(tfidf_list)

  #各店舗ごとにクラスタをデータベースに登録
  print
  cluster = clustering(5,feature_list)
  print cluster
  for i,c in enumerate(cluster):
    s = Shop.objects.get(pk=i+1)
    s.cluster = c
    s.save()

  #各店舗ごとにtf-idfの上位20位までをタグとしてデータベースに登録
  for num in range(68,69):  
    for i,shop in enumerate(shops):
      if not i==num:
        continue
      keywords = []
      tfidf = calc_tfidf(noun_list[i][1],len(shops))
      for k,v in sorted(tfidf.items(),key=lambda x:x[1],reverse=True):
        print k,v
        if len(keywords)>=20:
          break
        keyword = k
        flag = False
        for i,var in enumerate(keywords):
          if re.search(keyword,var):
            flag = True
          if re.search(var,keyword):
            keywords[i] = keyword
            flag = True
        if not flag:
          keywords.append(keyword)
      keywords_text = ''
      for keyword in keywords:
        print keyword
        keywords_text = keywords_text + "," + keyword
    s = Shop.objects.get(pk=num+1)
    s.tags = keywords_text
    s.save()

