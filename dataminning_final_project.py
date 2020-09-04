# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:12:32 2020

@author: admin
"""


import pandas as pd


datas=pd.read_csv("D:\데마\Measurement_summary.csv")
datas.dtypes

import matplotlib.pyplot as plt





#일별로 평균내기.

group=datas[['SO2','NO2','O3','CO','PM2.5','PM10']].groupby(datas['Measurement date'])
a=group.mean()
a
a['일시']=a.index
a['index']=range(a.shape[0])
a=a.set_index('index')
a['일시']=pd.to_datetime(a['일시'])
a.dtypes

#추세확인
plt.plot(a['일시'],a['PM10'])
plt.rcParams["figure.figsize"]=(100,20)
plt.show()

#계절변수 추가
Season=[]
spring=[3,4,5]
summer=[6,7,8]
fall=[9,10,11]
winter=[12,1,2]
for i in range(a.shape[0]):    
    if a.iloc[i]['일시'].month in spring:
        Season.append(1)
    if a.iloc[i]['일시'].month in summer:
        Season.append(2)
    if a.iloc[i]['일시'].month in fall:
        Season.append(3)
    if a.iloc[i]['일시'].month in winter:
        Season.append(4)
a['계절']=Season
            
    

#기후데이터
weather=pd.read_csv("D:\\데마\\a2017기후데이터.csv",encoding="ISO-8859-1")
weather2=pd.read_csv("D:\\데마\\a2018기후데이터.csv",encoding="ISO-8859-1")
weather3=pd.read_csv("D:\\데마\\a2019기후데이터.csv",encoding="ISO-8859-1")
weather=weather.append(weather2)
weather=weather.append(weather3)

weather.columns=['지점','지점명','일시','기온(℃)','강수량(mm)','풍속(m/s)','풍향(16방위)','습도(%)','이슬점온도(℃)','현지기압(hPa)','일조(hr)']

del weather['지점']
del weather['지점명']
#결측치처리
weather.isnull().sum()
light=weather['일조(hr)']
rain=weather['강수량(mm)']
arc=weather['풍향(16방위)']
wind=weather['풍속(m/s)']
light=light.fillna(0)
rain=rain.fillna(0)
arc=arc.fillna(0)
wind=wind.fillna(0)

weather['일조(hr)']=light
weather['강수량(mm)']=rain
weather['풍향(16방위)']=arc
weather['풍속(m/s)']=wind
weather.isnull().sum()

weather=weather.fillna(weather.mean())
weather.isnull().sum()

weather['일시']=pd.to_datetime(weather['일시']) #시간으로 바꿔주기.

merged_data=pd.merge(a,weather)
merged_data.dtypes
colnames=['SO2','NO2','O3','CO','PM25','PM10','time','season','temp','rain','wind','arc','water','watertemp','hpa','hr']
merged_data.columns=colnames

#풍향변수 더미코드
D=pd.get_dummies(merged_data['arc'])
dataset_with_d=merged_data.copy()
del dataset_with_d['arc']
D['time']=dataset_with_d['time']
dataset_with_d=pd.merge(dataset_with_d,D)
colnames2=['SO2','NO2','O3','CO','PM25','PM10','time','season','temp','rain','wind','water','watertemp','hpa','hr','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
dataset_with_d.columns=colnames2

#교통데이터 추가해보자.
for year in range(2017,2018):
    for month in range(1,13):
        if year==2017 and month==1:
            traf=pd.read_excel("D:\데마\%d %d월 서울시 교통량 조사자료.xlsx"%(year,month))
        else:
            t=pd.read_excel("D:\데마\%d %d월 서울시 교통량 조사자료.xlsx"%(year,month))
            traf=traf.append(t)
for year in range(2018,2020):
    for month in range(1,13):
        if year==2018 and month==1:
            traf2=pd.read_excel("D:\데마\%d %d월 서울시 교통량 조사자료.xlsx"%(year,month))
        else:
            t=pd.read_excel("D:\데마\%d %d월 서울시 교통량 조사자료.xlsx"%(year,month))
            traf2=traf2.append(t)
traf.columns
group2=traf[['0시', '1시', '2시', '3시', '4시',
       '5시', '6시', '7시', '8시', '9시', '10시', '11시', '12시', '13시', '14시', '15시',
       '16시', '17시', '18시', '19시', '20시', '21시', '22시', '23시']].groupby(traf['일자'])
a2=group2.mean()
a2
group3=traf2[['0시', '1시', '2시', '3시', '4시',
       '5시', '6시', '7시', '8시', '9시', '10시', '11시', '12시', '13시', '14시', '15시',
       '16시', '17시', '18시', '19시', '20시', '21시', '22시', '23시']].groupby(traf2['일자'])
a3=group3.mean()
a3
traf_sample=a2.append(a3)
traf_sample.isnull().sum()
traf_sample=traf_sample.fillna(traf_sample.mean())

date=merged_data['time']
sumoftraf=[]
for row in range(traf_sample.shape[0]):
    for col in list(traf_sample):
        sumoftraf.append(traf_sample.iloc[row][col])


date=[]
for year in range(2017,2020):
    for month in range(1,13):
        if month in [1,3,5,7,8,10,12]:
            for day in range(1,32):
                if month<10 and day<10:
                    date.append("%d-0%d-0%d"%(year,month,day))
                elif month>=10 and day<10: 
                    date.append("%d-%d-0%d"%(year,month,day))
                elif month<10 and day>=10: 
                    date.append("%d-0%d-%d"%(year,month,day))
                else: date.append("%d-%d-%d"%(year,month,day))
        elif month in [4,6,9,11]:
            for day in range(1,31):
                if month<10 and day<10:
                    date.append("%d-0%d-0%d"%(year,month,day))
                elif month>=10 and day<10: 
                    date.append("%d-%d-0%d"%(year,month,day))
                elif month<10 and day>=10: 
                    date.append("%d-0%d-%d"%(year,month,day))
                else: date.append("%d-%d-%d"%(year,month,day))
        else:
            for day in range(1,29):
                if month<10 and day<10:
                    date.append("%d-0%d-0%d"%(year,month,day))
                elif month>=10 and day<10: 
                    date.append("%d-%d-0%d"%(year,month,day))
                elif month<10 and day>=10: 
                    date.append("%d-0%d-%d"%(year,month,day))
                else: date.append("%d-%d-%d"%(year,month,day))
time=[]
for i in range(0,24):
    if i<10:
        time.append('0%d:00:00'%i)
    else:
        time.append('%d:00:00'%i)
datetime=[]
for i in range(len(date)):
    for j in time:
        datetime.append(date[i]+' '+j)

traf_real=pd.DataFrame({'time':datetime,'traf':sumoftraf})
traf_real['time']=pd.to_datetime(traf_real['time'])

#풍향삭제
del merged_data['arc']

merged_data2=pd.merge(merged_data,traf_real)
merged_data2.isnull().sum()

#풍향쓴거
dataset2=pd.merge(dataset_with_d,traf_real)
dataset2.isnull().sum()

import seaborn as sns
from patsy import dmatrices
import statsmodels.api as sm;
from statsmodels.stats.outliers_influence import variance_inflation_factor

#다중공선성 높은걸 뺌 이슬점온도 
y, X = dmatrices('PM25 ~ NO2+SO2+O3+CO+temp+rain+wind+water+watertemp+hpa+hr+season+traf', dataset2, return_type = 'dataframe')
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns 
vif
#이슬점뺀
y, X = dmatrices('PM25 ~ NO2+SO2+O3+CO+temp+rain+wind+water+hpa+hr+season+traf', dataset2, return_type = 'dataframe')
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns 
vif

y, X = dmatrices('PM10 ~ NO2+SO2+O3+CO+temp+rain+wind+water+hpa+hr+season+traf', dataset2, return_type = 'dataframe')
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns 
vif

#풍향더미변수,이슬점온도 빼고 티테스트 hpa,hr제거

#no2, hr 
lm = sm.OLS(dataset2['PM10'], dataset2[['SO2','NO2','O3','CO','temp','rain','wind','water','hpa','hr','season','traf']])
result=lm.fit()
result.summary()

#hr
lm = sm.OLS(dataset2['PM25'], dataset2[['SO2','NO2','O3','CO','temp','rain','wind','water','hpa','hr','season','traf']])
result=lm.fit()
result.summary()
#계수들 정규화 한번해보자 <안해도됌
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
X_scaled=pd.DataFrame(X_scaled)
X_scaled.columns=list(X)
X_scaled.loc[X_scaled['Intercept'] ==0, 'Intercept'] = 1

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X_scaled.values, i) for i in range(X.shape[1])]
vif["features"] = X_scaled.columns 
vif

#정규화 해야한다. 시작 no2,hr만하자

datasets_copy=dataset2.copy()

del datasets_copy['time']

scaler = StandardScaler()
scaler.fit(datasets_copy)
data_scaled = scaler.transform(datasets_copy)
data_scaled=pd.DataFrame(data_scaled)
data_scaled.columns=list(datasets_copy)

del dataset2['NO2']
del dataset2['hr']


dataset2['NO2']=data_scaled['NO2']
dataset2['hr']=data_scaled['hr']


#ttest해보자 << 정규화후에 하는거임
lm = sm.OLS(dataset2['PM10'], dataset2[['SO2','NO2','O3','CO','temp','rain','wind','water','hpa','hr','season','traf']])
result=lm.fit()
result.summary()
lm = sm.OLS(dataset2['PM25'], dataset2[['SO2','NO2','O3','CO','temp','rain','wind','water','hpa','hr','season','traf']])
result=lm.fit()
result.summary()
#여전히 피밸류가 높다. 그래서 no2와 hr 제거.



#모델링
#'SO2','NO2','O3','CO',
#선형회귀 풍향뺀거. <이거말고 밑에거
X=merged_data2[['SO2','O3','CO','temp','rain','wind','water','season','traf','hpa']]
Y=merged_data2[['PM25']]

from sklearn.model_selection import train_test_split 

Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
from sklearn.linear_model import LinearRegression

reg=LinearRegression()
reg.fit(Xtr,Ytr)
r2=reg.score(Xts,Yts)
X.shape[1]
n=X.shape[0]
p=Xts.shape[1]
k=(n-1)/(n-p-1)
k*(1-r2)
adj_r2=1-k*(1-r2)
adj_r2


#풍향넣은거 선형회귀 <<<이거써야함.
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Y=dataset2[['PM10']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
reg.fit(Xtr,Ytr)
reg.score(Xts,Yts)

regmo=sm.OLS(Ytr,Xtr)
reg_result=regmo.fit()
reg_result.summary()


X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Y=dataset2[['PM25']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
reg.fit(Xtr,Ytr)
reg.score(Xts,Yts)

regmo=sm.OLS(Ytr,Xtr)
reg_result=regmo.fit()
reg_result.summary()


#미세먼지나 초미세먼지나 똑같다고 판단.
mi=merged_data2['PM10']
chomi=merged_data2['PM25']
import operator

aver=map(operator.add,mi,chomi)
ave=[]
for i in aver:
    ave.append(round(i/2,2))

dataset2['average']=ave    

lm = sm.OLS(merged_data2['average'], merged_data2[['SO2','NO2','O3','CO','temp','rain','wind','water','watertemp','season','traf']])
result=lm.fit()
result.summary()


#에버리지에대한 다중공선성 (사실안해봐도됌)
y, X = dmatrices('average ~ temp+rain+wind+water+season+traf', merged_data2, return_type = 'dataframe')
X
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns 
vif

#에버리지로 선형회귀
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Y=dataset2[['average']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)

reg=LinearRegression()
reg.fit(Xtr,Ytr)
reg.score(Xts,Yts)

regmo=sm.OLS(Ytr,Xtr)
reg_result=regmo.fit()
reg_result.summary()


#로지스틱 범주4개 <<이거말고 밑에거하자
from sklearn.linear_model import LogisticRegression 


merged_data2.loc[merged_data2['PM10'] <31, 'PM10'] = 0
merged_data2.loc[merged_data2['PM10'] >=151, 'PM10'] = 3
merged_data2.loc[merged_data2['PM10'] >=81, 'PM10'] = 2
merged_data2.loc[merged_data2['PM10'] >=31, 'PM10'] = 1


Y=merged_data2[['PM10']] 
X=merged_data2[['SO2','NO2','O3','CO','temp','rain','wind','water','traf','season']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
logreg=LogisticRegression(multi_class='multinomial')
logreg.fit(Xtr,Ytr)

logreg.score(Xts,Yts)
#풍향쓴거 미세먼지 로지스틱 범주 4개
dataset2=pd.merge(dataset_with_d,traf_real)
dataset2['average']=ave
dataset2.loc[dataset2['PM10'] <31, 'PM10'] = 0
dataset2.loc[dataset2['PM10'] >=151, 'PM10'] = 3
dataset2.loc[dataset2['PM10'] >=81, 'PM10'] = 2
dataset2.loc[dataset2['PM10'] >=31, 'PM10'] = 1


Y=dataset2[['PM10']] 
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
logreg=LogisticRegression(multi_class='multinomial')
logreg.fit(Xtr,Ytr)

logreg.score(Xts,Yts)

logreg.coef_

#초미세먼지에 대해 로지스틱 <<이거말고 밑에거
merged_data2=pd.merge(merged_data,traf_real)
merged_data2.loc[merged_data2['PM25'] <16, 'PM25'] = 0
merged_data2.loc[merged_data2['PM25'] >=76, 'PM25'] = 3
merged_data2.loc[merged_data2['PM25'] >=36, 'PM25'] = 2
merged_data2.loc[merged_data2['PM25'] >=16, 'PM25'] = 1


Y=merged_data2[['PM25']] 
X=merged_data2[['SO2','NO2','O3','CO','temp','rain','wind','water','traf','season']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
logreg=LogisticRegression(multi_class='multinomial')
logreg.fit(Xtr,Ytr)

logreg.score(Xts,Yts)
#초미세먼지에 대해 풍향써서
dataset2.loc[dataset2['PM25'] <16, 'PM25'] = 0
dataset2.loc[dataset2['PM25'] >=76, 'PM25'] = 3
dataset2.loc[dataset2['PM25'] >=36, 'PM25'] = 2
dataset2.loc[dataset2['PM25'] >=16, 'PM25'] = 1


Y=dataset2[['PM25']] 
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
logreg=LogisticRegression(multi_class='multinomial')
logreg.fit(Xtr,Ytr)

logreg.score(Xts,Yts)

#로지스틱 평균으로 범주4개

dataset2.loc[dataset2['average'] <23.5, 'average'] = 0
dataset2.loc[dataset2['average'] >=113.5, 'average'] = 3
dataset2.loc[dataset2['average'] >=58.5, 'average'] = 2
dataset2.loc[dataset2['average'] >=23.5, 'average'] = 1

Y=dataset2[['average']] 
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)
logreg=LogisticRegression(multi_class='multinomial')
logreg.fit(Xtr,Ytr)

logreg.score(Xts,Yts)


#디시젼트리 한번 해보자.

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
grid={'max_depth':range(1,len(list(dataset2))+1)}

Y=dataset2[['PM10']] 
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)

t1=DecisionTreeClassifier(max_depth=5)
t1.fit(Xtr, Ytr)
t1.score(Xts,Yts) #정확도 계산
t1.score(Xtr,Ytr)

Y=dataset2[['PM25']] 
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)

t1=DecisionTreeClassifier(max_depth=5)
t1.fit(Xtr, Ytr)
t1.score(Xts,Yts) #정확도 계산
t1.score(Xtr,Ytr)

Y=dataset2[['average']] 
X=dataset2[['SO2','O3','CO','temp','rain','wind','water','season','hpa','traf','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']]
Xtr, Xts, Ytr, Yts = train_test_split(X, Y, test_size=0.2,shuffle=True,random_state=10)

t1=DecisionTreeClassifier(max_depth=5)
t1.fit(Xtr, Ytr)
t1.score(Xts,Yts) #정확도 계산
t1.score(Xtr,Ytr)

#맥스뎁쓰.
grid_m=GridSearchCV(t1,param_grid=grid,cv=5,return_train_score=True)
grid_m.fit(Xtr,Ytr)
grid_m.best_params_
grid_m.score(Xts,Yts)
grid_m.score(Xtr,Ytr)
#트리
from sklearn import tree
fig=plt.figure(figsize=(100,200))
fig=plt.figure(dpi=100)
tree.plot_tree(t1)
plt.show()










