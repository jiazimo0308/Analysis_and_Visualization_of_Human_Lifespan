# Analysis_and_Visualization_of_Human_Lifespan
人类寿命分析与可视化.  
Analysis and Visualization of Human Lifespan

## 1. 数据背景(Data background)
世界卫生组织(WHO)下属的全球卫生观察站(GHO)数据库跟踪了全球众多国家 的健康状况以及许多其他相关因素。现向公众开放一份关于预期寿命、健康因素、经济情况有关的数据集，数据集中综合了2000年至2015年193个国家的数据，由于一些不太知名的国家的数据查找较困难，如瓦努阿图、汤加、多哥、佛得角等，因此该数据集中已排除这些国家，最终由22列、2938行组成.
(The Global Health Observatory (GHO) database under the World Health Organization (WHO) tracks the health status of many countries around the world and many other related factors. A data set related to life expectancy, health factors and economic conditions is now open to the public. The data set integrates data from 193 countries from 2000 to 2015, because it is difficult to find data from some lesser-known countries, such as Vanuatu, Tonga, Togo, Dejiao, etc., so these countries have been excluded from the data set, and eventually consist of 22 columns and 2938 rows.)

<div align=center>
  
|编号|特征|含义|
|:----:|:----:|:----:|
|1|Country|国家|
|2|Year|年份|
|3|Status|Developed or Developing status(发达/发展中)|
|4|Life expectancy|预期寿命年龄|
|5|Adult Mortality|每1000人的男女成人死亡数(15至60岁)|
|6|infant deaths|每1000人的婴儿死亡人数|
|7|under-five deaths|每1000人五岁以下死亡人数|
|8|HIV/AIDS|每1000个活产儿中在0-4岁死于艾滋病毒/艾滋病人数|
|9|Measles|每1000人报告的麻疹病例数|
|10|Hepatitis B|1岁儿童乙型肝炎免疫接种率(%)|
|11|Polio|1岁儿童脊髓灰质炎(Pol3)免疫覆盖率(%)|
|12|Diphtheria|1岁儿童白喉、破伤风、百日咳免疫接种率(%)|
|13|thinness1-19years|10至19岁儿童和青少年中的瘦弱率(%)|
|14|thinness5-9years|5 至9岁儿童中的瘦弱率(%)|
|15|BMI|平均体重指数|
|16|Alcohol|人均酒精消费量 (15岁+，单位:升)|
|17|Schooling|受教育年限|
|18|Population|该国家人口|
|19|GDP|人均国内生产总值(单位:美元)|
|20|Total expenditure|政府一般卫生支出占政府总支出的百分比(%)|
|21|percentage expenditure|卫生支出占人均国内生产总值的百分比(%)|
|22|Income composition of resources|以资源收入构成为单位的人力发展指数(范围:0-1)|
</div>

另外，附加一份各个国家的信息表(2015年).(In addition, provide an information form of each country (2015).)

<div align=center>
  
|编号|特征|含义|
|:----:|:----:|:----:|
|1|Country|国家|
|2|Region|所属地区|
|3|Area|国家面积|
|4|Literacy|识字率(%)|
|5|Phones|每1000人使用手机的人数|
|6|Agriculture|农业占比|
|7|Industry|工业占比|
|8|Service|服务业占比|
</div>

## 2. 数据概况(Data overview)
利用python函数对Life Expectancy Data数据集进行初步的数据预览。并做出如下数据预览结果。(Use the python function to preview the data set of Life Expectancy Data. And make the following data preview results.)

<div align=center>
  
|Column|Dtype|Isnull|
|:----:|:----:|:----:|
|Country|object|N|
|Year|int64|N|
|Status|object|N|
|Life expectancy|float64|Y|
|Adult Mortality|float64|Y|
|infant deaths|int64|N|
|under-five deaths|int64|N|
|HIV/AIDS|float64|N|
|Measles|int64|N|
|Hepatitis B|float64|Y|
|Polio|float64|Y|
|Diphtheria|float64|Y|
|thinness 1-19years|float64|Y|
|thinness 5-9 years|float64|Y|
|BMI|float64|Y|
|Alcohol|float64|Y|
|Schooling|float64|Y|
|Population|float64|Y|
|GDP|float64|Y|
|Total expenditure|float64|Y|
|Percentage expenditure|float64|N|
|Income composition of resources|float64|Y|
</div>

