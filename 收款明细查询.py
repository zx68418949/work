# -*- coding: utf-8 -*-
"""
Created on Tue Mar 5 20:51:45 2019

@author: zx684
"""
import pandas as pd

# 定义通过sql和账套的查询函数

def SQL(sql,zt):
    import pyodbc
    import pandas as pd
    conn = pyodbc.connect(r'DRIVER=SQL SERVER;SERVER=183.64.79.10;UID=bb;PWD=cqhg65730332')
    cursor = conn.cursor()
    cursor.execute(zt)
    sql_df= pd.read_sql(sql,con=conn)
    conn.close()
    return sql_df


# sql查询语句

sql1='''SELECT RTRIM(t1.NAME) as 客户名称,
       RTRIM(t2.dptname) as 部门,
       RTRIM(t3.NAME) as 业务员,
       RTRIM(t4.payname) as 结算方式,
       RTRIM(t.curr) as 金额,
       RTRIM(t.remark) as 摘要,
       RTRIM(t.operant) as 制单人,
       RTRIM(t.date0) as 制单日期,
       CASE
         WHEN t.fs = '0'
                 THEN '客户应收费用'
         WHEN t.fs = '1'
                 THEN '客户应付费用'
         WHEN t.fs = '2'
                 THEN '客户已收费用'
         WHEN t.fs = '3'
                 THEN '客户已付费用'
         WHEN t.fs = '5'
                 THEN '供商应收费用'
         WHEN t.fs = '6'
                 THEN '供商应付费用'
         WHEN t.fs = '7'
                 THEN '供商已收费用'
         WHEN t.fs = '8'
                 THEN '供商已付费用'
         ELSE ''
           END '业务类型'
FROM OTHERCHARGE t
       LEFT JOIN CUSTOMER t1 ON t1.code = t.code
       LEFT JOIN DEPARTMENT t2 ON t2.dptno = t.dptno
       LEFT JOIN EMPLOYE t3 ON t3.code = t.handman
       LEFT JOIN PAYWAY t4 ON t4.payno = t.payno
WHERE t.date0 >= '2019-01-01'
ORDER BY t.date0 DESC'''
zt = ["use saledata001","use saledata004","use saledata006","use saledata010","use saledata011","use saledata014","use saledata015","use saledata020","use saledata021","use saledata022","use saledata023","use saledata024"]
gs = ["集团","成都兴恒","贵州瑞豪","昆明云沃","成都惠友","西昌惠友","乐山惠友","贵州后市场","重庆后市场","昆明租赁","重庆租赁","成都租赁"]
x = []
y = []
for i in range(len(zt)):
    a = SQL(sql1,zt[i])
    a['公司']=gs[i]#增加一列公司
    x.append(a)#通过列表循环依次从各个账套导入数据
df1 = pd.concat(x)#合并成一张表格

sql2 = '''SELECT RTRIM(t1.name) as 客户名称,
       RTRIM(t2.dptname) as 部门,
       RTRIM(t3.name) as 业务员,
       RTRIM(t4.payname) as 结算方式,
       RTRIM(t.curr) as 金额,
       RTRIM(t.remark) as 摘要,
       RTRIM(t.operant) as 制单人,
       RTRIM(t.date0) as 制单日期,
       case
         when t.lx = '0' then '配件收款'
         when t.lx = '1' then '配件退款'
         when t.lx = '2' then '整机收款'
         when t.lx = '3' then '整机退款'
         when t.lx = '4' then '维修收款'
         when t.lx = '5' then '三包'
         when t.lx = '6' then '租金收款'
         when t.lx = '7' then '设备销售收款'
         when t.lx = '8' then '设备销售退款'
         else '' end '业务类型'
from INCOMECURR t
       left join CUSTOMER t1 on t1.code = t.custno
       left join DEPARTMENT t2 on t2.dptno = t.dptno
       left join EMPLOYE t3 on t3.code = t.saleman
       left join PAYWAY t4 on t4.payno = t.payno
where t.lx in ('2', '3')
  and t.date0 >= '2016-01-01'
order by notedate desc'''
for i in range(len(zt)):
    b = SQL(sql2,zt[i])
    b['公司']=gs[i]#增加一列公司
    y.append(b)#通过列表循环依次从各个账套导入数据
df2 = pd.concat(y)
df3 = [df1,df2]
df =pd.concat(df3)
df.to_excel('收款明细.xlsx', sheet_name='收款明细')