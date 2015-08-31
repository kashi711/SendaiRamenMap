from django.contrib import admin
from myapp.models import Shop,Myreview,Review,evalInfo,BusinessHour
from django.contrib.auth.models import User

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 3

class evalInfoInline(admin.TabularInline):
    model = evalInfo
    extra = 0

class BusinessHourInline(admin.TabularInline):
    model = BusinessHour
    extra = 0


class ShopAdmin(admin.ModelAdmin):
    inlines = (ReviewInline,evalInfoInline,BusinessHourInline)

admin.site.register(Shop,ShopAdmin)
admin.site.register(Myreview)
admin.site.register(Review)
admin.site.register(evalInfo)
