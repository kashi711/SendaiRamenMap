# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from myapp.models import Shop,Myreview,Review,evalInfo,BusinessHour
import re
from django.utils import timezone
import datetime
from datetime import date

# Create your views here.
# 最初のページ
def root(request):
    return HttpResponseRedirect("/index/")

def index(request):
    shop_list = Shop.objects.all()
    username=request.user.username
    context = {'username':username,'shop_list':shop_list}
    return render(request, 'myapp/index_ver4.html', context)

# 検索結果
def result(request):
    button = request.POST['ButtonType']
    username=request.user.username
    request_keyword = request.POST['keyword']
    #キーワード検索の処理
    if button == "search":
      if len(request_keyword) < 1:
          return HttpResponseRedirect("../index/")
      keywords = filter(lambda w: len(w) > 0, re.split(r'\s', request_keyword))
      shop_list = Shop.objects.all()
      result_list = []
      for shop in shop_list:
        tags = shop.tags
        tags = tags.split(",")
        tags.append(shop.name)
        AppendFlags = [False]*len(keywords)
        for i,keyword in enumerate(keywords):
          for tag in tags:
            if re.search(keyword , tag):
              AppendFlags[i] = True

        flag = True
        for AppendFlag in AppendFlags:
          if not AppendFlag:
            flag = False 
            break
        if flag:
          result_list.append(shop)

      context = {'username':username,'shop_list':result_list,'keyword':request_keyword}
      return render(request, 'myapp/result.html', context)

    #開店中店舗検索の処理
    else:
        #現在の時刻
        d = datetime.datetime.today()
        now_time = datetime.time(d.hour, d.minute, d.second)
        #現在の曜日(月曜0～日曜6)
        week = date(d.year,d.month,d.day).weekday()
        
        if len(request_keyword) < 1:
          shop_list = Shop.objects.all()
        else:
          keywords = filter(lambda w: len(w) > 0, re.split(r'\s', request_keyword))
          shop_list = Shop.objects.all()
          result_list = []
          for shop in shop_list:
            tags = shop.tags
            tags = tags.split(",")
            tags.append(shop.name)
            AppendFlags = [False]*len(keywords)
            for i,keyword in enumerate(keywords):
              for tag in tags:
                if re.search(keyword , tag):
                  AppendFlags[i] = True

            flag = True
            for AppendFlag in AppendFlags:
              if not AppendFlag:
                flag = False 
                break
            if flag:
              result_list.append(shop)
          shop_list = result_list  

        result_list = []
        #各曜日で現在営業中かどうかを判定
        if week==0:
          for shop in shop_list:
            businessHour = BusinessHour.objects.get(shop=shop)
            if now_time>=businessHour.MonOpen1 and now_time<businessHour.MonClose1:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.MonOpen2 and now_time<businessHour.MonClose2:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.MonOpen3 and now_time<businessHour.MonClose3:
              result_list.append(shop)
              continue

        elif week==1:
          for shop in shop_list:
            businessHour = BusinessHour.objects.get(shop=shop)
            if now_time>=businessHour.TueOpen1 and now_time<businessHour.TueClose1:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.TueOpen2 and now_time<businessHour.TueClose2:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.TueOpen3 and now_time<businessHour.TueClose3:
              result_list.append(shop)
              continue

        elif week==2:
          for shop in shop_list:
            businessHour = BusinessHour.objects.get(shop=shop)
            if now_time>=businessHour.WedOpen1 and now_time<businessHour.WedClose1:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.WedOpen2 and now_time<businessHour.WedClose2:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.WedOpen3 and now_time<businessHour.WedClose3:
              result_list.append(shop)
              continue

        elif week==3:
          for shop in shop_list:
            businessHour = BusinessHour.objects.get(shop=shop)
            if now_time>=businessHour.ThuOpen1 and now_time<businessHour.ThuClose1:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.ThuOpen2 and now_time<businessHour.ThuClose2:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.ThuOpen3 and now_time<businessHour.ThuClose3:
              result_list.append(shop)
              continue

        elif week==4:
          for shop in shop_list:
            businessHour = BusinessHour.objects.get(shop=shop)
            if now_time>=businessHour.FriOpen1 and now_time<businessHour.FriClose1:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.FriOpen2 and now_time<businessHour.FriClose2:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.FriOpen3 and now_time<businessHour.FriClose3:
              result_list.append(shop)
              continue

        elif week==5:
          for shop in shop_list:
            businessHour = BusinessHour.objects.get(shop=shop)
            if now_time>=businessHour.SatOpen1 and now_time<businessHour.SatClose1:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.SatOpen2 and now_time<businessHour.SatClose2:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.SatOpen3 and now_time<businessHour.SatClose3:
              result_list.append(shop)
              continue

        elif week==6:
          for shop in shop_list:
            businessHour = BusinessHour.objects.get(shop=shop)
            if now_time>=businessHour.SunOpen1 and now_time<businessHour.SunClose1:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.SunOpen2 and now_time<businessHour.SunClose2:
              result_list.append(shop)
              continue
            elif now_time>=businessHour.SunOpen3 and now_time<businessHour.SunClose3:
              result_list.append(shop)
              continue

        print len(result_list)
        if len(request_keyword) < 1:
          context = {'username':username,'shop_list':result_list}
        else:
          context = {'username':username,'shop_list':result_list,'keyword2':request_keyword}
        return render(request, 'myapp/result.html', context)

