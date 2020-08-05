import hashlib,time,requests,os
import random,ssl,getopt
import threading,queue,datetime
import sys,re,sqlite3,lxml
from bs4 import BeautifulSoup as BS


def test_db():
    """
    测试数据库连接是否正常
    """
    pwd = os.getcwd()
    db_path = os.path.join(pwd,"cms_finger.db")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        result = cursor.execute('SELECT COUNT(id) FROM `fofa`')
        for row in result:
            assert row[0] == 2119

def test_parameterize_sql():
    """
    测试数据库参数化SQL支持情况
    """
    pwd = os.getcwd()
    db_path = os.path.join(pwd,"cms_finger.db")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        result = cursor.execute('SELECT name FROM `fofa` where id=(?)', (1,))
        for row in result:
            assert row[0] == "Huawei-Firewall"