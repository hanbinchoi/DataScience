import pandas as pd
import numpy as np

df=pd.DataFrame({'column_a':[3,'?',2,5],
                 'column_b':['*',4,5,6],
                 'column_c':['+',3,2,'&'],
                 'column_d':[5,'?',7,'!']})


print(df)

# 특정 기호를 NaN으로 대체 
df.replace({'?':np.nan,'*':np.nan,'+':np.nan,'&':np.nan,'!':np.nan}, inplace=True)

print(df)

# NaN 이 있는지 없는지 True or False 로 출력
print(df.isna().any())

# NaN이 있으면 개수 합 출력 
print(df.isna().sum())

# NaN값이 1개라도 있으면 그 열(raw) 삭제
df.dropna(axis=0,how='any',inplace=True)
print(df)

df=pd.DataFrame({'column_a':[3,'?',2,5],
                 'column_b':['*',4,5,6],
                 'column_c':['+',3,2,'&'],
                 'column_d':[5,'?',7,'!']})
df.replace({'?':np.nan,'*':np.nan,'+':np.nan,'&':np.nan,'!':np.nan}, inplace=True)

# 모든 값이 NaN 값이면 그 열(raw) 삭제
df.dropna(axis=0,how='all',inplace=True)
print(df)


df=pd.DataFrame({'column_a':[3,'?',2,5],
                 'column_b':['*',4,5,6],
                 'column_c':['+',3,2,'&'],
                 'column_d':[5,'?',7,'!']})
df.replace({'?':np.nan,'*':np.nan,'+':np.nan,'&':np.nan,'!':np.nan}, inplace=True)

# 모든 raw를 기준으로 NaN이 아닌값이 1개 이상있으면 삭제 안하고 나머진 삭제 
df.dropna(axis=0,thresh=1,inplace=True)
print(df)

df=pd.DataFrame({'column_a':[3,'?',2,5],
                 'column_b':['*',4,5,6],
                 'column_c':['+',3,2,'&'],
                 'column_d':[5,'?',7,'!']})
df.replace({'?':np.nan,'*':np.nan,'+':np.nan,'&':np.nan,'!':np.nan}, inplace=True)

# 모든 raw를 기준으로 NaN이 아닌값이 2개 이상있으면 삭제 안하고 나머진 삭제
df.dropna(axis=0,thresh=2,inplace=True)
print(df)

df=pd.DataFrame({'column_a':[3,'?',2,5],
                 'column_b':['*',4,5,6],
                 'column_c':['+',3,2,'&'],
                 'column_d':[5,'?',7,'!']})
df.replace({'?':np.nan,'*':np.nan,'+':np.nan,'&':np.nan,'!':np.nan}, inplace=True)

# 모든 raw를 기준으로 NaN이 아닌값이 3개 이상있으면 삭제 안하고 나머진 삭제 
df.dropna(axis=0,thresh=3,inplace=True)
print(df)

df=pd.DataFrame({'column_a':[3,'?',2,5],
                 'column_b':['*',4,5,6],
                 'column_c':['+',3,2,'&'],
                 'column_d':[5,'?',7,'!']})
df.replace({'?':np.nan,'*':np.nan,'+':np.nan,'&':np.nan,'!':np.nan}, inplace=True)

# NaN 값을 다 100으로 채움
print(df.fillna(100))

# NaN 값을 각 컬럼 평균으로 채움
mean = df.mean()
print(df.fillna(mean))

# NaN 값을 각 컬럼의 중간값으로 채움
median = df.median()
print(df.fillna(median))

# NaN 값을 각 컬럼의 바로 위에 있는 값으로 채워줌 (없으면 그대로 NaN)
print(df.fillna(axis=0,method='ffill'))

# NaN 값을 각 컬럼의 바로 아래에 있는 값으로 채워줌 (없으면 그대로 NaN)
print(df.fillna(axis=0,method='bfill'))

# NaN 값을 각 컬럼의 바로 아래에 있는 값으로 채워주는데 연속으로 NaN이면 1개만 채워줌 (없으면 그대로 NaN)
print(df.fillna(axis=0,method='bfill',limit=1))