# ログインページ
def loginpage(request):
    context = {}
    return render(request, 'myapp/login.html', context)

# ログインページ（エラー１）
def loginpage_error(request):
    error_message = 'ユーザ名かパスワードが違います'
    context = {'error_message':error_message}
    return render(request, 'myapp/login.html', context)

# ログイン処理
def enter(request):
  try:
    user = authenticate(username=request.POST['name'], password=request.POST['password'])
    if user is not None and user.is_active:
      login(request, user)
      return HttpResponseRedirect("../index/")
    else:
      return HttpResponseRedirect("../loginpage_error/")
  except:
    return HttpResponse("login error")

# アカウント作成ページ
def make(request):
    context = {}
    return render(request, 'myapp/make.html', context)

# アカウント作成ページ（エラー1）
def make_error1(request):
    error_message = 'ユーザ名かパスワードが入力されていません'
    context = {'error_message':error_message}
    return render(request, 'myapp/make.html', context)

# アカウント作成ページ（エラー2）
def make_error2(request):
    error_message = '入力されたユーザ名は既に使用されています'
    context = {'error_message':error_message}
    return render(request, 'myapp/make.html', context)

# アカウント作成処理
def makeAccount(request):
  try:
    name = request.POST['name']
    password = request.POST['password']
    
    if len(name) < 1 or len(password) < 1:
      return HttpResponseRedirect("../make_error1/")
    
    if User.objects.filter(username=name):
      return HttpResponseRedirect("../make_error2/")
    else:
      user = User.objects.create_user(name, '', password)
      user.save()
      login( request, authenticate(username=name, password=password) )
      return HttpResponseRedirect("../index/")
  except:
    return HttpResponse("Error")

# ログアウト処理
def out(request):
  logout(request)
  return HttpResponseRedirect("../index/")

#類似店検索ページ
def similarity(request, shop_id):
  username=request.user.username
  request_shop = Shop.objects.get(pk=shop_id)
  cluster = request_shop.cluster
  shops = Shop.objects.all()
  result_list = []
  for shop in shops:
    if shop.cluster == cluster:
      result_list.append(shop)
  context = {'username':username,'shop_list':result_list,'request_shop':request_shop.name}
  return render(request, 'myapp/result.html', context)

# 詳細ページ
def detail(request, shop_id):
  username=request.user.username
  shop = Shop.objects.get(pk=shop_id)
  evaluationInfo = evalInfo.objects.get(shop = shop)
  bbs_list = shop.review_set.order_by('-pub_date')[:5]
  if evaluationInfo.total < 6:
    bbs_flag = False
  else:
    bbs_flag = True
  
  #みんなのコメントに関する情報
  if evaluationInfo.total>0:
    ratio = [0,0,0,0,0]		#星5から星1の比率
    ratio[0] = evaluationInfo.five*100.0/evaluationInfo.total
    ratio[1] = evaluationInfo.four*100.0/evaluationInfo.total
    ratio[2] = evaluationInfo.three*100.0/evaluationInfo.total    
    ratio[3] = evaluationInfo.two*100.0/evaluationInfo.total
    ratio[4] = evaluationInfo.one*100.0/evaluationInfo.total
  else:
    #bbsが存在しない
    ratio = [0,0,0,0,0]

  try:
    UserInfo = User.objects.get(username=username)
    my_review = UserInfo.myreview_set.filter(shop_id=shop_id)
    num_list = [5,4,3,2,1]
    error_message = ""
    if not my_review:
      #ログインしているが一度もMyレビューを使っていない場合
      my_review = "empty"
    else:
      #ログインしておりMyレビューに一度何か書き込んだ場合
      my_review = my_review[0]
      #投稿規制をかける
      my_bbs = shop.review_set.filter(name=username)
      if my_bbs:
        my_bbs = my_bbs.last()
        now_time = timezone.now()
        diff = now_time - my_bbs.pub_date
        if diff.days < 1:
          error_message = "最後の投稿から１日経過するまで投稿できません"

    context = {'username':username,'shop':shop,'my_review':my_review,'num_list':num_list,'bbs_list':bbs_list,'bbs_flag':bbs_flag,'eval':evaluationInfo,'ratios':ratio,'error_message':error_message}
  except:
    #ログインしていない場合
    context = {'username':username,'shop':shop,'bbs_list':bbs_list,'bbs_flag':bbs_flag,'eval':evaluationInfo,'ratios':ratio}
  return render(request, 'myapp/detail.html', context)



