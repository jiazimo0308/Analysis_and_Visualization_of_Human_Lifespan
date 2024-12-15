# Analysis_and_Visualization_of_Human_Lifespan
人类寿命分析与可视化.  
Analysis and Visualization of Human Lifespan

## 1. 数据背景(Data background)
世界卫生组织(WHO)下属的全球卫生观察站(GHO)数据库跟踪了全球众多国家 的健康状况以及许多其他相关因素。现向公众开放一份关于预期寿命、健康因素、经济情况有关的数据集，数据集中综合了2000年至2015年193个国家的数据，由于一些不太知名的国家的数据查找较困难，如瓦努阿图、汤加、多哥、佛得角等，因此该数据集中已排除这些国家，最终由22列、2938行组成.
(The Global Health Observatory (GHO) database under the World Health Organization (WHO) tracks the health status of many countries around the world and many other related factors. A data set related to life expectancy, health factors and economic conditions is now open to the public. The data set integrates data from 193 countries from 2000 to 2015, because it is difficult to find data from some lesser-known countries, such as Vanuatu, Tonga, Togo, Dejiao, etc., so these countries have been excluded from the data set, and eventually consist of 22 columns and 2938 rows.)

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

另外，附加一份各个国家的信息表(2015年).(In addition, provide an information form of each country (2015).)

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

## 2. 数据概况(Data overview)
利用python函数对Life Expectancy Data数据集进行初步的数据预览。并做出如下数据预览结果。(Use the python function to preview the data set of Life Expectancy Data. And make the following data preview results.)

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

其中数据的数值类型共有三种。Obiect类型的有两种，int类型有四种，其余为float64类型数据。共2938行数据，22列特征。(Among them, there are three types of numerical data. There are two types of Obiect type, four types of int type, and the rest are float64 type data. A total of 2938 rows of data and 22 columns of features.)

利用python函数对Life Expectancy Data数据集进行初步的数据预览。并做出如下数据预览结果。(Use the python function to preview the data set of Life Expectancy Data. And make the following data preview results.)

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

其中数据的数值类型共有两种。Obiect类型的有七种，int类型有一种。共227行，8列特征。 (Among them, there are two numerical types of data. There are seven types of Obiect and one type of int. A total of 227 rows, 8 columns of features.)

## 3.数据预处理(Data preprocessing)
观察数据可以看出全球城市的情况，为了表现出城市正常的数据来填充缺失值。我选用众数填充为缺失值进行处理。使用众数体现一个所有国家相对正常下的数据状态。(Observing the data can see the situation of cities around the world. In order to show the normal data of the city, the missing values are filled in. I choose to fill in the number of missing values to process it. The use of crowd numbers reflects the relatively normal data status of all countries.)

## 4.数据分析与可视化(Data analysis and visualization)
利用pyecharts进行全世界地图的绘制。绘制出全球各个地点这几年预期寿命的平均值。利用颜色来展现出每个国家平均预期年龄的差别。通过数据切分，切选出国家和预期寿命并通过mean()函数来求得平均寿命。之后通过Map()函数对各个国家进行可视化作图。看出全球预期寿命分布的具体情况。(Use pyecharts to draw maps around the world. Draw the average life expectancy of various locations around the world in recent years. Use color to show the difference in the average expected age of each country. Through data cutting, the country and life expectancy are selected and the average life expectancy is obtained through the mean() function. After that, visualize and map each country through the Map() function. See the specific distribution of global life expectancy.)  
通过pyecharts绘制出全球预期寿命分布情况。(Draw the distribution of global life expectancy through pyecharts.)

<img width="400" alt="image" src="https://github.com/user-attachments/assets/4f1469b9-85fc-4907-a85e-74acec601d76" />

由全球预期寿命分布图可以看到，预期寿命较高的国家分布。主要分布在北半球且发达国家，东半球的预期寿命要小于西半球的预期寿命。非洲的预期寿命整体最差。且北美洲，欧洲和大洋洲的预期寿命最高。




  
