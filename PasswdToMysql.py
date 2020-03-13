#!/bin/env python3
import pymysql
#在库中建表哦～!
#create table user( id int auto_increment primary key, name varchar(20), passwd char(1), uid varchar(10), gid varchar(10), text varchar(100), home varchar(100), shell varchar(100));

#
data=[]
data1=[]
with open("/etc/passwd","r") as f1:
    data = f1.readlines()

for i in data:
    j=i.split(":")
    data1.append(j)
#注意自己的IP，用户名，密码，数据库
conn = pymysql.connect('127.0.0.1','root','123','testdb')
cur = conn.cursor() 
sqli = "insert into user(name, passwd, uid, gid, text, home, shell ) values(%s, %s, %s, %s, %s, %s, %s)"
cur.executemany(sqli,data1)
conn.commit()
cur.close()
conn.close()
