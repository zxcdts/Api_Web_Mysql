# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class BaseTable(models.Model):
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'


class RequestMethod(BaseTable):
    class Meta:
        verbose_name = 'RequestMethod'
        db_table = 'RequestMethod'

    method_name = models.CharField(u'请求方式', max_length=50)
    method_desc = models.CharField(u'请求描述', max_length=100, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.method_name


class RequestUrlInfo(BaseTable):
    class Meta:
        verbose_name = 'RequestUrlInfo'
        db_table = 'RequestUrlInfo'

    request_name = models.CharField(u'请求名称', max_length=50)
    request_url = models.CharField(u'请求地址', max_length=50)
    # lifting_time = models.DateTimeField()
    request_method = models.ForeignKey(RequestMethod, on_delete=models.CASCADE)
    simple_desc = models.CharField(u'请求描述', max_length=100, null=True)
    other_desc = models.CharField(max_length=100, null=True)
    status = models.IntegerField(u'请求状态', default=1)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.request_url


class TestCaseInfo(BaseTable):
    class Meta:
        verbose_name = 'TestCaseInfo'
        db_table = 'TestCaseInfo'

    type = models.IntegerField(u'用例类型', default=1)
    name = models.CharField(u'用例名称', max_length=50)
    belong_project = models.CharField(u'用例所属项目', max_length=50)
    belong_request = models.ForeignKey(RequestUrlInfo, on_delete=models.CASCADE)
    # include = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=20)
    # request = models.TextField()
    active = models.IntegerField(u'用例是否执行', default=1)
    status = models.IntegerField(u'用例状态', default=1)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name


class CaseParemsInfo(BaseTable):
    class Meta:
        verbose_name = 'CaseParemsInfo'
        db_table = 'CaseParemsInfo'

    param_key = models.CharField(u'请求key', max_length=50)
    param_value = models.CharField(u'请求value', max_length=50)
    belong_case = models.ForeignKey(TestCaseInfo, on_delete=models.CASCADE)
    simple_desc = models.CharField(u'简要描述', max_length=100, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.param_key
