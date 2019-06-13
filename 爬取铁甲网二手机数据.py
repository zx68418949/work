# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys
import re
import multiprocessing
from multiprocessing import Pool
from requests.packages import urllib3
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
requests.packages.urllib3.disable_warnings()
import pandas as pd
import threading
import time

MAX_WORKER_NUM = multiprocessing.cpu_count()

t1 = time.time()

##查询一页的所有网址，p表示某一页
def url(p):
    sever = 'https://www.tiebaobei.com/ue/'
    target = sever + str(p)+'/'
    req = requests.get(url=target, verify=False)
    html = req.text
    div_bf = BeautifulSoup(html, "lxml")
    div = div_bf.find_all('ul', class_='proList clearfix')
    a_bf = BeautifulSoup(str(div[0]), "lxml")
    a = a_bf.find_all('a')
    x = []
    for i in range(0, len(a), 2):
        b = str(a[i]).split()[2][6:-1]
        x.append(b)
    return x

##多页网址合并，o表示页数
def urls(o):
    d=[]
    for p in range(1,o):
        try:
            r=url(p)
            d.extend(r)
            print("正在爬取第{a}页,共计{b}页,已经执行{x:.2%}".format(a=p,b=o,x=p/(o+1)))
        except:
            continue
    return(d)

v=urls(1778)##设置读取的网页
print("耗时：", time.time()-t1)


def data(x):
    target = x
    req = requests.get(url=target,verify=False)
    html = req.text
    bf = BeautifulSoup(html, "lxml")
    equipmentBrand = bf.find('input', id="equipmentBrand").get('value')  # 品牌
    equipmentCategory = bf.find('input', id="equipmentCategory").get('value')  # 机型
    equipmentModel = bf.find('input', id="equipmentModel").get('value')  # 型号
    equipmentTonnage = bf.find('input', id="equipmentTonnage").get('value')  # 吨位
    equipmentOutDate = bf.find('input', id="equipmentOutDate").get('value')  # 出厂年份
    equipmentHours = bf.find('input', id="equipmentHours").get('value')  # 工作小时数
    managerProvince = bf.find('input', id="managerProvince").get('value')  # 省
    managerCity = bf.find('input', id="managerCity").get('value')  # 市
    equipmentPrice = bf.find('input', id="equipmentPrice").get('value')  # 价格
    # 将计算结果逐行插入result,注意变量要用[]括起来,同时ignore_index=True，否则会报错，ValueError: If using all scalar values, you must pass an index
    data=pd.DataFrame(columns=['品牌', '机型', '型号', '吨位','出厂年份','工作小时数','省','市','价格'])
    data=data.append(pd.DataFrame({'品牌':[equipmentBrand], '机型':[equipmentCategory], '型号':[equipmentModel], '吨位':[equipmentTonnage],'出厂年份':[equipmentOutDate],'工作小时数':[equipmentHours],'省':[managerProvince],'市':[managerCity],'价格':[equipmentPrice]}),ignore_index=True)
    return data

##多个页面的数据，y表示页数
def df(y):
    df=[]
    for i in range(len(y)):
        try:
            datas=data((y)[i])
            df.append(datas)
            print("正在爬取第{a}条,共计{b}条,已经执行{x:.2%}".format(a=i, b=len(y), x=i/len(y)))
        except:
            continue
    df=pd.concat(df).reset_index(drop=True)
    return df

dp=df(v)
df.to_excel('铁甲网二手机xlsx', sheet_name='铁甲网二手机')
