import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
from pyecharts.charts import  Map
from  pyecharts import options as opts


data1=pd.read_csv('../数据/Life Expectancy Data.csv')
data2=pd.read_csv('../数据/Countries of the wor.csv')

#data1
#print(data1.info())
#存在缺失值（使用众数填充）
for col in data1.columns:
    if ((data1[col].isnull()).sum())!=0:
        ll=data1[col].mode()[0]
        data1[col]=data1[col].fillna(value=ll)
    else:
        pass
#国家名称替换
#data1.to_csv('处理_1.csv')
data1['Country'].replace(
    ['United States of America','Bolivia (Plurinational State of)','Venezuela (Bolivarian Republic of)',
     'Bosnia and Herzegovina','Brunei Darussalam','Central African Republic','Czechia','Equatorial Guinea',
     'Iran (Islamic Republic of)',"Lao People's Democratic Republic",'Russian Federation','United Kingdom of Great Britain and Northern Ireland',
     'Republic of Korea','Dominican Republic','South Sudan','United Republic of Tanzania','Czechia',
     'Democratic Republic of the Congo','Central African Republic','Viet Nam',"Democratic People's Republic of Korea",
     'Syrian Arab Republic','The former Yugoslav republic of Macedonia','Bosnia and Herzegovina','Republic of Moldova','Denmark'],
    ['United States','Bolivia','Venezuela','Bosnia and Herz','Brunei','Central African Rep','Czech Rep',
     'Eq. Guinea','Iran','Lao PDR','Russia','United Kingdom','Korea','Dominican Rep.','S. Sudan','Tanzania',
     'Czech Rep.','Dem. Rep. Congo','Central African Rep.','Vietnam',"Dem. Rep. Korea",'Syria','Macedonia',
     'Bosnia and Herz.','Moldova','Greenland'],inplace=True)

#一、全球预期寿命分布如何
#切分数据
Country=data1.iloc[:,[0,3]]
Country_life=Country.groupby(['Country']).mean()
Country_life=Country_life.reset_index()

#MAP函数作图
map = Map( init_opts=opts.InitOpts(width="1900px", height="900px", bg_color="#ADD8E6",
	page_title="全球预期寿命分布图",theme="white"))
map.add("预期平均寿命",[list(z) for z in zip(Country_life['Country'], Country_life['Life expectancy '])],is_map_symbol_show=False,
    maptype="world",label_opts=opts.LabelOpts(is_show=False),
    itemstyle_opts=opts.ItemStyleOpts(color="rgb(49,60,72)"))
map.set_global_opts(title_opts = opts.TitleOpts(title='全球预期寿命分布图'),legend_opts=opts.LegendOpts(is_show=False),visualmap_opts = opts.VisualMapOpts(max_=90,min_=40))
map.render('全球寿命图.html')



