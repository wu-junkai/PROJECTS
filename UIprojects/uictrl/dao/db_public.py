#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@version: python3.7
@author: wjk
@software: PyCharm
@file: db_public.py
@time: 2020/10/27 21:13
@description: None
"""
from datetime import datetime


def deal_with_data(value):
    if value is '' or str(value).lower() == 'null':
        value = None
    if isinstance(value, datetime):
        value = value.strftime("%Y-%m-%d %H:%M:%S")
    return value


def pubic_parse_result(data_list):
    return_data = []
    for every_data in data_list:
        key_list = list(every_data.keys())
        value_list = list(every_data.values())
        temp = dict(list(zip(key_list, value_list)))
        for key in temp.keys():
            temp[key] = deal_with_data(temp[key])
        return_data.append(temp)
    return return_data


def structure_query_sql(table, param=None):
    adds = ""
    if param is None:
        sql = f'select * from {table}'
    else:
        keys = list(param.keys())
        for index, k in enumerate(keys):
            if isinstance(param[k], str):
                adds = adds + " %s = '%s' " % (k, param[k])
            else:
                adds = adds + " %s = %s " % (k, param[k])
            if index < len(keys) - 1:
                adds = adds + 'and'
        sql = f'select * from {table} where {adds}'
    return sql


def structure_update_sql(table, set_param, select_param):
    set_add = ""
    set_keys = list(set_param.keys())
    for index, k in enumerate(set_keys):
        if isinstance(set_param[k], str):
            set_add = set_add + " %s = '%s' " % (k, set_param[k])
        else:
            set_add = set_add + " %s = %s " % (k, set_param[k])
        if index < len(set_keys) - 1:
            set_add = set_add + ','

    select_add = ""
    select_keys = list(select_param.keys())
    for index, k in enumerate(select_keys):
        if isinstance(select_param[k], str):
            select_add = select_add + " %s = '%s' " % (k, select_param[k])
        else:
            select_add = select_add + " %s = %s " % (k, select_param[k])
        if index < len(select_keys) - 1:
            select_add = select_add + 'and'
    sql = f'update {table} set {set_add} where {select_add}'
    return sql


def structure_delete_sql(table, select_param):
    delete_adds = ""
    keys = list(select_param.keys())
    for index, k in enumerate(keys):
        if isinstance(select_param[k], str):
            delete_adds = delete_adds + " %s = '%s' " % (k, select_param[k])
        else:
            delete_adds = delete_adds + " %s = %s " % (k, select_param[k])
        if index < len(keys) - 1:
            delete_adds = delete_adds + 'and'
    sql = f'delete from {table} where {delete_adds}'
    return sql


if __name__ == "__main__":
    print(structure_delete_sql(table='myapp_students', select_param={'id': 5}))