# 詳細ページ（もっと見る）
def detail_more(request, shop_id):
  username=request.user.username
  shop = Shop.objects.get(pk=shop_id)
  bbs_list = shop.review_set.order_by('-pub_date')
  bbs_flag = False
  #みんなのコメントに関する情報
  evaluationInfo = evalInfo.objects.get(shop = shop)
  if evaluationInfo.total>0:
    ratio = [0,0,0,0,0]		#星5から星1の比率
    ratio[0] = evaluationInfo.five*100.0/evaluationInfo.total
    ratio[1] = evaluationInfo.four*100.0/evaluationInfo.total
    ratio[2] = evaluationInfo.three*100.0/evaluationInfo.total    
    ratio[3] = evaluationInfo.two*100.0/evaluationInfo.total
    ratio[4] = evaluationInfo.one*100.0/evaluationInfo.total
  else:
    #bbsが存在しない
    ratio = [0,0,0,0,0]

  try:
    UserInfo = User.objects.get(username=username)
    my_review = UserInfo.myreview_set.filter(shop_id=shop_id)
    num_list = [5,4,3,2,1]
    if not my_review:
      #ログインしているが一度もMyレビューを使っていない場合
      my_review = "empty"
    else:
      #ログインしておりMyレビューに一度何か書き込んだ場合
      my_review = my_review[0]
    context = {'username':username,'shop':shop,'my_review':my_review,'num_list':num_list,'bbs_list':bbs_list,'bbs_flag':bbs_flag,'eval':evaluationInfo,'ratios':ratio}
  except:
    #ログインしていない場合
    context = {'username':username,'shop':shop,'bbs_list':bbs_list,'bbs_flag':bbs_flag,'eval':evaluationInfo,'ratios':ratio}
  return render(request, 'myapp/detail.html', context)


# Myレビュー保存処理
def preserve(request, shop_id):
  try:
    username=request.user.username
    UserInfo = User.objects.get(username=username)
    my_review = UserInfo.myreview_set.filter(shop_id=shop_id)
    title=request.POST['my_title']
    comment=request.POST['my_comment']
    evaluation=request.POST['my_eval']
    if not my_review:
      #ログインしているが一度もMyレビューを使っていない場合
      my_review = Myreview(user=UserInfo,shop_id=shop_id,title=title,comment=comment,evaluation=evaluation,pub_date=timezone.now())
      my_review.save()
    else:
      #ログインしておりMyレビューに一度何か書き込んだ場合
      my_review = Myreview.objects.get(shop_id=shop_id,user=UserInfo)
      my_review.title = title
      my_review.comment = comment
      my_review.evaluation = evaluation
      my_review.pub_date = timezone.now()
      my_review.save()
    return HttpResponseRedirect("../../detail/"+shop_id+"/#myReview")

  except:
    #ログインしていない場合
    return HttpResponseRedirect("../../index/")
    