其中数据的数值类型共有三种。Obiect类型的有两种，int类型有四种，其余为float64类型数据。共2938行数据，22列特征。(Among them, there are three types of numerical data. There are two types of Obiect type, four types of int type, and the rest are float64 type data. A total of 2938 rows of data and 22 columns of features.)

利用python函数对Life Expectancy Data数据集进行初步的数据预览。并做出如下数据预览结果。(Use the python function to preview the data set of Life Expectancy Data. And make the following data preview results.)

<div align=center>
  
|Column|Dtype|Isnull|
|:----:|:----:|:----:|
|Country|object|N|
|Region|object|N|
|Area|Int64|Y|
|Literacy|object|Y|
|Phones|object|Y|
|Agriculture|object|Y|
|Industry|object|Y|
|Service|object|Y|
</div>

其中数据的数值类型共有两种。Obiect类型的有七种，int类型有一种。共227行，8列特征。 (Among them, there are two numerical types of data. There are seven types of Obiect and one type of int. A total of 227 rows, 8 columns of features.)

## 3.数据预处理(Data preprocessing)
观察数据可以看出全球城市的情况，为了表现出城市正常的数据来填充缺失值。我选用众数填充为缺失值进行处理。使用众数体现一个所有国家相对正常下的数据状态。(Observing the data can see the situation of cities around the world. In order to show the normal data of the city, the missing values are filled in. I choose to fill in the number of missing values to process it. The use of crowd numbers reflects the relatively normal data status of all countries.)

