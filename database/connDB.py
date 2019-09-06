# -*- coding: UTF-8 -*

import pymysql

import config.readConfig as readConfig
#from common.Log import Log


localReadConfig = readConfig.ReadConfig()
global user_id

def conn(database):
    #global host, port, username,password,database
    host = localReadConfig.get_db("host")
    port = localReadConfig.get_db("port")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    database = localReadConfig.get_db(database)

    try:
        mydb = pymysql.connect(host=host,user=username,passwd=password,db=database,charset='utf8')
        return mydb
    except:
        print ("db connect failed")

def conn_diversion():
    host = localReadConfig.get_db("host")
    port = localReadConfig.get_db("port")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    database_diversion = localReadConfig.get_db("database_diversion")

    try:
        mydb = pymysql.connect(host=host, user=username, passwd=password, db=database_diversion, charset='utf8')
        return mydb
    except:
        print("db connect failed")


# 执行查询sql并返回结果
def queryData(querysql,database):
    db = conn(database)
    cursor = db.cursor()
    results = []
    try:
        cursor.execute(querysql)
        rows = cursor.fetchall()
        for result in rows:
            results.append(result)
        #print(results)
        return results
    except:
        return False
    db.close()
    print('关闭查询数据库')



def queryOneData(querySql,database='database_engine'):
    db = conn(database)
    cursor = db.cursor()
    try:
        cursor.execute(querySql)
        rows = cursor.fetchone()
        #print(rows)
        return rows
    except:
        return False

    db.close()
    print('关闭查询数据库')

# 插入或更新数据

def InsertData(insertSql,database):
    db = conn(database)
    cursor = db.cursor()
    user_id = localReadConfig.get_user("user_id")
    try:
        cursor.execute(insertSql,[user_id])
        print(insertSql)
        db.commit()

    except Exception as e:
        db.rollback()
        print(e)
        return False

    db.close()
    #print('关闭更新数据库')
"""
def get_in_sql(dictd, table_name):
    '''
                生成insert的sql语句
    @table，插入记录的表名
    @dict,插入的数据，字典
    '''
    sql3 = 'insert into ' + table_name + ' set'
    sql3 += dict_2_str(dictd)
    return sql3
"""

mobile = localReadConfig.get_user("mobile")[0:3] + "******" + localReadConfig.get_user("mobile")[9:11]
sql1 = "select user_id from user_extension where mobileNumber = '%s'" % mobile
user_id = queryOneData(sql1, "database_diversion")[0]


table = "wise_user_exp"
database = "database_customer"
sql2 = "select count(1) from %s where user_id = '%s'" % (table,user_id)
print(sql2)

c = queryOneData(sql2, database)[0]
print(type(c))
if c > 0:
    print("已完成基本资料")
else:
    print("未完成基本资料")