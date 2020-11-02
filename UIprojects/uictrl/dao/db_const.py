#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@version: python3.7
@author: wjk
@software: PyCharm
@file: db_const.py
@time: 2020/10/26 21:32
@description: None
"""


class DBConst(object):
    db_url = "mysql+pymysql://root:wjk123@localhost:3306/django_database?charset=utf8"


class TablesName(object):
    MyApp_Students = 'myapp_students'
    MyApp_Teachers = 'myapp_teachers'
    MyApp_Grades = 'myapp_grades'
