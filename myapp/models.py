from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
  name = models.CharField(max_length=100)
  tell = models.CharField(max_length=20)
  address = models.CharField(max_length=100)
  opening = models.CharField(max_length=100)
  closed = models.CharField(max_length=100)
  photo = models.CharField(max_length=100)
  evaluation = models.DecimalField(decimal_places=1,max_digits=2,default=0.0)
  int_eval = models.IntegerField(default=0)
  lat = models.DecimalField(decimal_places=6,max_digits=9)
  lng = models.DecimalField(decimal_places=6,max_digits=9)
  cluster = models.IntegerField(default=0)
  tags = models.CharField(max_length=300,default="")
  def __unicode__(self):
    return u"{}".format(self.name)


class Myreview(models.Model):
  user = models.ForeignKey(User)
  shop_id = models.IntegerField()
  title = models.CharField(max_length=100)
  comment = models.TextField()
  evaluation = models.IntegerField()
  pub_date = models.DateTimeField()
  def __unicode__(self):
    return u"{}".format(self.user)


class Review(models.Model):
  shop = models.ForeignKey(Shop)
  title = models.CharField(max_length=100)
  comment = models.TextField()
  evaluation = models.IntegerField()
  pub_date = models.DateTimeField()
  name = models.CharField(max_length=100)
  def __unicode__(self):
    return u"{}".format(self.title)

class evalInfo(models.Model):
  shop = models.ForeignKey(Shop)
  total = models.IntegerField(default=0)
  evaluation = models.DecimalField(decimal_places=1,max_digits=2,default=0.0)
  int_eval = models.IntegerField(default=0)
  one = models.IntegerField(default=0)
  two = models.IntegerField(default=0)
  three = models.IntegerField(default=0)
  four = models.IntegerField(default=0)
  five = models.IntegerField(default=0)


class BusinessHour(models.Model):
  shop = models.ForeignKey(Shop)
  MonOpen1 = models.TimeField(default = "0:00:00")
  MonClose1 = models.TimeField(default = "0:00:00")
  MonOpen2 = models.TimeField(default = "0:00:00")
  MonClose2 = models.TimeField(default = "0:00:00")
  MonOpen3 = models.TimeField(default = "0:00:00")
  MonClose3 = models.TimeField(default = "0:00:00")
  TueOpen1 = models.TimeField(default = "0:00:00")
  TueClose1 = models.TimeField(default = "0:00:00")
  TueOpen2 = models.TimeField(default = "0:00:00")
  TueClose2 = models.TimeField(default = "0:00:00")
  TueOpen3 = models.TimeField(default = "0:00:00")
  TueClose3 = models.TimeField(default = "0:00:00")
  WedOpen1 = models.TimeField(default = "0:00:00")
  WedClose1 = models.TimeField(default = "0:00:00")
  WedOpen2 = models.TimeField(default = "0:00:00")
  WedClose2 = models.TimeField(default = "0:00:00")
  WedOpen3 = models.TimeField(default = "0:00:00")
  WedClose3 = models.TimeField(default = "0:00:00")
  ThuOpen1 = models.TimeField(default = "0:00:00")
  ThuClose1 = models.TimeField(default = "0:00:00")
  ThuOpen2 = models.TimeField(default = "0:00:00")
  ThuClose2 = models.TimeField(default = "0:00:00")
  ThuOpen3 = models.TimeField(default = "0:00:00")
  ThuClose3 = models.TimeField(default = "0:00:00")
  FriOpen1 = models.TimeField(default = "0:00:00")
  FriClose1 = models.TimeField(default = "0:00:00")
  FriOpen2 = models.TimeField(default = "0:00:00")
  FriClose2 = models.TimeField(default = "0:00:00")
  FriOpen3 = models.TimeField(default = "0:00:00")
  FriClose3 = models.TimeField(default = "0:00:00")
  SatOpen1 = models.TimeField(default = "0:00:00")
  SatClose1 = models.TimeField(default = "0:00:00")
  SatOpen2 = models.TimeField(default = "0:00:00")
  SatClose2 = models.TimeField(default = "0:00:00")
  SatOpen3 = models.TimeField(default = "0:00:00")
  SatClose3 = models.TimeField(default = "0:00:00")
  SunOpen1 = models.TimeField(default = "0:00:00")
  SunClose1 = models.TimeField(default = "0:00:00")
  SunOpen2 = models.TimeField(default = "0:00:00")
  SunClose2 = models.TimeField(default = "0:00:00")
  SunOpen3 = models.TimeField(default = "0:00:00")
  SunClose3 = models.TimeField(default = "0:00:00")













