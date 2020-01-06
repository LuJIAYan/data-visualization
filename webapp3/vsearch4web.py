import plotly as py
import cufflinks as cf
import pandas as pd
from flask import Flask
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline, Grid, Page, EffectScatter
from flask import render_template, request
import datetime

app = Flask(__name__)
df = pd.read_csv(r"./static/data/themes2.csv")
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

@app.route('/')
def index_baxr():
    return render_template("index_x.html")

# 浏览量和评论数的关系
@app.route('/Scatter')
def index_bar():
    ted = pd.read_csv("./static/data/ted_main.csv")
    ted['film_date'] = ted['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    ted['published_date'] = ted['published_date'].apply(
        lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    r = (
        EffectScatter()
            .add_xaxis(ted['views'].values.tolist())
            .add_yaxis('评论数', ted['comments'].values.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="浏览量和评论数的关系", subtitle="由右边图片，并根据相关系数矩阵我们可以看出二者的皮尔逊相关系数为0.53，具有显著相关性。"),
            xaxis_opts=opts.AxisOpts(
                type_="value",  # x轴数据类型是连续型的
                min_=0  # x轴范围最小为20
            ))
    )
    return render_template('index.html',
                           myechart=r.render_embed(),select=list(res.keys()))


# 浏览量和评论数TOP10视频是
@app.route('/bar1')
def index_bar_every_1_tp():
    ted = pd.read_csv("./static/data/ted_main.csv")
    ted['film_date'] = ted['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    ted['published_date'] = ted['published_date'].apply(
        lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    views_ted = ted[['main_speaker', 'title', 'published_date', 'views', 'comments', 'tags', 'speaker_occupation',
                     'num_speaker']].sort_values(by='views', ascending=False)

    views_ted_1 = ted[['main_speaker', 'title', 'published_date', 'views', 'comments', 'tags', 'speaker_occupation',
                       'num_speaker']].sort_values(by='comments', ascending=False)
    bar = (
        Bar()
            .add_xaxis(views_ted.head(10).main_speaker.values.tolist())
            .add_yaxis("top10", views_ted.head(10).views.values.tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="浏览量和评论数TOP10视频"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    bar1 = (
        Bar()
            .add_xaxis(views_ted_1.head(10).main_speaker.values.tolist())
            .add_yaxis("top10", views_ted_1.head(10).comments.values.tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="浏览量和评论数TOP10视频"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(bar1, grid_opts=opts.GridOpts(pos_top="60%"))
    )

    return render_template('index.html',
                           myechart=grid.render_embed(),select=list(res.keys()))


# 主讲人都来自什么职业
@app.route('/bar')
def index_bar_every():
    ted = pd.read_csv("./static/data/ted_main.csv")
    ted['film_date'] = ted['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    ted['published_date'] = ted['published_date'].apply(
        lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    occupation_df = ted.groupby('speaker_occupation').count().reset_index()[['speaker_occupation', 'comments']]
    occupation_df.columns = ['speaker_occupation', 'talk_times']
    occupation_df = occupation_df.sort_values('talk_times', ascending=False)

    bar = (
        Bar()
            .add_xaxis(occupation_df.head(10).speaker_occupation.values.tolist())
            .add_yaxis("top10", occupation_df.head(10).talk_times.values.tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="主讲人都来自职业"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True)
        )
    )

    return render_template('index.html',
                           myechart=bar.render_embed(),select=list(res.keys())
                           )


# 每个时间段的评论和浏览量
@app.route('/time')
def index_bar_every_X():
    ted = pd.read_csv("./static/data/ted_main.csv")
    ted['film_date'] = ted['film_date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    ted['published_date'] = ted['published_date'].apply(
        lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y'))
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ted['month'] = ted['film_date'].apply(lambda x: month_order[int(x.split('-')[1]) - 1])
    month_df = pd.DataFrame(ted['month'].value_counts()).reset_index()
    month_df.columns = ['month', 'talk_times']
    ted['years'] = ted['published_date'].apply(lambda x: x.split('-')[2])
    year_df = pd.DataFrame(ted['years'].value_counts().reset_index())
    year_df.columns = ['years', 'times']
    bar = (
        Bar()
            .add_xaxis(month_df.month.values.tolist())
            .add_yaxis("", month_df.talk_times.values.tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="每个月评论量及每年视频产出个数", subtitle="TED演讲视频有季节特点，TED演讲视频2010后基本稳定在250个"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    bar1 = (
        Line()
            .add_xaxis(year_df.years.values.tolist()[::-1])
            .add_yaxis("", year_df.times.values.tolist()[::-1])
            .set_global_opts(title_opts=opts.TitleOpts())
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(bar1, grid_opts=opts.GridOpts(pos_top="60%"))
    )

    return render_template('index.html',
                           myechart=grid.render_embed(),select=list(res.keys())
                           )


@app.route('/line')
def index_bar_every_y():
    years2 = pd.read_excel("./static/data/years2.xlsx", encoding='utf-8')
    years_sum = years2.groupby('years')['views', 'comments'].sum()
    df_sum = years_sum.T
    bar = (
        Line()
            .add_xaxis([pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df_sum.columns.values])
            .add_yaxis("views", df_sum.loc["views", :].values.tolist())
            .add_yaxis("comments", df_sum.loc["comments", :].values.tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="不同年份观看和评论对比"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True)
        )
    )

    return render_template('index.html', myechart=bar.render_embed(),select=list(res.keys()))


@app.route('/123')
def index_bar_every_z():
    prevention = request.args.get("city", "children")

    bar = (
        Bar()
            .add_xaxis(list(res[prevention].keys()))
            .add_yaxis("", list(res[prevention].values()))
            .set_global_opts(title_opts=opts.TitleOpts())
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    return render_template('index_1.html', myechart=bar.render_embed(), select=list(res.keys()))


if __name__ == '__main__':
    app.run(debug=True)
