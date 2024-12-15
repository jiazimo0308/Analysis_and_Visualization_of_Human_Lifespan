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
#二、发达国家和发展中国家的预期寿命是否有区别？
#发达国家和发展中国家平均预期寿命折线图
data1=data.iloc[:,[1,2,3]]
data2=data1.groupby(['Year','Status']).mean()
data2=data2.reset_index()
#索引取值
index=np.arange(len(data2))
D_ed=index[index%2==0]
D_ing=index[index%2!=0]
D_data_ed=data2.iloc[D_ed,:]
D_data_ing=data2.iloc[D_ing,:]
#设置函数(折线图）
def huitu(x,y):
    x1=x['Year']
    x2=x['Life expectancy ']
    x3=y['Life expectancy ']
    plt.title('各年预期寿命')
    plt.plot(x1,x2,marker='o',color='b')
    plt.plot(x1,x3,marker='o',color='r')
    plt.legend(["Developed", "Developing"])
    plt.xlabel("年份")
    plt.ylabel("平均预期寿命")
    plt.show()
huitu(D_data_ed,D_data_ing)

#三、预期寿命较低的发展中国家是否应该增加医疗支出以提高其平均寿命？
#选出发展中国家
Developing=data.loc[data["Status"]=='Developing',:]
#piersen相关系数看关系
def heatmap(x):
    corr1 = x.corr()
    fig = plt.figure(figsize=(20, 15))
    mask = np.zeros_like(corr1, dtype=np.bool)
    sns.heatmap(corr1, mask=mask, cmap="RdBu_r", center=0, linewidths=.5)
    plt.show()
#通过相关系数可以看出增加医疗支出对提高寿命有影响
#heatmap(data)

#挑选出主要数据
Developing_data=Developing.iloc[:,[1,3,19,20]]
data3=Developing_data.groupby('Year').mean()
data3=data3.reset_index().drop(['Year'],axis=1)
def sanzheguanxi(x):
    plt.figure(figsize=(12,5))
    plt.subplot(1, 2, 1)
    x.sort_values('Total expenditure',inplace=True)
    x1=x['Total expenditure']
    y1=x['Life expectancy ']
    plt.plot(x1, y1, marker='o',color='b')
    plt.xlabel('政府一般卫生支出占政府总支出的百分比(%)')
    plt.ylabel('预期寿命年龄')
    plt.title('政府一般卫生支出占政府总支出的百分比与预期寿命年龄')
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    plt.subplot(1,2,2)
    x.sort_values('percentage expenditure',inplace=True)
    x2=x['percentage expenditure']
    y2=x['Life expectancy ']
    plt.plot(x2,y2,marker='o',color='r')
    plt.xlabel('卫生支出占人均国内生产总值的百分比(%)')
    plt.ylabel('预期寿命年龄')
    plt.title('卫生支出占人均国内生产总值的百分比与预期寿命年龄')
    plt.show()
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    x3 = x['Total expenditure']
    y3= x['percentage expenditure']
    plt.scatter(x3, y3, color='r')
    plt.xlabel('政府一般卫生支出占政府总支出的百分比(%)')
    plt.ylabel('卫生支出占人均国内生产总值的百分比(%)')
    plt.title('政府一般卫生支出占政府总支出的百分比与卫生支出占人均国内生产总值的百分比')
    plt.show()

#sanzheguanxi(data3)

#四、婴儿和成人死亡率如何影响预期寿命？
#选择数据
baby_adult=data.iloc[:,[1,3,4,5]]
data4=baby_adult.groupby('Year').mean()
data4=data4.reset_index()
def baby_adult(x):
    year=x['Year']
    L_e=x['Life expectancy ']
    A_M=x['Adult Mortality']
    I_D=x['infant deaths']
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    plt.plot(year,L_e,color='r')
    plt.xlabel('年份')
    plt.ylabel('预期寿命年龄')
    plt.title('年份与预期寿命年龄变化趋势')
    plt.show()
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(A_M,L_e,color='b')
    plt.xlabel('每1000人的男女成人死亡数')
    plt.ylabel('预期寿命年龄')
    plt.title('每1000人的男女成人死亡数与预期寿命年龄变化趋势')
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    plt.subplot(1, 2, 2)
    plt.scatter(I_D, L_e,color='b')
    plt.xlabel('每1000人的婴儿死亡人数')
    plt.ylabel('预期寿命年龄')
    plt.title('每100人的婴儿死亡人数与预期寿命年龄变化趋势')
    plt.show()
baby_adult(data4)