# みんなのレビュー投稿処理
def post(request, shop_id):
  try:
    shop = Shop.objects.get(id=shop_id)
    #Reviewに対する処理
    title = request.POST['title']
    comment = request.POST['comment']
    evaluation = request.POST['eval']
    name = request.user.username
    shop.review_set.create(title=title,comment=comment,evaluation=evaluation,pub_date=timezone.now(),name=name)
    shop.save()
    
    #evalInfoに対する処理
    temp = shop.review_set.all()
    evaluationInfo = evalInfo.objects.get(shop = shop)
    evaluationInfo.total = len(temp)
    if evaluation=="1":
      evaluationInfo.one += 1
    elif evaluation=="2":
      evaluationInfo.two += 1
    elif evaluation=="3":
      evaluationInfo.three += 1
    elif evaluation=="4":
      evaluationInfo.four += 1
    elif evaluation=="5":
      evaluationInfo.five += 1
    
    Sum = evaluationInfo.one*1+evaluationInfo.two*2+evaluationInfo.three*3+evaluationInfo.four*4+evaluationInfo.five*5
    evaluationInfo.evaluation = round(Sum*1.0/evaluationInfo.total,1)
    shop.evaluation = round(Sum*1.0/evaluationInfo.total,1)
    evaluationInfo.int_eval = round(Sum*1.0/evaluationInfo.total)
    shop.int_eval = round(Sum*1.0/evaluationInfo.total)
    evaluationInfo.save()
    shop.save()

    return HttpResponseRedirect("../../detail/"+shop_id+"/#bbs")
  
  except:
    #ログインしていない場合
    return HttpResponseRedirect("../../index/")



# みんなのレビューの削除処理
def delete(request, shop_id):
  try:
    shop = Shop.objects.get(id=shop_id)
    review = Review.objects.get(id = request.POST['id'])
    evaluation = review.evaluation
    #evalInfoに対する処理
    evaluationInfo = evalInfo.objects.get(shop = shop)
    evaluationInfo.total -= 1
    if evaluation==1:
      evaluationInfo.one -= 1
    elif evaluation==2:
      evaluationInfo.two -= 1
    elif evaluation==3:
      evaluationInfo.three -= 1
    elif evaluation==4:
      evaluationInfo.four -= 1
    elif evaluation==5:
      evaluationInfo.five -= 1
    
    if evaluationInfo.total == 0:
      evaluationInfo.evaluation = 0
      shop.evaluation = 0
      evaluationInfo.int_eval = 0
      shop.int_eval = 0
    else:
      Sum = evaluationInfo.one*1+evaluationInfo.two*2+evaluationInfo.three*3+evaluationInfo.four*4+evaluationInfo.five*5
      evaluationInfo.evaluation = round(Sum*1.0/evaluationInfo.total,1)
      shop.evaluation = round(Sum*1.0/evaluationInfo.total,1)
      evaluationInfo.int_eval = round(Sum*1.0/evaluationInfo.total)
      shop.int_eval = round(Sum*1.0/evaluationInfo.total)

    evaluationInfo.save()
    shop.save()
    review.delete()
    return HttpResponseRedirect("../../detail/"+shop_id+"/#bbs")
    
  except:
    #ログインしていない場合
    return HttpResponseRedirect("../../index/")


# みんなのレビューの編集処理
def edit(request, shop_id):
  try:
    shop = Shop.objects.get(id=shop_id)
    review = Review.objects.get(id = request.POST['id'])
    #evalInfoの書き換え
    evaluationInfo = evalInfo.objects.get(shop = shop)
    old_eval = review.evaluation
    new_eval = evaluation = request.POST['eval']
    if old_eval==1:
      evaluationInfo.one -= 1
    elif old_eval==2:
      evaluationInfo.two -= 1
    elif old_eval==3:
      evaluationInfo.three -= 1
    elif old_eval==4:
      evaluationInfo.four -= 1
    elif old_eval==5:
      evaluationInfo.five -= 1

    print new_eval
    if new_eval=="1":
      evaluationInfo.one += 1
    elif new_eval=="2":
      evaluationInfo.two += 1
    elif new_eval=="3":
      evaluationInfo.three += 1
    elif new_eval=="4":
      evaluationInfo.four += 1
    elif new_eval=="5":
      evaluationInfo.five += 1

    Sum = evaluationInfo.one*1+evaluationInfo.two*2+evaluationInfo.three*3+evaluationInfo.four*4+evaluationInfo.five*5
    evaluationInfo.evaluation = round(Sum*1.0/evaluationInfo.total,1)
    shop.evaluation = round(Sum*1.0/evaluationInfo.total,1)
    evaluationInfo.int_eval = round(Sum*1.0/evaluationInfo.total)
    shop.int_eval = round(Sum*1.0/evaluationInfo.total)
    evaluationInfo.save()
    shop.save()
    #Reviewの更新
    title=request.POST['title']
    comment=request.POST['comment']
    review.title = title
    review.comment = comment
    review.evaluation = new_eval
    review.pub_date=timezone.now()
    review.save()
    return HttpResponseRedirect("../../detail/"+shop_id+"/#bbs")
  except:
    #ログインしていない場合
    return HttpResponseRedirect("../../index/")




















