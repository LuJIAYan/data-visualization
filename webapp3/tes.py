# # import pandas as pd
# # import numpy as np
# # import plotly as py
# # import datetime
# # #
# # # ted = pd.read_csv("./static/data/ted_main.csv")
# # # a = ted['film_date'].unique()
# # #
# # # ted['film_date'] = ted['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
# # # ted['published_date'] = ted['published_date'].apply(
# # #     lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
# # # a = ted['views']
# # # import plotly.express as px
# # # ted['duration'] = ted['duration']/60
# # # views_ted = ted[['main_speaker', 'title','published_date', 'views','comments','tags','speaker_occupation','num_speaker']].sort_values(by = 'views', ascending = False)
# # # # fig.show()
# # # import numpy as np
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns
# # #
# # # import plotly.graph_objects as go
# # #
# # # # import numpy as np
# # # # import ast
# # # # views_ted = ted[['main_speaker', 'title','published_date', 'views','comments','tags','speaker_occupation','num_speaker']].sort_values(by = 'comments', ascending = False)
# # # # ted['tags'] = ted['tags'].apply(lambda x: ast.literal_eval(x))
# # # # s = ted.apply(lambda x: pd.Series(x['tags']),axis=1).stack().reset_index(level=1, drop=True)
# # # # s.name = 'title'
# # # # theme_df = ted.drop('title', axis = 1).join(s)
# # # # x=theme_df['comments']
# # # # y = theme_df['title']
# # # # # Use `y` argument instead of `x` for horizontal histogram
# # # #
# # # # fig = go.Figure(data=[go.Histogram(y=y)])
# # # # fig.show()
# # # occupation_df = ted.groupby('speaker_occupation').count().reset_index()[['speaker_occupation', 'comments']]
# # # occupation_df.columns = ['speaker_occupation', 'talk_times']
# # # occupation_df = occupation_df.sort_values('talk_times', ascending = False)
# # #
# # # ted = pd.read_csv("./static/data/ted_main.csv")
# # # ted['film_date'] = ted['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
# # # ted['published_date'] = ted['published_date'].apply(
# # #     lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
# # # month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# # # day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# # # ted['month'] = ted['film_date'].apply(lambda x: month_order[int(x.split('-')[1]) - 1])
# # # month_df = pd.DataFrame(ted['month'].value_counts()).reset_index()
# # # month_df.columns = ['month', 'talk_times']
# # # ted['years'] = ted['published_date'].apply(lambda x: x.split('-')[2])
# # # year_df = pd.DataFrame(ted['years'].value_counts().reset_index())
# # # year_df.columns = ['years', 'times']
# # # # sns.barplot(x = 'month', y = 'talk_times', data = month_df, order = month_order)
# # # print(year_df.years.values)
# # # print(year_df.times.values)
# # # print(month_df)
# # years2 = pd.read_excel("./static/data/years2.xlsx", encoding='utf-8')
# # years_sum = years2.groupby('years')['views', 'comments'].sum()
# # df_sum = years_sum.T
# # print(df_sum.columns.values)
# # print([pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df_sum.columns.values])
#
# def count_word(path):
#     count = {}
#     with open(path) as f:
#         lines = f.readlines()
#     for line in lines:
#         word = line.strip().split(' ')[0]
#         print(word)
#         if word in count:
#             count[word] = count[word] + 1
#         else:
#             count[word] = 1
#     print(count)
#
#
# path = input("请输入文件名称：")
# count_word(path)
import pandas as pd

df = pd.read_csv(r"E:\pythonProject\HINGAN\HINGAN.v1\text8\18flask_LHN402017\static\data\themes2.csv")
df = df[['themes', "years"]].values.tolist()
res = {}
for i in df:
    if i[0] not in res:
        res[i[0]] = {i[1]: 1}
    else:
        if i[1] not in res[i[0]]:
            res[i[0]][i[1]] = 1
        else:
            res[i[0]][i[1]] += 1
print(res)
print(df)
