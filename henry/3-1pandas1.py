#pandas 패키지는 1차원배열인 시리즈(series)
#행과열로 이루어진 2차원 배열인 데이터프레임(DataFrame)으로 데이터 분석 처리

#1차원배열 시리즈 
import pandas as pd

dict_data = {'a':1,'b':2,'c':3}
series = pd.Series(dict_data)
# print(series)
# print(series.index)
# print(series.values)


list_data = ['a','b','c']
series_2 = pd.Series(list_data)
print(series_2)


# pd.Series = ("dddddddddd")
