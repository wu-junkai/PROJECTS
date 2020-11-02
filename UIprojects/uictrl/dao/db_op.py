#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@version: python3.7
@author: wjk
@software: PyCharm
@file: db_op.py
@time: 2020/10/26 20:34
@description: 数据库操作
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from uictrl.dao.db_const import DBConst, TablesName
from uictrl.dao.db_public import pubic_parse_result, structure_query_sql, structure_update_sql, structure_delete_sql


class DBUtil(object):
    __base_class = None

    def __init__(self, url, encoding='utf-8', echo=False):
        self._engine = create_engine(url, encoding=encoding, echo=echo)
        session_class = sessionmaker(bind=self._engine)
        self._session = session_class()

    def _table_query(self, table_name):
        if self.__base_class is None:
            self.__base_class = automap_base()
            self.__base_class.prepare(self._engine, reflect=True)
        if hasattr(self.__base_class.classes, table_name):
            table = getattr(self.__base_class.classes, table_name)
            print(table)
            return self._session.query(table)
        else:
            raise KeyError(f"未搜寻到表: {table_name}")

    def all(self, table_name, ft=None):
        """ 所有数据 """
        ft = {} if ft is None else ft
        all_row = self._table_query(table_name).filter_by(**ft).all()
        return all_row

    def db_query_all(self, table_name, param=None):
        try:
            full_sql = structure_query_sql(table_name, param)
            sql = text(full_sql)
            res = self._session.execute(sql)
            data_list = res.fetchall()
            result = pubic_parse_result(data_list)
        finally:
            self._session.close()
        return result

    def db_update_all(self, table_name, set_param, select_param):
        try:
            full_sql = structure_update_sql(table_name, set_param, select_param)
            sql = text(full_sql)
            self._session.execute(sql)
            self._session.commit()
        finally:
            self._session.close()

    def db_delete_all(self, table_name, select_param):
        try:
            full_sql = structure_delete_sql(table_name, select_param)
            sql = text(full_sql)
            self._session.execute(sql)
            self._session.commit()
        finally:
            self._session.close()


if __name__ == '__main__':
    # DBUtil(url=DBConst.db_url).all(TablesName.MyApp_Students, ft=dict(id='5'))
    DBUtil(url=DBConst.db_url).db_delete_all(TablesName.MyApp_Students, select_param={'id': 5})


