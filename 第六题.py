import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
from pyecharts.charts import  Map
from  pyecharts import options as opts
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

data=pd.read_csv('../处理_1.csv')
data=data.drop(['Unnamed: 0'],axis=1)
#六.学校教育对其他因素有什么影响？
#取每个国家的平均值作为代表
data2=data.groupby('Country').mean()
data2=data2.drop(['Year'],axis=1)
data3=data2.drop(['Schooling'],axis=1)
plt.figure(figsize=(30,12))
plt.tight_layout()
for i,col in enumerate(data3.columns):
    ax=plt.subplot(3,6,i +1)
    ax=plt.scatter(data2['Schooling'],data3[col],color='r')
    plt.xlabel('受教育年限')
    plt.ylabel(col)
plt.show()

