import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter
# Загрузка данных из CSV-файла
df = pd.read_csv("E://yt/filmdata.csv")

# numeric_columns = ['Run Time in minutes', 'Movie Rating', 'Votes', 'MetaScore', 'Gross']
# df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# duplicates_count = df.duplicated().sum()
# if duplicates_count > 0:
#     print(f'Обнаружено {duplicates_count} дубликатов. Удаление дубликатов...')
#     df = df.drop_duplicates()

##1
# df['Run Time in minutes'] = pd.to_numeric(df['Run Time in minutes'], errors='coerce')
# average_runtime_by_year = df.groupby('Year of Release')['Run Time in minutes'].mean()
# average_runtime_by_year.plot(kind='line', title='Средняя длина фильмов с течением времени')
# plt.xlabel('Год выпуска')
# plt.ylabel('Средняя длина фильмов (в минутах)')
# plt.show()

##2
# most_prolific_director = df['Director'].value_counts().idxmax()
# print(f'Самый продуктивный режиссер: {most_prolific_director}')

##3
# genres_by_decade = df.groupby(df['Year of Release'] // 10 * 10)['Genre'].value_counts().unstack()
# genres_by_decade.plot(kind='bar', stacked=True, title='Популярные жанры по десятилетиям')
# plt.xlabel('Десятилетие')
# plt.ylabel('Количество фильмов')
# plt.show()

##4
# actor_combinations = df['Stars'].apply(lambda x: list(combinations(x.split(', '), 2)) if pd.notnull(x) else [])
# flat_combinations = [item for sublist in actor_combinations for item in sublist]
# common_actor_combinations = Counter(flat_combinations).most_common(10)
# print('Наиболее часто снимающиеся вместе актеры:')
# for combination, count in common_actor_combinations:
#     print(f'{combination}: {count} раз')

# # 5 Как распределены оценки фильмов (Movie Rating) в наборе данных?
# df['Movie Rating'] = pd.to_numeric(df['Movie Rating'], errors='coerce')
# df['Movie Rating'].plot(kind='hist', bins=20, edgecolor='black', title='Распределение оценок фильмов')
# plt.xlabel('Оценка фильма')
# plt.ylabel('Частота')
# plt.show()

# #6 Какова динамика изменения кассовых сборов (Gross) с течением времени?
# df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')
# df.groupby('Year of Release')['Gross'].sum().plot(kind='line', marker='o', title='Динамика кассовых сборов с течением времени')
# plt.xlabel('Год выпуска')
# plt.ylabel('Общие кассовые сборы')
# plt.show()