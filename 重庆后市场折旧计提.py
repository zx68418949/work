# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:17:35 2017

@author: zx
"""
import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir("E:\\OneDrive\\跌价")#设定工作目录
os.getcwd()
excel_path = 'E:\\OneDrive\\跌价\\重庆.xlsx'#设定读取excel路径
a = pd.read_excel(excel_path, sheetname=0)
a = pd.DataFrame(a)
def SQL(sql,zt):
    import pyodbc
    import pandas as pd
    conn = pyodbc.connect(r'DRIVER=SQL SERVER;SERVER=183.64.79.10;UID=bb;PWD=cqhg65730332')
    cursor = conn.cursor()
    cursor.execute(zt)
    sql_df= pd.read_sql(sql,con=conn)
    conn.close()
    return sql_df
sql='''DECLARE @sdate DATETIME;
DECLARE @edate DATETIME;
DECLARE @qtck VARCHAR(10);
DECLARE @sbck VARCHAR(10);
DECLARE @xxck VARCHAR(10);
DECLARE @wzck VARCHAR(10);
DECLARE @cgth VARCHAR(10);
SET @sdate = '2015-11-25';
SET @edate = '2018-05-25';
SET @qtck = '其他出库';
SET @sbck = '三包出库';
SET @xxck = '销售出库';
SET @wzck = '物资出库';
SET @cgth = '采购退货';
SELECT  RTRIM(OTHEROUTM.wareno) AS 件号 ,
OTHEROUTM.amount AS 数量 ,
OTHEROUTM.price AS 单价 ,
OTHEROUTM.curr AS 合计金额 ,
RTRIM(OTHEROUTM.idstr) AS 关联标志 ,
OTHEROUTH.notedate AS 日期 ,
@qtck AS 出库类型 ,
RTRIM(PROVIDE.name) AS 供应商
FROM    OTHEROUTM
INNER JOIN OTHEROUTH ON OTHEROUTH.noteno = OTHEROUTM.noteno
INNER JOIN WAREIDSTR ON WAREIDSTR.idstr = OTHEROUTM.idstr
INNER JOIN dbo.PROVIDE ON PROVIDE.code = dbo.WAREIDSTR.provno
WHERE  OTHEROUTH.notedate BETWEEN @sdate AND @edate
UNION ALL
SELECT  RTRIM(SBSPM.wareno) AS 件号 ,
SBSPM.amount AS 数量 ,
SBSPM.price AS 单价 ,
SBSPM.curr AS 合计金额 ,
RTRIM(SBSPM.idstr) AS 关联标志 ,
SBSPH.notedate AS 日期 ,
@sbck AS 出库类型 ,
RTRIM(PROVIDE.name) AS 供应商
FROM    SBSPM
INNER JOIN SBSPH ON SBSPH.noteno = SBSPM.noteno
INNER JOIN WAREIDSTR ON WAREIDSTR.idstr = SBSPM.idstr
INNER JOIN dbo.PROVIDE ON PROVIDE.code = dbo.WAREIDSTR.provno
WHERE  SBSPH.notedate BETWEEN @sdate AND @edate
UNION ALL
SELECT  RTRIM(WAREOUTM.wareno) AS 件号 ,
WAREOUTM.amount AS 数量 ,
WAREOUTM.price AS 单价 ,
WAREOUTM.curr AS 合计金额 ,
RTRIM(WAREOUTM.idstr) AS 关联标志 ,
WAREOUTH.notedate AS 日期 ,
@xxck AS 出库类型 ,
RTRIM(PROVIDE.name) AS 供应商
FROM    WAREOUTM
INNER JOIN WAREOUTH ON WAREOUTH.noteno = WAREOUTM.noteno
INNER JOIN WAREIDSTR ON WAREIDSTR.idstr = WAREOUTM.idstr
INNER JOIN dbo.PROVIDE ON PROVIDE.code = dbo.WAREIDSTR.provno
WHERE  WAREOUTH.notedate BETWEEN @sdate AND @edate
UNION ALL
SELECT  RTRIM(REPAIROUTM.wareno) AS 件号 ,
REPAIROUTM.amount AS 数量 ,
REPAIROUTM.price AS 单价 ,
REPAIROUTM.curr AS 合计金额 ,
RTRIM(REPAIROUTM.idstr) AS 关联标志 ,
REPAIROUTH.notedate AS 日期 ,
@wzck AS 出库类型 ,
RTRIM(PROVIDE.name) AS 供应商
FROM    REPAIROUTM
INNER JOIN REPAIROUTH ON REPAIROUTH.noteno = REPAIROUTM.noteno
INNER JOIN WAREIDSTR ON WAREIDSTR.idstr = REPAIROUTM.idstr
INNER JOIN dbo.PROVIDE ON PROVIDE.code = dbo.WAREIDSTR.provno
WHERE  REPAIROUTH.notedate BETWEEN @sdate AND @edate
UNION ALL
SELECT  RTRIM(REFUNDINM.wareno) AS 件号 ,
REFUNDINM.amount AS 数量 ,
REFUNDINM.price AS 单价 ,
REFUNDINM.curr AS 合计金额 ,
RTRIM(REFUNDINM.idstr) AS 关联标志 ,
REFUNDINH.notedate AS 日期 ,
@cgth AS 出库类型 ,
RTRIM(PROVIDE.name) AS 供应商
FROM    REFUNDINM
INNER JOIN REFUNDINH ON REFUNDINH.noteno = REFUNDINM.noteno
INNER JOIN WAREIDSTR ON WAREIDSTR.idstr = REFUNDINM.idstr
INNER JOIN dbo.PROVIDE ON PROVIDE.code = dbo.WAREIDSTR.provno
WHERE  REFUNDINH.notedate BETWEEN @sdate AND @edate;'''
restult= pd.DataFrame(SQL(sql,"use saledata021"))
b= pd.DataFrame(restult.groupby(['件号'])['数量'].sum())#分类求和
b= b.reset_index()#重建索引
for i in range(len(a)):
  try:
    list(b["件号"]).index(a.loc[i,'件号'])
  except:#异常处理
    a.loc[i,"数量"]=a.loc[i,"数量"]
  else:
    r=list(b["件号"]).index(a.loc[i,'件号'])
    x=a.loc[i,"数量"]-b.loc[r,'数量']
    if x>=0:
        a.loc[i,"数量"]=x
        b.loc[r,"数量"]=0
    else:
        a.loc[i,"数量"]=0
        b.loc[r,"数量"]=abs(x)
sql2='''DECLARE @a VARCHAR(10);
SET @a='2018 5';
SELECT period AS 期间,
RTRIM(wareno) AS 件号,
amount AS 数量,
price  AS 单价,
curr  AS 合计金额,
RTRIM(idstr)  AS 关联标志,
RTRIM(WAREHOUSE.housename) AS 仓库名称,
RTRIM(DEPARTMENT.dptname) AS 部门名称,
CAST(SUBSTRING(idstr,PATINDEX('%[0-9]%',idstr),6)AS DATETIME) AS 入库时间
FROM WARESUM0
INNER JOIN WAREHOUSE ON WARESUM0.houseno=WAREHOUSE.houseno
INNER JOIN DEPARTMENT ON DEPARTMENT.dptno=WAREHOUSE.dptno
WHERE period=@a AND amount<>0'''
result2 = pd.DataFrame(SQL(sql2,"use saledata021"))#读取现在的库存
result2['公司'] = result2.部门名称.apply(lambda x: "丹太" if '综合配件组' in x else "后市场")
c = result2.loc[(result2['入库时间']>'2016-6-25')&(result2['部门名称']!="重庆服务部")&(result2['部门名称']!="寄售成都丹太组")&(result2['部门名称']!="寄售昆明丹太组")&(result2['部门名称']!="寄售贵州后市场组")&(result2['仓库名称']!="综合配件组2S"),['件号','数量','关联标志','入库时间','单价','合计金额','公司']]#筛选早于2016-1-1的库存
c = c.reset_index()
nf = ('2017-05-25','2016-05-25','2015-05-25','2014-5-25')
nf = pd.to_datetime(nf)#改为时间类型
def nx(number):#分条件赋值
    if number >= nf[0]:
        return '一年以内'
    elif number >= nf[1]:
        return '一年以上'
    elif number >= nf[2]:
        return '两年以上'
    elif number >= nf[3]:
        return '三年以上'
    elif number < nf[3]:
        return '四年以上'
c['年限']=c['入库时间'].map(nx)
a['入库时间']=a['入库时间'].astype('datetime64[ns]')#改变数据类型
a['年限']=a['入库时间'].map(nx)
df1 = c.loc[:,['件号','数量','单价','年限','公司']]#按照列进行选择
df2 = a.loc[:,['件号','数量','单价','年限','公司']]
df3= [df1,df2]
df = pd.concat(df3)#两个表格合并
df['合计金额']=df['数量']*df['单价'].astype('int')
y = df.groupby(['年限','公司'])['合计金额'].sum()
y = y.reset_index()
k = ('一年以内','一年以上','两年以上','三年以上','四年以上')
bl=(0,0.2,0.5,0.8,0.95)
z = pd.DataFrame({'年限':k,'计提比例':bl})
y=pd.merge(y,z,how='inner')
y['计提金额']=y['合计金额']*y['计提比例']
y['计提金额']=y['计提金额'].astype('int')
y
y['计提金额'].sum()