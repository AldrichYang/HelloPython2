# -*- coding: utf-8 -*-
import MySQLdb
from DBUtils.PooledDB import PooledDB

# 连接数据库
invt_pool = PooledDB(MySQLdb, 4, host='', db='', user='',
                     passwd='', port=3306, charset='utf8', blocking=True)
                     
def conn_db():
    db = invt_pool.connection()
    return db                   
                                          
# 查询操作

def query(sql, param_tuple):
    conn = conn_db()
    dbc = conn.cursor()
    dbc.execute(sql, param_tuple)
    rs = dbc.fetchall()
    dbc.close()
    conn.close()
    return rs

def queryOne(sql,param_tuple):
    rs = query(sql,param_tuple)
    if rs[0]:
        return rs[0]
