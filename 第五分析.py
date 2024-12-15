import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
from pyecharts.charts import  Map
from pyecharts.charts import Timeline
from  pyecharts import options as opts
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

data=pd.read_csv('../处理_1.csv')
data=data.drop(['Unnamed: 0'],axis=1)
#地点替换
data['Country'].replace(
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
#五、不同地区的免疫覆盖范围是否有区别？
mianyi=data.iloc[:,[0,9,10,11]]
C_mianyi=mianyi.groupby("Country").mean()
C_mianyi=C_mianyi.reset_index()

Country=C_mianyi['Country']
year=['Hepatitis B','Polio','Diphtheria']
time_axis=Timeline()
for i in range(3,0,-1):
    pop_time=Map(init_opts=opts.InitOpts(width="1900px", height="900px", bg_color="#ADD8E6",
	page_title="全球免疫分布图",theme="white"))
    pop_time.add('world',[list(z) for z in zip(Country,C_mianyi.iloc[:,i].tolist())],is_map_symbol_show=False,
    maptype="world",label_opts=opts.LabelOpts(is_show=False), itemstyle_opts=opts.ItemStyleOpts(color="rgb(49,60,72)"))
    pop_time.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0,max_=100,), title_opts=opts.TitleOpts(title='免疫覆盖范围地图'),)
    time_axis.add_schema(is_auto_play=True)
    time_axis.add(chart=pop_time,time_point='{}'.format(year[i-1]))
time_axis.render("全球免疫图.html")