## 4.数据分析与可视化(Data analysis and visualization)
### 4.1全球预期寿命分布如何(What is the distribution of global life expectancy?)
利用pyecharts进行全世界地图的绘制。绘制出全球各个地点这几年预期寿命的平均值。利用颜色来展现出每个国家平均预期年龄的差别。通过数据切分，切选出国家和预期寿命并通过mean()函数来求得平均寿命。之后通过Map()函数对各个国家进行可视化作图。看出全球预期寿命分布的具体情况。(Use pyecharts to draw maps around the world. Draw the average life expectancy of various locations around the world in recent years. Use color to show the difference in the average expected age of each country. Through data cutting, the country and life expectancy are selected and the average life expectancy is obtained through the mean() function. After that, visualize and map each country through the Map() function. See the specific distribution of global life expectancy.)  
通过pyecharts绘制出全球预期寿命分布情况。(Draw the distribution of global life expectancy through pyecharts.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/4f1469b9-85fc-4907-a85e-74acec601d76" />
</div>

由全球预期寿命分布图可以看到，预期寿命较高的国家分布。主要分布在北半球且发达国家，东半球的预期寿命要小于西半球的预期寿命。非洲的预期寿命整体最差。且北美洲，欧洲和大洋洲的预期寿命最高。(It can be seen from the global life expectancy distribution map that the distribution of countries with higher life expectancy. It is mainly distributed in the Northern Hemisphere and developed countries, and the life expectancy of the Eastern Hemisphere is shorter than that of the Western Hemisphere. Africa's overall life expectancy is the worst. And North America, Europe and Oceania have the highest life expectancy.)

### 4.2发达国家和发展中国家的预期寿命是否有区别？(Is there a difference in life expectancy between developed and developing countries?)
通过数据的切分，切分出发达国家与发展中国家的数据。得到的数据进行Year和Status的分组并求出平均值。这样我们就得到了两个发达国家和发展中国家在这几年中预期寿命的数据。之后制作折线图进行数据的可视化。(Through data fragmentation, the data of developed countries and developing countries can be separated. The obtained data is grouped into Year and Status and the average value is calculated. In this way, we have the data of the life expectancy of two developed countries and developing countries in recent years. Then make a line chart to visualize the data.)  
通过matplotlib绘制出发达国家与发展中国家在2000年到2015年平均寿命变化情况。(The changes in the average life expectancy of developed and developing countries from 2000 to 2015 are drawn through matplotlib.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/1e534bb7-3636-4c2a-88ee-c2d833155224" />
</div>

由发达国家与发展中国家每年预期寿命变化可以看出，发达国家的预期平均寿命要比发展中国家的预期寿命高。但不管是发达国家还是发展中国家每年预期寿命都在不断地上升。且发展中国家在这15年中增长的幅度要大于发达国家增长的幅度。(It can be seen from the annual changes in life expectancy between developed and developing countries that the average life expectancy in developed countries is higher than that in developing countries. But whether it is developed or developing, the life expectancy is constantly rising every year. Moreover, the growth rate of developing countries in the past 15 years is greater than that of developed countries.)

### 4.3预期寿命较低的发展中国家是否应该增加医疗支出以提高其平均寿命？(Should developing countries with low life expectancy increase their medical spending to improve their average life expectancy?)
切分出发展中国家的数据。之后为了看到全部国家中医疗支出是否对预期寿命是否有一定的影响。绘制出皮尔森相关系数探究三者的相关性。之后根据发展中国家的数据，绘制政府一般卫生支出占政府总支出的百分比、卫生支出占人均国内生产总值的百分比和预期寿命三者的散点图。(Cut out the data of developing countries. After that, in order to see whether the medical expenditure in all countries has a certain impact on life expectancy. Draw the Pierson correlation coefficient to explore the correlation between the three. Then, according to the data of developing countries, a scatter plot of the percentage of government general health expenditure to total government expenditure, the percentage of health expenditure per capita GDP and life expectancy are drawn.)  
绘制出全部数据的皮尔森相关热图。(Draw a Pierson-related heat map of all the data.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/c8aadee3-dd32-454d-8730-6392d6cf23c9" />
</div>

我们由相关热谱图可以看到，预期寿命与政府一般卫生支出占政府总支出的百分比、卫生支出占人均国内生产总值的百分比程正相关。且卫生支出占人均国内生产总值的百分比要大于政府一般卫生支出占政府总支出的百分比的相关性。可以说医疗支出与预期寿命存在一定关系。之后制作政府一般卫生支出占政府总支出的百分比与卫生支出占人均国内生产总值的百分比。探究两者之间的关系。(We can see from the relevant heat spectrum map that life expectancy is related to the percentage of government general health expenditure to total government expenditure and the percentage of health expenditure per capita GDP. And the percentage of health expenditure to GDP per capita is greater than the percentage of general government health expenditure to total government expenditure. It can be said that there is a certain relationship between medical expenditure and life expectancy. After that, make the percentage of the government's general health expenditure to the total government expenditure and the percentage of health expenditure to the per capita GDP. Explore the relationship between the two.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/f1cb6cd8-8349-48a2-9cf4-69c6f3264f3f" />
</div>

可以看到政府一般卫生支出占政府总支出的百分比与卫生支出占人均国内生产总值的百分比是成正向相关的关系。我们确定了政府一般卫生支出占政府总支出的百分比与卫生支出占人均国内生产总值的百分比的关系，之后绘制两种医疗占比对预期寿命的关系图。(It can be seen that the percentage of government general health expenditure to total government expenditure and the percentage of health expenditure per capita GDP are positively related. We determined the relationship between the percentage of government general health expenditure to total government expenditure and the percentage of health expenditure per capita GDP, and then drew a diagram of the relationship between the proportion of medical care to life expectancy.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/c5f9c1b5-de3b-4053-aee2-ebd1e8ad9299" />
</div>

我们通过医疗支出的情况可以看出，随着卫生支出占人均国内生产总值的百分和大于政府一般卫生支出占政府总支出的百分比的逐渐增大。其预期寿命在图示上是先减小在增大。由于第一个点导致图像展现出次情况。但多数点组成的大体趋势可以看出，随着卫生支出占人均国内生产总值的百分和大于政府一般卫生支出占政府总支出的百分比的逐渐增大其预期寿命是在不断地波折上升，但总趋势是在不断地增大。(We can see from the situation of medical expenditure that with the gradual increase of health expenditure as a percentage of per capita GDP and a percentage greater than the government's general health expenditure to the total government expenditure. Its life expectancy is reduced first and then increased in the diagram. Because of the first point, the image shows the secondary situation. However, the general trend of majority points can be seen that with the gradual increase of health expenditure as a percentage of GDP per capita and greater than the percentage of government general health expenditure to total government expenditure, its life expectancy is constantly rising, but the general trend is increasing.)

### 4.4婴儿和成人死亡率如何影响预期寿命？(How do infant and adult mortality rates affect life expectancy?)
先切取出需要的数据，根据年份对数据进行分组并求出那一年每1000人的男女成人死亡数和每1000人的婴儿死亡人数的平均值作为主要数据。绘制出所有国家每年平均的预期寿命的变化趋势，之后在根据每1000人的男女成人死亡数和每1000人的婴儿死亡人数与预期寿命的关系。(First, cut out the required data, group the data according to the year, and find the average number of male and female adult deaths per 1,000 people and the number of infant deaths per 1,000 people in that year as the main data. Draw the trend of the average annual life expectancy in all countries, and then according to the relationship between the number of male and female adult deaths per 1,000 and the number of infant deaths per 1,000 people and life expectancy.)  
做出做出年份与预期寿命之间的全球变化趋势。(Make a global trend of change between the year and the life expectancy.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/674f926b-180e-4653-b999-4b3a37ad6aea" />
</div>

由年份与预期寿命变化趋势可以看到，全球预期寿命在逐年升高。且增长幅度较大。之后我们针对于婴儿和成人死亡率分别做出与预期寿命年龄的散点图，由图可以看出，成人死亡率在逐渐赠多的同时预期寿命在下降，由散点图可以看出数据分布较为松散但总体趋势是反向关系，数据分散可能由于其他的因素所导致，而婴儿死亡率则与预期寿命有较为集中的反向关系。数据趋势较为明显。可见婴儿死亡率对预期寿命有明显的影响作用。(It can be seen from the trend of year and life expectancy that global life expectancy is increasing year by year. And the growth rate is large. After that, we made a scatter diagram of the expected life expectancy for infant and adult mortality rates respectively. It can be seen from the figure that the adult mortality rate is gradually increasing while the life expectancy is decreasing. From the scatter chart, it can be seen that the data distribution is relatively loose, but the overall trend is the opposite relationship. The dispersion of data may be due to other factors. As a result, the infant mortality rate has a relatively concentrated inverse relationship with life expectancy. The data trend is more obvious. It can be seen that the infant mortality rate has a significant impact on life expectancy.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/73537372-45cc-49ca-9d40-00ba97b72d89" />
</div>

### 4.5不同地区的免疫覆盖范围是否有区别？(Is there a difference in immunization coverage in different regions?)
不同地区的免疫覆盖范围是否有区别。通过查看原始数据我们可以看到三个疫苗节奏信息。分别是1岁儿童乙型肝炎免疫接种率，1 岁儿童脊髓灰质炎(Pol3)免疫覆盖率和1岁儿童白喉、破伤风、百日咳免疫接种率。既然接种了，那就代表这个国家地区有了这个病的免疫能力。我们画出世界地图进行查看，数据为国家这16年的平均值进行绘制。(Is there a difference in immunization coverage in different regions? By checking the original data, we can see the rhythm information of three vaccines. They are the immunization rate of hepatitis B in 1-year-old children, the immunization coverage rate of 1-year-old children with polio (Pol3) and the immunization rate of diphtheria, tetanus and whooping cough in 1-year-old children. Since it has been vaccinated, it means that the country and region have the immunity of this disease. We draw a world map for viewing, and the data is the average of the country in the past 16 years.)  
免疫覆盖分别是1岁儿童乙型肝炎免疫接种率，1岁儿童脊髓灰质炎(Pol3)免疫覆盖率和1岁儿童白喉、破伤风、百日咳免疫接种率。我们首先看乙型肝炎免疫接种率。(Immunization coverage is the immunization rate of hepatitis B in 1-year-old children, the immunization coverage rate of polio (Pol3) in 1-year-old children, and the immunization rate of diphtheria, tetanus and whooping cough in 1-year-old children. Let's first look at the immunization rate of hepatitis B.)

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/0b11f109-c598-4564-bee8-5b5b6a49d0c2" />
</div>

1岁儿童乙型肝炎免疫接种率在全球范围内的接种率很高，通过得资料显示，乙型肝炎主要分布在东南亚和非洲热带地区欧美地区乙肝病毒的携带率较低，所以这也解释了美国和加拿大等地区的接种率较低的原因。下面是1岁儿童脊髓灰质炎(Pol3)免疫覆盖率。（The vaccination rate of hepatitis B in 1-year-old children is very high in the world. According to the data, hepatitis B is mainly distributed in Southeast Asia and the tropical regions of Africa, the carrying rate of hepatitis B virus is low in Europe and the United States, so this also explains the low vaccination rate in the United States, Canada and other regions. The following is the immunization coverage rate of polio (Pol3) in 1-year-old children.）

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/721cb51e-94a1-4adf-a74a-f52ec4ae7cd5" />
</div>

1岁儿童脊髓灰质炎(Pol3)免疫覆盖率在亚洲的覆盖率比在欧洲的覆盖率高。非洲国家的覆盖率较低，可能与当地的经济负担情况有关。大部分国家的脊髓灰质炎(Pol3)免疫覆盖率相对较高。最后为1岁儿童白喉、破伤风、百日咳免疫接种率。（The immunization coverage rate of polio (Pol3) in 1-year-old children is higher in Asia than in Europe. The low coverage rate of African countries may be related to the local economic burden. The immunization coverage rate of polio (Pol3) in most countries is relatively high. Finally, the immunization rate of diphtheria, tetanus and whooping cough in 1-year-old children.）

<div align=center>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/153f91d0-fa09-446b-a003-0c4f2f1b75a2" />
</div>

1岁儿童白喉、破伤风、百日咳免疫接种率在亚洲的覆盖率和欧洲的覆盖率高。非洲国家和印度的覆盖率较低，印度是人口大国，飞快增长的人口导致政府的压力加大不能保证所有人的接种，非洲国家可能与当地的经济负担与其他疾病还存在联系。（The immunization rate of diphtheria, tetanus and pertussis in 1-year-old children is high in Asia and in Europe. African countries and India have a low coverage rate. India is a country with a large population. The rapid population growth has led to increased pressure on the government to ensure vaccination for all. African countries may also be related to the local economic burden and other diseases.）

### 4.6学校教育对其他因素有什么影响？（What is the impact of school education on other factors?） 
通过压缩好的函数进行绘制散点图，展现受教育年限与其他因素的影响关系。画出所有关系之间的散点图之后再进行进一步的分析。（Draw a scatter plot through the compressed function to show the relationship between the years of education and other factors. Draw a scatter plot between all relationships and then carry out further analysis.）  
我们做出了教育年限与各个因素的散点图，从上到下从左到右分别是，预期寿命年龄，每 1000 人的男女成人死亡数，每 1000人的婴儿死亡人数，每1000 人五岁以下死亡人数，每 1000 个活产儿中在0-4岁死于艾滋病毒/艾滋病人数，每1000人报告的麻疹病例数，1岁儿童乙型肝炎免疫接种率，1岁儿童脊髓灰质炎(Pol3)免疫覆盖率，1岁儿童白喉、破伤风、百日咳免疫接种率，10至19岁儿童和青少年中的瘦弱率，5至9岁儿童中的瘦弱率，平均体重指数，人均酒精消费量，该国家人口，人均国内生产总值，政府一般卫生支出占政府总支出的百分比，卫生支出占人均国内生产总值的百分比，以资源收入构成为单位的人力发展指数。之间的关系。（We have made a scatter chart of the years of education and various factors. From top to bottom and from left to right, they are the expected life expectancy age, the number of male and female adult deaths per 1,000 people, the number of infant deaths per 1,000 people, the number of deaths under the age of five per 1,000 people, and 0 per 1,000 live births. - The number of HIV/AIDS deaths at the age of 4, the number of measles cases reported per 1,000 people, the immunization rate of hepatitis B in 1-year-old children, the immunization coverage rate of polio (Pol3) in 1-year-old children, the immunization rate of diphtheria, tetanus and whooping cough in 1-year-old children, children aged 10 to 19 and adolescents Thinning rate, thinning rate among children aged 5 to 9, average body mass index, per capita alcohol consumption, the country's population, per capita GDP, the percentage of government's general health expenditure to the total government expenditure, the percentage of health expenditure per capita GDP, and the human development index composed of resource income . The relationship between.）

<div align=center>
<img width="417" alt="image" src="https://github.com/user-attachments/assets/2676e9a0-6cff-404d-bddb-f9d50ef949ac" />
</div>

从总体来看受教育年限较少的部分，数据分布的点都很少。每 1000 人的婴儿死亡人数，每 1000 人五岁以下死亡人数，每 1000 个活产儿中在 0-4 岁死于艾滋病毒/艾滋病人数，每 1000 人报告的麻疹病例数，政府一般卫生支出占政府总支出的百分比，该国家人口和卫生支出占人均国内生产总值的百分比没有明显的相关性。很多图示在后期都呈现出数据聚集的情况，也体现出全球受教育年限的一个整体水平范围。（Generally speaking, in the parts with fewer years of education, there are very few points of data distribution. The number of infant deaths per 1,000 people, the number of deaths under the age of five per 1,000 people, the number of HIV/AIDS deaths per 1,000 live births aged 0-4, the number of measles cases reported per 1,000 people, and the percentage of total government expenditure on general health expenditure There is no obvious correlation between the country's population and health expenditure as a percentage of per capita GDP. Many diagrams show data aggregation in the later stage, which also reflects an overall horizontal range of the global years of education.）  
从预期寿命年龄与受教育年限的散点图中可以看出，随着受教育年限的增加，预期寿命也在增加，并且数据呈现出正相关的趋势。从每1000人的男女成人死亡数与受教育年限的散点图中可以看出，随着受教育年限的增加，每1000人的男女成人死亡数也在减少，并且数据呈现出负相关的趋势。（It can be seen from the scatter chart of life expectancy age and years of education that with the increase of years of education, life expectancy is also increasing, and the data shows a positive correlation trend. It can be seen from the scatter chart of the number of male and female adult deaths and the years of education per 1,000 people that with the increase of the number of years of education, the number of male and female adult deaths per 1,000 is also decreasing, and the data shows a negative correlation trend.）  
1岁儿童乙型肝炎免疫接种率，1岁儿童脊髓灰质炎(Pol3)免疫覆盖率，1岁儿童白喉、破伤风、百日咳免疫接种率。在图上变化范围相似归为一类进行分析，随着受教育年限的增加，数据分布也呈现出增加的分布，但数据出现了数据聚集的现象。整体呈现出正相关趋势，但相关性可能较低。（The immunization rate of hepatitis B in 1-year-old children, the immunization coverage rate of polio (Pol3) in 1-year-old children, and the immunization rate of diphtheria, tetanus and pertussis in 1-year-old children. The similar range of change on the chart is classified into one category for analysis. With the increase of years of education, the data distribution also shows an increasing distribution, but the data has a phenomenon of data aggregation. Overall, there is a positive correlation trend, but the correlation may be low.）  
10至19岁儿童和青少年中的瘦弱率，5至9岁儿童中的瘦弱率。在图上变化范围相似归为一类进行分析，数据分布可以看到随着受教育年限的增加，数据分布也呈现出减少的趋势，也可以看出数据此事集中于两类。这两类区别应该源自于发达国家与发展中国家的区别。但总体趋势是在减小。平均体重指数可以看到数据聚集为了两类，两类的区别应该为发展中与发达国家的分类，但大体方向是随着受教育年限的增加不断变大。两者为正向关系。(The thinning rate among children and adolescents aged 10 to 19, and the thinning rate among children aged 5 to 9. The similar range of change on the chart is classified into one category for analysis. The data distribution can be seen that with the increase of the number of years of education, the data distribution also shows a decreasing trend, and it can also be seen that the data is concentrated in two categories. These two types of differences should come from the difference between developed and developing countries. But the general trend is decreasing. The average body mass index shows that the data is gathered into two categories. The difference between the two categories should be classified as developing and developed, but the general direction is to increase with the increase of years of education. The two are positive.)

非新数据集，结果仅作可视化参考。（Non-new data sets, the results are for visual reference only.）

































































