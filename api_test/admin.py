# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class CaseParemsInfoInLine(admin.StackedInline):
    admin.StackedInline.extra = 0
    model = CaseParemsInfo


class TestCaseInfoInLine(admin.StackedInline):
    admin.StackedInline.extra = 0
    model = TestCaseInfo


class RequestMethodAdmin(admin.ModelAdmin):
    list_display = ('method_name', 'method_desc', 'create_time',)


class RequestUrlInfoAdmin(admin.ModelAdmin):
    list_display = ('request_name', 'request_url', 'simple_desc', 'status',)
    inlines = [TestCaseInfoInLine]


class TestCaseInfoAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'belong_request', 'author', 'active', 'status',)
    inlines = [CaseParemsInfoInLine]


class CaseParemsInfoAdmin(admin.ModelAdmin):
    list_display = ('param_key', 'param_value', 'belong_case', 'simple_desc',)


# Register your models here.
admin.site.register(RequestMethod, RequestMethodAdmin)
admin.site.register(RequestUrlInfo, RequestUrlInfoAdmin)
admin.site.register(TestCaseInfo, TestCaseInfoAdmin)
# admin.site.register(CaseParemsInfo, CaseParemsInfoAdmin)
